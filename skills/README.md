# Skills

A skill is a reusable, step-by-step procedure. Roles say *who* is accountable; skills say *how* the work is done. Several roles can use the same skill.

Each skill is a folder containing a `SKILL.md` file that follows the [Agent Skills specification](https://agentskills.io/specification):

- YAML frontmatter with `name` (must match the folder name; lowercase letters, numbers and hyphens) and `description` (what the skill does and when to use it).
- Optional `license` and `metadata` (here: `owner`, `used-by`, `version`).
- A body with inputs, numbered steps, outputs, and a "Done when" checklist.

Keep each `SKILL.md` under 500 lines. Put long reference material in a `references/` subfolder and link to it.

## Catalogue

| Skill | Owner | Use when |
| --- | --- | --- |
| [project-intake-scoping](project-intake-scoping/SKILL.md) | Lead PM | Any new request |
| [literature-review](literature-review/SKILL.md) | Research Librarian | A cited evidence base or jurisdictional scan is needed |
| [data-sourcing-validation](data-sourcing-validation/SKILL.md) | Data Engineer | Data must be found, retrieved and validated |
| [data-quality-audit](data-quality-audit/SKILL.md) | Data Engineer | Before analysis; after joins; during QA |
| [regression-analysis](regression-analysis/SKILL.md) | Econometrician | An estimated relationship or causal effect is needed |
| [forecasting](forecasting/SKILL.md) | Econometrician | Future values or projections are needed |
| [cost-benefit-analysis](cost-benefit-analysis/SKILL.md) | Applied Economist | Options must be compared on net benefit |
| [market-monitoring](market-monitoring/SKILL.md) | Applied Economist | Recurring view of a market's performance |
| [policy-options-analysis](policy-options-analysis/SKILL.md) | Policy Designer | What could be done, and which option is best |
| [financial-model-build](financial-model-build/SKILL.md) | Financial Modeller | Cost, budget, rate or investment calculations |
| [chart-dashboard-build](chart-dashboard-build/SKILL.md) | Dataviz Builder | Any chart, map or dashboard |
| [briefing-note](briefing-note/SKILL.md) | Writer | A concise note to inform a senior reader |
| [decision-note](decision-note/SKILL.md) | Writer | A senior reader must choose among options |
| [qa-review](qa-review/SKILL.md) | QA Reviewer | Before anything reaches Mohsen; every pull request |

## Adding a skill

1. Create `skills/<name>/SKILL.md` with the frontmatter above.
2. Set `metadata.owner` to one role slug from [`org/team.yaml`](../org/team.yaml), and add the skill to that role's `skills_owned`.
3. List every role that uses it in `metadata.used-by`, and add it to those roles' `skills_used`.
4. Run `python scripts/check_repo.py`.
5. Open a pull request.
