---
name: qa-review
description: Independently reviews a deliverable against the QA checklist (numbers against sources, methods, citations, confidentiality, style), logs every issue with a severity and a suggested fix, and gives an explicit PASS or FAIL. Use before any deliverable goes to Mohsen, and on every pull request before merge.
license: MIT
metadata:
  owner: qa-reviewer
  used-by: qa-reviewer
  version: "0.1.0"
---

# QA review

Use the [QA checklist template](../../templates/qa-checklist.md) for the report.

## Severity levels

| Severity | Meaning | Effect |
| --- | --- | --- |
| **Critical** | A wrong figure or claim that changes a conclusion; an invented or misattributed source, quote or link; a confidentiality breach | Blocks release |
| **Major** | A method flaw; an unsupported claim; a key figure without a citation; a missing material caveat; a deliverable that does not answer the charter question | Blocks release |
| **Minor** | An error that does not change a conclusion (rounding, labels, formatting, wording) | Fix before release unless Mohsen waives it |
| **Note** | A suggestion | Optional |

**Verdict rule:** PASS only when no critical or major issues are open. Otherwise FAIL. Only Mohsen can accept a release with an open major issue, in writing in the QA report. Nobody can accept an open critical issue.

## Inputs

- The deliverable and its version.
- The charter.
- Sources, data, code, assumptions log, risk log and data documentation cards.
- The author's figure and citation list.

## Steps

1. **Check independence.** Confirm you did not author or substantially edit the deliverable. If you did, tell the Lead PM and stop.
2. **Read the charter.** Note the question, audience and label.
3. **Accuracy.** For every figure: find it in the source or reproduce it from saved code. Check units, reference periods and rounding. Recalculate derived figures (percentage changes, totals, ratios).
4. **Sources.** Open every link. Confirm each source exists, is correctly cited, and says what is claimed. Check quotes word for word.
5. **Methods.** Is the method suitable for the question? Are assumptions stated? Is causal language supported by the design? Is uncertainty reported?
6. **Assumptions and data.** Every assumption is logged. Data documentation cards exist. Placeholders and unknowns are labelled, not presented as facts.
7. **Confidentiality.** Run the confidentiality section of the checklist. For anything public: no regulated company names, internal figures, unpublished findings, internal dashboards, screenshots, internal URLs or personal information.
8. **Style and completeness.** Bottom line first, plain language, Canadian spelling, within length, answers the charter question.
9. **Charts.** Title, labels, units, source line, dates, alt text; values match the data.
10. **Code (for pull requests).** Tests pass; README updated; no secrets or real data; behaviour matches the description.
11. **Log issues:** ID (`QA-1`, `QA-2`, ...), location, severity, description, suggested fix.
12. **Give the verdict** using the rule above.
13. **List what Mohsen should check personally:** the two to five points where his judgment matters most.
14. **Record what was not checked**, if anything, and why.
15. **Send the QA VERDICT message** with the report.

## Re-review

When a fixed version comes back, check every open issue, then re-check any part of the deliverable that changed. Update the issue log status (open, fixed, waived by Mohsen).

## Done when

- [ ] Every figure was checked or reproduced, or the report lists what was not and why.
- [ ] Every link was opened.
- [ ] The confidentiality section was completed.
- [ ] Every issue has a severity and a suggested fix.
- [ ] The verdict follows the rule.
- [ ] The report lists what Mohsen should check personally and which roles contributed.
