---
name: project-intake-scoping
description: Turns a new request into a scoped, staffed plan. Use at the start of every request to restate the question, size it as small or standard, set the handling label, write the project charter, choose only the specialists needed, and get Mohsen's approval at the scope gate.
license: MIT
metadata:
  owner: lead-pm
  used-by: lead-pm
  version: "0.1.0"
---

# Project intake and scoping

## Inputs

- The request, in Mohsen's words.
- Any material Mohsen provides, with its handling label.
- The [project charter template](../../templates/project-charter.md).

## Steps

1. **Assign an ID.** `REQ-YYYY-NNN`, next number in sequence.
2. **Restate the request** in one sentence: "Mohsen needs X, for Y, by Z."
3. **Identify the essentials:**
   - The question to answer.
   - The decision it supports, and who makes it.
   - The audience for the product.
   - The deadline, and whether it is fixed.
   - The handling label (Public, Internal, Confidential). If any material is Confidential, the whole request is.
   - What is out of scope.
4. **Ask what is missing.** If any essential is unclear, send Mohsen up to five numbered questions. Do not plan around guesses.
5. **Size it.** It is small only if one specialist can do it, it uses only public or provided material, it is a single short product, and one review pass will do. Otherwise it is standard.
6. **Choose the specialists.** For each role involved, write one line on why. Check each role card's "Must never" list against the task.
7. **Draft the deliverables list.** Format, length, audience and due date for each.
8. **Map the first risks** into a [risk log](../../templates/risk-log.md): data availability, confidentiality, method, timing.
9. **Write the charter** (standard requests) or a short intake note (small requests).
10. **Scope gate.** Send the charter to Mohsen. Wait for explicit approval. Record his reply and any changes.
11. **Plan and hand off.** Break work into tasks (`REQ-YYYY-NNN-T1`, ...) with owner, inputs, dependencies and due dates. Leave time for QA and one round of fixes. Send handoffs using the [handoff template](../../templates/handoff-message.md).

## Outputs

- Intake note or approved project charter.
- Task plan.
- Initial risk log and assumptions log.
- Handoff messages.

## Done when

- [ ] The question, decision, audience, deadline, label and out-of-scope items are written down.
- [ ] Every specialist involved has a stated reason; the QA Reviewer is included.
- [ ] Mohsen has explicitly approved the charter (standard requests).
- [ ] Every handoff has all required fields.

## Common pitfalls

- Staffing every role "just in case". More agents means more handoffs and more cost.
- Treating a vague request as clear. Ask.
- Forgetting to set the label, so specialists do not know which tools they may use.
- Leaving no time for QA.
