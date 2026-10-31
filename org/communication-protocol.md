# Communication protocol

All messages between agents, and between agents and Mohsen, use the formats below. Fixed formats make handoffs complete, make status easy to scan, and leave a record.

## General rules

- **Route through the Lead PM.** Specialists send work back to the Lead PM, not to each other, unless the Lead PM sets up a direct consult. The QA Reviewer may go straight to Mohsen on QA and confidentiality matters.
- **One message, one purpose.** Do not combine a handoff with an unrelated question.
- **Start with the header.** Every message begins with the request ID, message type, sender and recipient.
- **Bottom line first.** The first line after the header says what the reader needs to know or do.
- **Link, don't paste,** for anything long or anything Internal or Confidential. Give the location in the private workspace.
- **Say what you did not do.** If a check was skipped or a source could not be found, say so.
- **Plain language.** Follow the [style guide](../library/style-guide.md).

### Request IDs

Format: `REQ-YYYY-NNN` (for example, `REQ-2026-014`). The Lead PM assigns it at intake. Sub-tasks add a suffix: `REQ-2026-014-T3`.

## Message header

```text
[REQ-2026-014-T3] HANDOFF
From: Lead PM
To: Data Engineer
Date: 2026-10-31
Label: Public | Internal | Confidential
```

## Message types

### 1. Handoff (Lead PM to specialist)

Use the full [handoff message template](../templates/handoff-message.md). Required fields:

- **Task:** one sentence, starting with a verb.
- **Why:** the question in the charter this serves.
- **Inputs:** what is attached or where to find it.
- **Expected output:** format, length, and the skill to follow.
- **Done when:** the acceptance criteria.
- **Constraints:** label, sources to use or avoid, method limits.
- **Due:** date (and time if it matters).
- **Next:** who receives the output after you.

A specialist who receives a handoff missing any required field replies with a help request asking for it, rather than guessing.

### 2. Return (specialist to Lead PM)

```text
[REQ-2026-014-T3] RETURN
From: Data Engineer
To: Lead PM

Bottom line: <one or two sentences>
Output: <what is delivered, and where>
Done-when check: <each criterion, met / not met>
Assumptions added: <IDs in the assumptions log>
Open issues: <anything unresolved, with severity>
Not done: <anything skipped, and why>
Confidence: high | medium | low, because <reason>
Suggested next step: <optional>
```

### 3. Status update

Sent by the Lead PM to Mohsen at the cadence in the charter, and whenever status changes colour.

```text
[REQ-2026-014] STATUS
From: Lead PM
To: Mohsen Fazeli

Status: green | amber | red
Since last update: <what was done>
Next: <what happens next, and by when>
Decisions needed from you: <none, or a numbered list>
Risks: <new or changed, with risk log IDs>
```

- **Green:** on track for scope, quality and date.
- **Amber:** at risk, with a plan to recover.
- **Red:** will miss scope, quality or date without a decision from Mohsen.

### 4. Help request

Use when stuck, when an input is missing, or when unsure what is being asked. Asking early is expected.

```text
[REQ-2026-014-T3] HELP
From: Econometrician
To: Lead PM

I need: <the specific thing>
Because: <what is blocked>
I have tried: <what you did>
Options I see: <a, b, c, with your preference>
Blocking: yes | no (I can continue with <X> meanwhile)
```

### 5. Escalation

Use for any [governance escalation trigger](governance.md#3-escalation). For confidentiality concerns, stop work before sending.

```text
[REQ-2026-014] ESCALATION
From: <role>
To: Lead PM (cc Mohsen Fazeli if confidentiality or irreversible action)

Issue: <one sentence>
Trigger: <which trigger>
What happened: <facts only>
Impact: <what is at risk>
Options: <numbered, with a recommendation>
Decision needed by: <date>
Work paused: yes | no
```

### 6. Disagreement

Use when you disagree with another role's method, finding or wording. Disagree about the work, with evidence.

```text
[REQ-2026-014-T5] DISAGREEMENT
From: Applied Economist
To: Lead PM
About: <output and author>

Position: <what you think, in one sentence>
Evidence: <sources, tests, reasoning>
Their position, as I understand it: <fair summary>
What would change my mind: <specific>
Proposed resolution: <a, b, or escalate>
```

How disagreements are resolved:

1. The Lead PM reads both positions and asks each side once for anything missing.
2. The Lead PM decides on matters of scope, timing and presentation. On matters of method, the accountable specialist decides, after considering the challenge, and records the decision and the rationale in the assumptions log.
3. If either side believes the decision creates a material risk of a wrong conclusion, the Lead PM escalates to Mohsen with both positions.
4. Once decided, everyone works to the decision. The disagreement stays on record, and the QA Reviewer sees it.

### 7. QA verdict

Sent by the QA Reviewer to the Lead PM (and to Mohsen with the final package). Uses the [QA checklist](../templates/qa-checklist.md).

```text
[REQ-2026-014] QA VERDICT
From: QA Reviewer
To: Lead PM, Mohsen Fazeli

Verdict: PASS | FAIL
Reviewed: <product and version>
Issues: <count by severity: critical / major / minor / note>
Must fix before release: <issue IDs>
What Mohsen should check personally: <short list>
Contributors: <roles that worked on the product>
```

## Status cadence

| Request size | Status update frequency |
| --- | --- |
| Small (no charter) | On completion only |
| Standard | At each stage change and at least every two working days |
| Urgent (due in under two working days) | At each stage change and at least daily |
