# Context library

The library is the team's shared, **public** reference shelf: where to find data, which methods references to trust, and how to write. Agents read it before starting work, and the Research Librarian and Data Engineer keep it current.

## What is here

| Path | Contents | Kept by |
| --- | --- | --- |
| [`data-sources/canada-bc.md`](data-sources/canada-bc.md) | Catalogue of Canadian and BC public data and legal sources, with links | Data Engineer, Research Librarian |
| [`methods/references.md`](methods/references.md) | Methods guides and references the team relies on | Econometrician, Applied Economist |
| [`style-guide.md`](style-guide.md) | Writing and chart style: plain language, Canadian spelling, formats | Writer |

## Where private context lives (not here)

> **This repo is public. Private and confidential context lives outside it.**

The team also needs context that cannot be public: details of real files, internal figures, unpublished findings, internal dashboards, stakeholder correspondence, and drafts. That material is kept in a **private workspace** that Mohsen controls, in storage and tools approved for its handling label (see the [confidentiality policy](../org/confidentiality-and-data-handling.md)).

The private workspace mirrors this structure so agents know where to look:

```text
<private workspace>/            # NOT in this repo
├── requests/REQ-YYYY-NNN/      # charter, handoffs, logs, QA report, approvals
├── context/                    # internal briefing material, background, glossaries
├── data/                       # approved data, by label
└── retrospectives/             # real-request retrospectives
```

Agents receive pointers to private material in their handoffs (for example, "see `context/sector-background.md` in the private workspace"), never copies pasted into public places. If a handoff points to private material and your tool is not approved for its label, stop and say so.

## How to add context

**To this public library** (public sources only):

1. Confirm the material is Public: published by its owner, openly available, and not from real work files.
2. Add an entry in the right file, following the existing format: name, publisher, what it covers, link, and any caveats. Do not add a link you have not opened.
3. For data sources, include the table, series or dataset ID if there is one.
4. Open a pull request ([process](../processes/code-change-via-pr.md)). The QA Reviewer checks links and labels; Mohsen merges.

**To the private workspace:** follow the same structure, label every file, and never move anything from there into this repo without the line-by-line check and Mohsen's approval described in the confidentiality policy.

## Rules

- No placeholders pretending to be sources. If a source is needed but not yet found, write `[UNKNOWN: source for ...]` in the request's working notes, not here.
- Record when a link was last checked if a source changes often.
- Remove or mark sources that are discontinued or archived.
