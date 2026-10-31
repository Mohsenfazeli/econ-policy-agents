# AGENTS.md

Instructions for AI coding agents (and people) editing this repository. For what the repo is, see [README.md](README.md).

## What this repo is

Markdown and YAML documents that define a team of 11 AI agents: organization rules in `org/`, roles in `agents/`, skills in `skills/`, processes, templates, a public context library and one worked example. There is almost no code: `scripts/check_repo.py` and `examples/cpi-fee-indexing/fetch_cpi.py`.

## Rules that always apply

- Never invent data, figures, sources, quotes, dates, links or employers. Every link must point to a real page. Placeholders use the form `[PLACEHOLDER: ...]`.
- Never add confidential material: no regulated company names, internal government figures, unpublished findings, internal dashboards, internal URLs or file paths, or personal information.
- No data extracts, Excel outputs or dashboard files from real work. `.gitignore` blocks common data formats; do not force-add them.
- Do not push to `main`. Work on a branch and open a pull request. Mohsen Fazeli approves every merge.
- Plain, direct language and Canadian spelling, per [`library/style-guide.md`](library/style-guide.md).

## Consistency rules

- [`org/team.yaml`](org/team.yaml) is the single source of truth for role slugs, display names, reporting lines and skill assignments.
- Role names are always written exactly as in `team.yaml` (for example "Lead PM", "QA Reviewer", "Financial Modeller").
- Each agent has `agents/<slug>/role-card.md` and `agents/<slug>/system-prompt.md`. The prompt's frontmatter `name` equals the slug.
- Each skill is `skills/<name>/SKILL.md`. Frontmatter `name` equals the folder name; `metadata.owner` and `metadata.used-by` match `team.yaml`.
- If you change a role or skill assignment, update `team.yaml`, the role card, the system prompt, the skill's frontmatter and the tables in `agents/README.md` and `skills/README.md` together.

## Checks

```bash
pip install pyyaml
python scripts/check_repo.py
```

The script validates the rules above and checks that relative links resolve. CI runs it on every pull request.

## Commits and changelog

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style messages where practical (`docs:`, `feat:`, `fix:`). Record user-visible changes under `Unreleased` in [CHANGELOG.md](CHANGELOG.md).
