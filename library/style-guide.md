# Style guide

The team's house style for everything it writes: notes, reports, charts, messages and this repo. When an employer or publication has its own style guide, that guide wins for products going there.

Main references:

- [Canada.ca Content Style Guide](https://design.canada.ca/style-guide/), especially its plain-language section.
- Treasury Board's [Guidelines on Making Communications Products and Activities Accessible](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32728).
- The Language Portal of Canada's [Writing Tips Plus](https://www.noslangues-ourlanguages.gc.ca/en/writing-tips-plus/) for questions of Canadian usage.
- The BC [Policy on the use of generative AI](https://digital.gov.bc.ca/ai/gen-ai-policy/), which requires AI-assisted text to be edited to align with government style guides and to be inclusive and respectful.

## 1. Plain language

- **Bottom line first.** The first sentence says what the reader needs to know or do.
- **Short sentences.** One idea per sentence. Aim for most sentences under 25 words.
- **Short paragraphs.** Three to five sentences.
- **Active voice.** "The team reviewed the data", not "The data were reviewed".
- **Common words.** "Use", not "utilize". "Help", not "facilitate". "About", not "approximately" (unless precision matters).
- **Verbs, not nouns made from verbs.** "We analysed", not "We conducted an analysis of".
- **Explain terms** the reader may not know, the first time they appear. Spell out acronyms on first use.
- **Be specific.** "BC consumer prices rose 2.6% in 2024 (annual average; Statistics Canada Table 18-10-0005-01)", not "Prices rose significantly".
- **Say how sure you are**, when it matters: "likely", "the evidence is mixed", "we could not find data on ...".
- **No hype.** Avoid "game-changing", "revolutionary", "cutting-edge", "robust" (unless the statistical meaning), "leverage" (as a verb).

## 2. Canadian spelling

Use Canadian spelling. Common cases:

| Use | Not |
| --- | --- |
| analyse, analysed, analysing | analyze |
| behaviour, colour, favour, labour, neighbour | behavior, color |
| centre, metre, litre | center, meter |
| cheque | check (for payment) |
| defence, licence (noun), practice (noun) | defense, license (noun) |
| license, practise (verbs) | licence, practice (verbs) |
| catalogue, dialogue | catalog, dialog |
| modelling, modeller, travelled, cancelled | modeling, traveled |
| program (all senses) | programme |
| organization, organize, recognize, prioritize | organisation (use -ize, as is usual in Canada) |
| fulfil, enrol, instalment | fulfill, enroll, installment |

Exceptions: keep official names as their owners spell them (for example, a US agency's "Center"), and keep code, file names and API fields as they are.

## 3. Numbers, dates and units

- **Dates:** ISO format in tables, logs and file names (`2026-10-31`). In running text, "October 31, 2026".
- **Reference periods** are stated with every figure: "2024 annual average", "September 2026".
- **Percentages:** use the % sign with numerals ("2.6%"). Say "percentage points" for differences between percentages.
- **Large numbers:** use commas as thousands separators in English ("12,500"). Use "million" and "billion" in text ("$4.2 million").
- **Currency:** "$" means Canadian dollars unless stated. Write "US$" for US dollars. State the price base for real values ("2025 dollars").
- **Rounding:** round for readability in text, but keep the precision of the source in tables. Say when derived figures are computed from rounded values.
- **Index values:** state the base ("2002=100").
- **Ranges:** "2015 to 2025" in text; "2015–2025" in tables and charts.

## 4. Citations

- Every figure, quote and factual claim has a citation.
- **In notes and reports:** a short reference in brackets in the text, and full citations in a Sources section.
- **Full citation:** issuing body or author, title, table or series ID if any, date published or reference period, link, and retrieval date.
  - Example: Statistics Canada. *Consumer Price Index, annual average, not seasonally adjusted*. Table 18-10-0005-01. https://doi.org/10.25318/1810000501-eng. Retrieved 2026-10-31.
- **Legislation:** name, chapter or citation, section, and the "current to" date of the consolidation.
- **Quotes** are exact, in quotation marks, with page or section.

## 5. Structure of written products

- Use the [briefing note](../templates/briefing-note.md) and [decision note](../templates/decision-note.md) templates.
- Headings that say something ("BC inflation tracked Canada's closely"), not just labels ("Results"), where the format allows.
- Lists for parallel items; tables for comparisons; prose for reasoning.
- One page is better than two. Two pages is the default maximum for a note.

## 6. Charts

See the [chart and dashboard skill](../skills/chart-dashboard-build/SKILL.md). In short:

- Title states the takeaway.
- Axis labels with units.
- Source line on every chart: source, table or series ID, reference period, retrieval date.
- Accessible colours; alt text; readable in greyscale.

## 7. Inclusive and respectful language

- Describe people and groups as they describe themselves, where known.
- Use gender-neutral terms ("chair", "workers", "they").
- Avoid language that stereotypes or stigmatizes.
- Follow current BC and Government of Canada guidance on terminology for Indigenous Peoples.

## 8. Messages and this repo

- Messages between agents use the [communication protocol](../org/communication-protocol.md) formats.
- Use the role names exactly as in [`org/team.yaml`](../org/team.yaml): "Lead PM", "QA Reviewer", and so on.
- Placeholders: `[PLACEHOLDER: ...]`. Unknowns: `[UNKNOWN: ...]`. Unverified: `[UNVERIFIED]`.
