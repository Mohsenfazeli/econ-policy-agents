# Contributing

This repo is maintained by Mohsen Fazeli. Suggestions are welcome through issues and pull requests. Mohsen reviews and approves every merge.

## Before you start

- Read [AGENTS.md](AGENTS.md). Its rules apply to people and agents alike.
- Do not include confidential material, real work data or anything you would not want public. See [confidentiality and data handling](org/confidentiality-and-data-handling.md).
- Every source you add must be real and linked. Check that the link opens and says what you claim.

## Making a change

1. Open an issue first for anything larger than a correction, especially changes to roles, gates or non-negotiable rules.
2. Create a branch from `main`.
3. Make the change. Keep role names, slugs and skill assignments consistent with [`org/team.yaml`](org/team.yaml).
4. Run the checks:

   ```bash
   pip install pyyaml
   python scripts/check_repo.py
   ```

5. Add a line under `Unreleased` in [CHANGELOG.md](CHANGELOG.md).
6. Open a pull request using the template. Say what changed and why.

## Adding a skill

1. Create `skills/<skill-name>/SKILL.md`, with a lowercase, hyphenated name that matches the folder.
2. Fill in the frontmatter: `name`, `description` (what it does and when to use it), `license`, and `metadata` with `owner`, `used-by` and `version`.
3. Add the skill to the owner's `skills_owned` and the users' `skills_used` in `org/team.yaml`, and to the role cards, system prompts and `skills/README.md`.

## Adding or changing a role

Changes to roles change who is accountable for what. Update `org/team.yaml`, the RACI, the role card, the system prompt, the org chart in the README and any process that names the role. Expect a major version bump.

## Style

Plain language, bottom line first, Canadian spelling. See the [style guide](library/style-guide.md).
