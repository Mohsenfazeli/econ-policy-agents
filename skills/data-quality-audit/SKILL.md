---
name: data-quality-audit
description: Systematically checks a dataset for completeness, accuracy, consistency, timeliness and fitness for the question. Use after data are sourced and before analysis, whenever data are joined or transformed, and by the QA Reviewer when checking a deliverable's data.
license: MIT
metadata:
  owner: data-engineer
  used-by: data-engineer econometrician qa-reviewer
  version: "0.1.0"
---

# Data-quality audit

The checks below follow common dimensions of data quality: relevance, accuracy, timeliness, accessibility, interpretability and coherence. Statistics Canada's [Quality Guidelines](https://www150.statcan.gc.ca/n1/en/catalogue/12-539-X) are a useful reference.

## Inputs

- The dataset (raw and processed) and its pipeline.
- The data documentation card.
- The question the data must answer.

## Steps

1. **Relevance.** Does the measure match the concept in the question? Note any gap (for example, a national series used as a proxy for BC).
2. **Completeness.**
   - Count missing values by variable and period.
   - Count suppressed or flagged values.
   - Check that all expected geographies and periods are present.
3. **Accuracy.**
   - Reconcile totals and selected values to the published source.
   - Check ranges and outliers; investigate any value more than a plausible distance from its neighbours.
   - For survey data, check that estimates flagged as unreliable are not used as if precise.
4. **Consistency.**
   - Units and scaling are the same across series being compared.
   - Definitions do not change over the period, or the break is documented.
   - Joins: count matched, unmatched and duplicated keys on both sides.
   - Subtotals add to totals, within rounding.
5. **Timeliness.** Record the reference period and release date. Note whether newer data or revisions are available.
6. **Interpretability.** Is the documentation enough for someone else to use the data correctly?
7. **Transformations.** Re-run the pipeline from a clean start. Compare outputs to the previous run.
8. **Record results** in an audit table and decide an action for each issue: fix, document, or escalate.

## Outputs

| Check | Dimension | Result | Issue | Action |
| --- | --- | --- | --- | --- |

Plus a one-line overall rating: fit for purpose, fit with caveats (listed), or not fit.

## Done when

- [ ] Every dimension above was checked.
- [ ] At least one reconciliation to the published source was done.
- [ ] Join diagnostics were recorded for every join.
- [ ] Each issue has an action.
- [ ] The overall rating is stated.

## Common pitfalls

- Checking only that the code runs, not that the values are right.
- Dropping unmatched rows in a join without counting them.
- Treating suppressed values as zero.
