---
name: data-sourcing-validation
description: Finds the right dataset, retrieves it by script, and validates it against published figures. Use whenever a request needs data from Statistics Canada, BC Stats, Bank of Canada, IRCC, FRED, open data portals or approved administrative data, before any analysis begins.
license: MIT
metadata:
  owner: data-engineer
  used-by: data-engineer automation-engineer
  version: "0.1.0"
---

# Data sourcing and validation

## Inputs

- The data need: variables, geography, frequency, period, units (from the handoff).
- The [data sources catalogue](../../library/data-sources/canada-bc.md).
- The request's handling label.

## Steps

1. **Specify the need** in a short table: concept, preferred measure, geography, frequency, period, units.
2. **Choose the source.** Prefer the official producer (for example, [Statistics Canada](https://www.statcan.gc.ca/en/developers/wds) for CPI and the Labour Force Survey, the [Bank of Canada](https://www.bankofcanada.ca/valet/docs) for interest and exchange rates). Use aggregators such as [FRED](https://fred.stlouisfed.org/) only when the original is not practical, and record the original source.
3. **Check definitions.** Read the source's notes and methodology. Confirm the measure matches the concept. Note seasonal adjustment, base period, scaling and any breaks.
4. **Retrieve by script.** Use the API or a documented download URL. Save the raw file unchanged, with the retrieval date in the file name or metadata.
5. **Record identifiers:** table ID, vector or series ID, reference period, units, scaling factor, release or vintage date, retrieval date.
6. **Load and reshape in code.** Never edit raw files.
7. **Validate:**
   - Row and column counts as expected.
   - Values in plausible ranges; no unexpected negatives or zeros.
   - Missing values and status flags (for example, "x" for suppressed, "F" for too unreliable, "E" for use with caution) handled and counted.
   - Units and scaling consistent across series.
   - At least one value reconciled to the producer's published table or release.
8. **Check licence and label.** Record the licence (for example, the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence)). Confirm the data's label fits where it will be used.
9. **Document** with a [data documentation card](../../templates/data-documentation-card.md).
10. **Hand on** with any warnings the analysts must know.

## Outputs

- Pipeline script and README.
- Raw and processed data (stored according to label).
- Data documentation card.
- Validation results: check, result, action.

## Done when

- [ ] The pipeline runs from a clean start and reproduces the processed data.
- [ ] Identifiers, units, reference periods and retrieval dates are recorded.
- [ ] At least one value reconciles to the published source.
- [ ] Status flags and suppression are handled and documented.
- [ ] The data documentation card is complete.

## Common pitfalls

- Mixing seasonally adjusted and unadjusted series.
- Ignoring a base-year change or a series break.
- Using an aggregator's copy when the original has been revised.
- Computing percentage changes from rounded index values without saying so; they can differ slightly from the producer's published rates.
