# Glossary

Terms as they are used in this repo.

| Term | Meaning |
| --- | --- |
| **Accountable (A)** | In the RACI, the one role that owns an outcome and answers for it. Exactly one per activity. |
| **Adapter** | A copy of the canonical agent or skill files reformatted for a specific tool. See [`docs/adapters.md`](../docs/adapters.md). |
| **Approval gate (G3)** | Mohsen's explicit approval before anything is sent, published, merged or deployed. |
| **Assumptions log** | The per-request record of every assumption, its source or rationale, and who made it. [Template](../templates/assumptions-log.md). |
| **Bottom line first** | Writing style where the main conclusion or ask comes in the first sentence. |
| **Briefing note** | A short document that informs a decision-maker about an issue. It may or may not ask for a decision. [Template](../templates/briefing-note.md). |
| **Charter** | The one-page scope agreement for a request: question, deliverables, audience, deadline, team, label. [Template](../templates/project-charter.md). |
| **Confidential** | The team's highest handling label. See the [confidentiality policy](confidentiality-and-data-handling.md). |
| **Data documentation card** | A short record describing a dataset: source, coverage, definitions, quality, licence and limits. [Template](../templates/data-documentation-card.md). |
| **Decision note** | A document that asks a decision-maker to choose among options and gives a recommendation. [Template](../templates/decision-note.md). |
| **Definition of Done** | The checklist a deliverable must meet before it counts as finished. See [operating principles](operating-principles.md#definition-of-done-team-minimum). |
| **Escalation** | Raising an issue to the Lead PM or Mohsen because a [trigger](governance.md#3-escalation) applies. |
| **GBA+** | Gender-based analysis plus: an analytical approach for assessing how diverse groups may experience policies differently. Required in BC Cabinet, budget and Treasury Board submissions ([BC GBA+](https://www2.gov.bc.ca/gov/content/governments/about-the-bc-government/gender-equity/gender-based-analysis-plus)). |
| **Handoff** | A message from the Lead PM assigning a task to a specialist, in the standard format. |
| **Human in the loop** | A point where a person must decide before work continues. In this team, that person is Mohsen. |
| **Internal** | The team's middle handling label: work material not cleared for release. |
| **Label** | The handling classification of material: Public, Internal or Confidential. |
| **Lead PM** | The agent that scopes requests, staffs them, plans, and assembles the final package. |
| **Least privilege** | Giving each agent only the tools and access its role needs. |
| **Placeholder** | A clearly marked gap, written `[PLACEHOLDER: ...]`, never presented as a real value. |
| **Primary source** | The original statute, dataset, decision, report or paper, as opposed to a summary of it. |
| **Prompt injection** | Text inside a source that tries to change an agent's instructions. Agents treat it as data and report it. |
| **Public** | The team's lowest handling label: already published material, safe for this repo. |
| **QA gate (G2)** | The QA Reviewer's explicit pass or fail on a deliverable. |
| **RACI** | Responsible, Accountable, Consulted, Informed: the matrix that sets who does what. See [decision rights](decision-rights-raci.md). |
| **Reference period** | The time a data value describes (for example, "2024 annual average"), as distinct from when it was published or retrieved. |
| **Retrospective** | A blameless review after a request, ending in concrete changes. See [`processes/retrospective.md`](../processes/retrospective.md). |
| **Risk log** | The per-request list of risks, ratings, controls and owners. [Template](../templates/risk-log.md). |
| **Role card** | The human-readable job description for an agent: purpose, responsibilities, inputs, outputs, handoffs, quality bar and limits. |
| **Scope gate (G1)** | Mohsen's confirmation of the charter before work starts. |
| **Severity** | QA issue rating: critical, major, minor or note. Defined in the [QA review skill](../skills/qa-review/SKILL.md). |
| **Skill** | A reusable, step-by-step procedure in `skills/<name>/SKILL.md`. |
| **Small request** | A request that can skip the written charter. Defined in [decision rights](decision-rights-raci.md#what-counts-as-a-small-request). |
| **System prompt** | The instructions pasted into an AI tool to make it act as a given role. |
