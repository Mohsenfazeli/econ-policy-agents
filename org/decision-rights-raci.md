# Decision rights and RACI

## Rules for reading the matrix

- **R (Responsible)** does the work. There can be several.
- **A (Accountable)** owns the outcome and answers for it. There is exactly one per row.
- **C (Consulted)** gives input before the work is finished (two-way).
- **I (Informed)** is told the result (one-way).
- A blank cell means not normally involved. The Lead PM can add a role to any activity.
- An agent can never be Accountable for anything that leaves the team. Mohsen is.

This follows PMI's RACI guidance, especially "one Accountable owner per outcome" ([PMI](https://www.pmi.org/blog/stakeholder-management-raci)).

## Column key

| Code | Role |
| --- | --- |
| MF | Mohsen Fazeli (owner, human) |
| PM | Lead PM |
| RL | Research Librarian |
| DE | Data Engineer |
| EC | Econometrician |
| AE | Applied Economist |
| PD | Policy Designer |
| FM | Financial Modeller |
| DV | Dataviz Builder |
| WR | Writer |
| AU | Automation Engineer |
| QA | QA Reviewer |

## Matrix

| Activity | MF | PM | RL | DE | EC | AE | PD | FM | DV | WR | AU | QA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set priorities across requests | A | R | | | | | | | | | | I |
| Intake and scoping | C | A/R | C | C | C | C | C | C | C | C | C | I |
| Approve project charter (scope gate) | A | R | | | | | | | | | | I |
| Choose specialists for a request | I | A/R | | | | | | | | | | |
| Change scope, deadline or deliverables | A | R | | | | | | | | | | I |
| Evidence and literature review | | C | A/R | | C | C | C | | | | | I |
| Data sourcing and pipelines | | C | C | A/R | C | C | | | | | C | I |
| Data-quality audit | | I | | A/R | C | C | | | | | | C |
| Econometric analysis and forecasting | | C | C | C | A/R | C | | | | | | I |
| Market, cost and impact analysis | | C | C | C | C | A/R | C | C | | | | I |
| Cost-benefit analysis | | C | C | C | C | A/R | C | R | | | | I |
| Policy options and trade-offs | C | C | C | | | C | A/R | C | | C | | I |
| Financial model | | C | | C | | C | | A/R | | | | I |
| Charts, maps and dashboards | | C | | C | C | C | | | A/R | C | C | I |
| Drafting written products | | C | C | | C | C | C | C | C | A/R | | I |
| Scripts, tools and automation | C | C | | C | | | | | C | | A/R | I |
| Assemble final package | I | A/R | | | | | | | | R | | I |
| QA review and pass/fail verdict | I | I | C | C | C | C | C | C | C | C | C | A/R |
| Approve release (send, publish, merge, deploy) | A | R | | | | | | | | | | C |
| Merge a pull request | A | I | | | | | | | | | R | C |
| Declare a confidentiality incident | A | R | R | R | R | R | R | R | R | R | R | R |
| Retrospective and process changes | A | R | C | C | C | C | C | C | C | C | C | C |

Notes:

- **QA independence.** The QA Reviewer reports to Mohsen, not to the Lead PM, so the Lead PM cannot overrule a fail. Only Mohsen can accept a deliverable with open major issues, and he must do so in writing in the QA report.
- **Technical soundness** of each work product stays with the specialist who produced it (Accountable in its own row). QA checks it; QA does not take ownership of it.
- **Anyone can raise a confidentiality incident.** Every agent is Responsible for stopping work and reporting; Mohsen is Accountable for the response.

## Decision rights summary

| Decision | Who decides | Who must be consulted |
| --- | --- | --- |
| What the team works on, and in what order | Mohsen | Lead PM |
| Whether a request needs a charter | Lead PM (small requests can skip it) | Mohsen, if unsure |
| Which specialists to involve | Lead PM | The specialists, on feasibility |
| Methods within a specialty | The specialist | QA Reviewer, Lead PM |
| Pass or fail at the QA gate | QA Reviewer | The author |
| Accept a known limitation and release anyway | Mohsen | QA Reviewer, Lead PM |
| Send, publish, merge or deploy | Mohsen | QA Reviewer |
| Change a rule in this repo | Mohsen (by merging the pull request) | Affected roles |

## What counts as a small request

A request is small if all of these are true. Small requests skip the written charter but still go through QA and approval.

- One specialist (plus QA) can do it.
- It uses only public sources or material Mohsen has provided for the request.
- It is not going to anyone outside the team in its current form, or it is a single short product such as a one-paragraph summary.
- It can be reviewed in one pass.

If in doubt, write the charter.
