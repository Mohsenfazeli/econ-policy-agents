#!/usr/bin/env python3
"""Consistency checks for the econ-policy-agents repo.

Validates the repo against org/team.yaml: agent folders and prompts, skill
frontmatter and assignments, and relative Markdown links. Exits non-zero on
any error. Requires PyYAML.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "outputs", ".venv", "venv"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")

errors: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)


def frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(f"{rel(path)}: missing YAML frontmatter")
        return None
    end = text.find("\n---", 4)
    if end == -1:
        error(f"{rel(path)}: unterminated YAML frontmatter")
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        error(f"{rel(path)}: frontmatter does not parse: {exc}")
        return None
    if not isinstance(data, dict):
        error(f"{rel(path)}: frontmatter is not a mapping")
        return None
    return data


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def markdown_files() -> list[Path]:
    return [
        p for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    ]


def heading_anchors(path: Path) -> set[str]:
    anchors = set()
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line.startswith("#"):
            continue
        title = line.lstrip("#").strip().lower()
        title = re.sub(r"[^\w\- ]", "", title)
        anchors.add(title.replace(" ", "-"))
    return anchors


def check_team(team: dict) -> tuple[dict, set[str]]:
    agents = {a["slug"]: a for a in team.get("agents", [])}
    if len(agents) != 11:
        error(f"org/team.yaml: expected 11 agents, found {len(agents)}")
    for slug, agent in agents.items():
        for key in ("display_name", "purpose", "reports_to", "skills_owned", "skills_used"):
            if key not in agent:
                error(f"org/team.yaml: agent {slug} missing {key}")
        if agent.get("reports_to") not in set(agents) | {"owner"}:
            error(f"org/team.yaml: agent {slug} reports to unknown {agent.get('reports_to')}")

    folders = {p.name for p in (ROOT / "agents").iterdir() if p.is_dir()}
    for slug in agents:
        if slug not in folders:
            error(f"agents/{slug}/: folder missing for agent in team.yaml")
    for folder in folders - set(agents):
        error(f"agents/{folder}/: folder has no entry in team.yaml")

    owned: dict[str, str] = {}
    for slug, agent in agents.items():
        for skill in agent.get("skills_owned", []):
            if skill in owned:
                error(f"org/team.yaml: skill {skill} owned by both {owned[skill]} and {slug}")
            owned[skill] = slug
    return agents, set(owned)


def check_agents(agents: dict) -> None:
    for slug, agent in agents.items():
        folder = ROOT / "agents" / slug
        for name in ("role-card.md", "system-prompt.md"):
            if not (folder / name).is_file():
                error(f"agents/{slug}/{name}: missing")
        prompt = folder / "system-prompt.md"
        if prompt.is_file():
            fm = frontmatter(prompt)
            if fm is not None:
                if fm.get("name") != slug:
                    error(f"{rel(prompt)}: frontmatter name {fm.get('name')!r} != {slug!r}")
                if not fm.get("description"):
                    error(f"{rel(prompt)}: frontmatter description missing")
        card = folder / "role-card.md"
        if card.is_file():
            first = card.read_text(encoding="utf-8").splitlines()[0]
            if agent["display_name"] not in first:
                error(f"{rel(card)}: title does not use display name {agent['display_name']!r}")
            text = card.read_text(encoding="utf-8")
            for skill in agent.get("skills_owned", []) + agent.get("skills_used", []):
                if skill not in text:
                    error(f"{rel(card)}: does not mention skill {skill}")


def check_skills(agents: dict, owned: set[str]) -> None:
    folders = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    for skill in owned - folders:
        error(f"skills/{skill}/: folder missing for skill owned in team.yaml")
    for skill in sorted(folders):
        path = ROOT / "skills" / skill / "SKILL.md"
        if not path.is_file():
            error(f"skills/{skill}/SKILL.md: missing")
            continue
        lines = path.read_text(encoding="utf-8").count("\n")
        if lines > 500:
            error(f"{rel(path)}: {lines} lines; keep SKILL.md under 500")
        fm = frontmatter(path)
        if fm is None:
            continue
        name = fm.get("name")
        if name != skill:
            error(f"{rel(path)}: name {name!r} != folder {skill!r}")
        if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
            error(f"{rel(path)}: name must be lowercase letters, digits and hyphens, max 64")
        desc = fm.get("description")
        if not isinstance(desc, str) or not desc.strip():
            error(f"{rel(path)}: description missing")
        elif len(desc) > 1024:
            error(f"{rel(path)}: description longer than 1024 characters")
        meta = fm.get("metadata") or {}
        if not isinstance(meta, dict) or not all(isinstance(v, str) for v in meta.values()):
            error(f"{rel(path)}: metadata must be a map of strings")
            continue
        expected_owner = next(
            (s for s, a in agents.items() if skill in a.get("skills_owned", [])), None
        )
        if meta.get("owner") != expected_owner:
            error(f"{rel(path)}: owner {meta.get('owner')!r} != team.yaml {expected_owner!r}")
        expected_users = {
            s for s, a in agents.items()
            if skill in a.get("skills_owned", []) or skill in a.get("skills_used", [])
        }
        actual_users = set(meta.get("used-by", "").split())
        if actual_users != expected_users:
            error(
                f"{rel(path)}: used-by {sorted(actual_users)} != team.yaml {sorted(expected_users)}"
            )
    for slug, agent in agents.items():
        for skill in agent.get("skills_used", []):
            if skill not in folders:
                error(f"org/team.yaml: {slug} uses unknown skill {skill}")


def check_links() -> None:
    for path in markdown_files():
        in_code = False
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for match in LINK_RE.finditer(line):
                target = match.group(1) or match.group(2)
                if re.match(r"^[a-z]+:", target) or target.startswith("#") and len(target) == 1:
                    continue
                file_part, _, anchor = target.partition("#")
                dest = path if not file_part else (path.parent / file_part).resolve()
                if not dest.exists():
                    error(f"{rel(path)}:{lineno}: broken link {target}")
                    continue
                if anchor and dest.suffix == ".md" and anchor not in heading_anchors(dest):
                    error(f"{rel(path)}:{lineno}: missing anchor #{anchor} in {target}")


def main() -> int:
    team = yaml.safe_load((ROOT / "org" / "team.yaml").read_text(encoding="utf-8"))
    agents, owned = check_team(team)
    check_agents(agents)
    check_skills(agents, owned)
    check_links()
    for msg in errors:
        print(f"ERROR {msg}")
    if errors:
        print(f"\n{len(errors)} error(s)")
        return 1
    print(f"OK: {len(agents)} agents, {len(list((ROOT / 'skills').glob('*/SKILL.md')))} skills, "
          f"{len(markdown_files())} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
