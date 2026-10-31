# Confidentiality and data-handling policy

## Purpose

The owner of this team works in the BC public service. Much of the work the team supports is confidential. This policy sets out how the team protects that material, and what may appear in this public repo.

This policy is a floor, not a ceiling. When work is done for an employer, the employer's policies apply and take precedence wherever they are stricter. For BC public-service work that includes the [BC Policy on the use of generative AI](https://digital.gov.bc.ca/ai/gen-ai-policy/), which, among other things, says employees must not put confidential information, including personal information, into publicly available gen AI tools. Personal information in BC public bodies is governed by the [Freedom of Information and Protection of Privacy Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96165_00).

## Team classification labels

These labels are for the team's own handling. They do not replace any employer's official classification scheme. When an official classification exists, use it and apply the stricter handling.

| Label | What it covers | Where it may go |
| --- | --- | --- |
| **Public** | Published statistics, laws, public reports, open data, published papers, this repo's contents | Anywhere, including this repo |
| **Internal** | Work-in-progress analysis, drafts, notes, methods applied to a real file, anything Mohsen has not cleared for release | Private workspace and tools approved for it; never this repo |
| **Confidential** | Government-internal figures, unpublished findings, names of regulated companies in a work context, internal dashboards, Cabinet or Treasury Board material, personal information, legal advice | Only tools and storage approved by the employer for that material; never this repo; never a public AI tool |

If in doubt, treat it as Confidential and ask.

## What this public repo may hold

- Code, templates, prompts, skills and process documents.
- Summaries that describe methods and the *kinds* of decisions supported.
- Worked examples built entirely on public data and public sources.
- References to public laws, public datasets and published reports.

## What this public repo must never hold

- Data extracts, spreadsheet outputs, model files or dashboards from real work, even if they look harmless.
- Internal figures, unpublished findings, or results of real analysis.
- Names of regulated companies, applicants, licensees or individuals connected with real files.
- Screenshots of internal systems, dashboards or documents.
- Details of confidential matters before any decision-making body, including the BC Passenger Transportation Board. Saying that the team supports work in passenger transportation economics in general terms is fine.
- Credentials, tokens, internal URLs, server names or file paths.
- Anything about a real person that is not already public and relevant.

## Handling rules for agents

1. **Know the label before you start.** The charter states the highest label of material in the request. If the charter does not say, ask the Lead PM.
2. **Use only approved tools for Internal and Confidential material.** If you are not sure a tool is approved for the label, stop and ask.
3. **Minimize.** Use the least data needed. Prefer aggregates. Do not copy confidential material into handoffs if a reference to its location will do.
4. **No re-identification.** Do not combine datasets in a way that could identify a person or a business that is not meant to be identifiable.
5. **Respect suppression.** Keep source suppression and rounding rules (for example, IRCC open data rounds and suppresses small counts). Do not try to reverse them.
6. **Strip before sharing.** Before anything moves to a lower label (for example, from a real file to a public example), the Lead PM and QA Reviewer check it line by line, and Mohsen approves.
7. **Keep data out of git.** The repo's `.gitignore` blocks common data and output formats. Do not override it.

## Before anything is made public

The QA Reviewer runs the confidentiality section of the [QA checklist](../templates/qa-checklist.md). In short:

- [ ] No regulated company names, applicant names or personal information.
- [ ] No internal figures or unpublished findings.
- [ ] No internal dashboards, screenshots, URLs or file paths.
- [ ] Every figure comes from a public, cited source.
- [ ] Mohsen has approved publication.

## Incidents

An incident is any case where Internal or Confidential material went, or may have gone, somewhere it should not.

1. **Stop.** Do not continue the task.
2. **Contain** only if it is safe and reversible (for example, do not push a commit that contains the material).
3. **Report** immediately to the Lead PM and Mohsen using the escalation message format, stating what, where, when, and what has been done.
4. **Do not try to fix history yourself** (for example, rewriting git history or deleting messages) unless Mohsen asks.
5. Mohsen decides on next steps, including any reporting the employer requires.
6. Record it in a blameless [retrospective](../processes/retrospective.md).
