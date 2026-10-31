# QA report: REQ-2026-000, briefing note and chart, version 2 (illustrative example)

> Example product from the [worked example](README.md), using the [QA checklist template](../../templates/qa-checklist.md). The issues below are real points found while reviewing this example's data and drafts. The review was carried out by the same AI system that drafted the example, playing the QA Reviewer role. In a real run, the QA Reviewer is a separate agent session that did not draft the product.

**Reviewer:** QA Reviewer · **Date:** 2026-10-31 · **Label:** Public

**Independence:** I did not author or substantially edit this product. ☑ Confirmed (within the limits stated above)

## Verdict

**PASS** (after the fix to QA-1)

Open issues: critical 0 · major 0 · minor 0 · note 2 (both intended or optional)

## Checklist

### A. Accuracy

| # | Check | Result | Note |
| --- | --- | --- | --- |
| A1 | Every figure matches its source or was reproduced from saved code | Pass | Reran `fetch_cpi.py`; all twelve years for both series match the table in the walkthrough |
| A2 | Units, scaling and reference periods are correct and stated | Pass | Index 2002=100, annual averages, 2014 to 2025 |
| A3 | Derived figures recalculated and correct | Pass | Recomputed every annual change, indexed value and real value independently from the CSV; all match to the stated precision. 2015 to 2025: Canada 29.7%, BC 31.9% |
| A4 | Rounding is consistent | Pass | See QA-2 |
| A5 | Figures in text, tables and chart agree | Pass after fix | See QA-1 (fixed) |

### B. Sources and citations

| # | Check | Result | Note |
| --- | --- | --- | --- |
| B1 | Every link opened and works | Pass | S1 table page and DOI; S2 catalogue page |
| B2 | Every source exists and says what is claimed | Pass | |
| B3 | Quotes are exact | N/A | No quotes |
| B4 | Citations complete | Pass | Issuer, title, table number, vectors, link, retrieval date |
| B5 | Sources current enough | Pass | 2025 annual average is the latest complete year at retrieval |
| B6 | Jurisdiction stated; Canadian and BC sources used | Pass | |

### C. Methods

| # | Check | Result | Note |
| --- | --- | --- | --- |
| C1 | Method suits the question | Pass | Simple index ratios are enough for erosion and indexing |
| C2 | Assumptions stated | Pass | Hypothetical fee set in 2015; annual-average indexing |
| C3 | Causal language only where supported | Pass | No causal claims |
| C4 | Uncertainty reported | N/A | Descriptive figures from official statistics; revisions risk noted under D2 |
| C5 | Diagnostics and robustness | N/A | No estimation |
| C6 | Limitations stated | Pass | See QA-3 |

### D. Data

| # | Check | Result | Note |
| --- | --- | --- | --- |
| D1 | Data documentation card exists | Pass | Summary card in the walkthrough |
| D2 | Data-quality audit done; caveats carried into product | Pass | Rounding caveat is in the note. CPI is not normally revised, so revision risk is low |
| D3 | Pipeline reruns and reproduces the data | Pass | Reran on 2026-10-31 |
| D4 | Placeholders labelled | Pass | Recipient, approval and disclosure lines are labelled placeholders |

### E. Confidentiality

| # | Check | Result | Note |
| --- | --- | --- | --- |
| E1 | No regulated company names | Pass | |
| E2 | No internal figures or unpublished findings | Pass | Public Statistics Canada data only |
| E3 | No internal dashboards, internal URLs or file paths | Pass | |
| E4 | No personal information | Pass | |
| E5 | Label matches content | Pass | Public |
| E6 | Tools approved for label | Pass | Public material |

### F. Style and completeness

| # | Check | Result | Note |
| --- | --- | --- | --- |
| F1 | Answers the charter question | Pass | Erosion, whether to index, which index |
| F2 | Bottom line first | Pass | |
| F3 | Plain language | Pass | |
| F4 | Canadian spelling; style guide | Pass | |
| F5 | Within length | Pass | Under two pages |
| F6 | Chart: takeaway title, labels, units, source line, alt text | Pass | |

### G. Code

| # | Check | Result | Note |
| --- | --- | --- | --- |
| G1 | Tests exist and pass | N/A | Script stops on unexpected units or missing years, which serves as the check for this example |
| G2 | README updated | Pass | Rerun instructions in the walkthrough |
| G3 | No secrets or real work data committed | Pass | Generated CSV is in an ignored `outputs/` folder; only the chart is committed |
| G4 | Change matches description | N/A | |
| G5 | Changelog updated | N/A | |

## Issue log

| ID | Location | Severity | Description | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- |
| QA-1 | Briefing note, Discussion, "Which index" | Minor | Version 1 said BC was "slightly higher in most years from 2016 to 2020". The data show BC annual inflation was higher in every year from 2016 to 2020 (for example 1.8% vs 1.4% in 2016; 0.8% vs 0.7% in 2020) | State "in each year from 2016 to 2020" and describe 2021 to 2025 | Fixed |
| QA-2 | Briefing note, Limits; walkthrough table | Note | Annual changes are computed from index values rounded to one decimal, so they can differ by 0.1 point from rates Statistics Canada publishes. The note and the walkthrough already say so | None needed; keep the caveat in any reuse | Closed |
| QA-3 | Briefing note, Limits | Note | Checked that the note says the CPI measures consumer prices, not the cost of delivering a service, so "keeps real value" is not read as "keeps up with costs". It does | None needed | Closed |
| QA-4 | Briefing note, header and sign-off | Note | Recipient, approval and AI disclosure lines are placeholders | Correct for an example; in a real run these are completed only after Mohsen's approval | Open (intended) |
| QA-5 | Briefing note, Bottom line | Note | "About $76" in the bottom line and "$75.84" in Key facts are consistent, but readers may prefer one form | Optional | Open |

## Not checked

The legal authority to change or index a fee is out of scope. The chart's rendering was checked at the committed size only.

## What Mohsen should check personally

1. Whether the hypothetical framing ("a BC program") could be read as describing a real fee. If so, make it more generic.
2. Whether the options list is balanced, or leans toward indexing.
3. The AI disclosure wording before any use.

## Contributors

Lead PM, Research Librarian, Data Engineer, Applied Economist, Policy Designer, Dataviz Builder, Writer.

## Waivers (Mohsen only)

| Issue | Decision | Reason | Date |
| --- | --- | --- | --- |
| | | | |
