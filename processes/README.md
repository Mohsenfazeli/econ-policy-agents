# Processes

End-to-end workflows. Each process names the stages, the role accountable for each, the skill used, and the exit criterion that must be met before moving on. All processes share the three gates in [`org/governance.md`](../org/governance.md): scope (G1), QA (G2) and approval (G3).

| Process | Use for |
| --- | --- |
| [Request intake](request-intake.md) | Every new request |
| [Standard analysis pipeline](standard-analysis-pipeline.md) | Data and economic analysis questions |
| [Policy briefing pipeline](policy-briefing-pipeline.md) | Questions that end in a briefing note or decision note on policy options |
| [Dashboard build](dashboard-build.md) | New or changed dashboards |
| [Code change via pull request](code-change-via-pr.md) | Any change to code, tools, prompts, skills or this repo |
| [QA and sign-off](qa-and-sign-off.md) | Every deliverable, at the end of every pipeline |
| [Retrospective](retrospective.md) | After each standard request, and after any incident |

The Lead PM may skip stages a request does not need (for example, no econometrics in an evidence-only request), and records the choice in the charter. The QA and approval stages are never skipped.
