# Agents

One folder per agent. Each folder has:

- `role-card.md`: the job description, for people. Purpose, responsibilities, inputs and outputs, handoffs, skills, tools and access, quality bar, what it must never do, and when to escalate.
- `system-prompt.md`: the ready-to-paste prompt, for tools. YAML frontmatter (`name`, `description`, `tools-guidance`) followed by the prompt body. Paste everything after the closing `---` into an assistant's instructions. See [`docs/adapters.md`](../docs/adapters.md) for specific tools.

Every system prompt repeats the team's non-negotiable rules and working conventions, so each one works on its own.

| Role | Folder | Reports to | Owns skills |
| --- | --- | --- | --- |
| Lead PM | [`lead-pm/`](lead-pm/role-card.md) | Mohsen Fazeli | project-intake-scoping |
| Research Librarian | [`research-librarian/`](research-librarian/role-card.md) | Lead PM | literature-review |
| Data Engineer | [`data-engineer/`](data-engineer/role-card.md) | Lead PM | data-sourcing-validation, data-quality-audit |
| Econometrician | [`econometrician/`](econometrician/role-card.md) | Lead PM | regression-analysis, forecasting |
| Applied Economist | [`applied-economist/`](applied-economist/role-card.md) | Lead PM | market-monitoring, cost-benefit-analysis |
| Policy Designer | [`policy-designer/`](policy-designer/role-card.md) | Lead PM | policy-options-analysis |
| Financial Modeller | [`financial-modeller/`](financial-modeller/role-card.md) | Lead PM | financial-model-build |
| Dataviz Builder | [`dataviz-builder/`](dataviz-builder/role-card.md) | Lead PM | chart-dashboard-build |
| Writer | [`writer/`](writer/role-card.md) | Lead PM | briefing-note, decision-note |
| Automation Engineer | [`automation-engineer/`](automation-engineer/role-card.md) | Lead PM | None (uses data-sourcing-validation, chart-dashboard-build) |
| QA Reviewer | [`qa-reviewer/`](qa-reviewer/role-card.md) | Mohsen Fazeli | qa-review |

The QA Reviewer reports to Mohsen rather than the Lead PM so that the Lead PM cannot overrule a fail.

## Changing a role

1. Edit [`org/team.yaml`](../org/team.yaml) first if the name, purpose or skills change.
2. Update the role card and system prompt together. Keep the shared rules block identical across all prompts.
3. Run `python scripts/check_repo.py`.
4. Open a pull request and add a line to [`CHANGELOG.md`](../CHANGELOG.md).
