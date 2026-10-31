# Retrospective and lessons learned

A short, blameless review after each standard request and after any incident, modelled on blameless postmortem practice ([Google SRE book](https://sre.google/sre-book/postmortem-culture/)). The aim is to improve the system (prompts, skills, templates, processes), not to assign blame to any agent or person.

**Accountable:** Mohsen · **Responsible:** Lead PM · **Consulted:** every role involved, and the QA Reviewer.

## When

- After every standard request, within a few days of approval.
- After any confidentiality incident, any critical issue found after release, or any missed deadline. These are mandatory.
- Every quarter, a short review across all requests to look for patterns.

## Inputs

- The charter, task plan, handoffs and returns.
- The QA report and issue log.
- The risk log.
- Mohsen's feedback.

## Steps

1. **Collect facts.** The Lead PM writes a timeline: what was planned, what happened, where it diverged.
2. **Ask each role** involved three questions:
   - What went well?
   - What was harder than it should have been?
   - What one change would help most next time?
3. **Review QA findings.** Group issues by type (accuracy, sources, method, confidentiality, style). Note any type that recurs across requests.
4. **Find causes, not culprits.** For each significant problem, ask why it happened until you reach something the system can change (a missing step in a skill, an unclear template field, a gap in a prompt).
5. **Agree actions.** Each action is specific, has an owner, and changes a file in this repo or a working practice. Examples: add a check to a skill's Done-when list; add a field to the handoff template; tighten a "Must never" rule.
6. **Record** the retrospective (private workspace for real requests).
7. **Implement** repo changes through a [pull request](code-change-via-pr.md), and note them in [`CHANGELOG.md`](../CHANGELOG.md).

## Retrospective record

```markdown
# Retrospective: REQ-YYYY-NNN

Date:
Participants:
Request summary:

## Timeline
- 

## What went well
- 

## What was harder than it should have been
- 

## QA findings by type
| Type | Count | Example |
| --- | --- | --- |

## Causes
- 

## Actions
| Action | Owner | File or practice changed | Due |
| --- | --- | --- | --- |

## Success measures for this request
- QA first-pass result:
- Issues found after approval:
- Time from intake to approval:
```

## Rules

- No blame. Describe what happened and what the system allowed, not who failed.
- Facts first. Do not speculate about causes without evidence.
- Every retrospective produces at least one action, even if it is "no change needed, because ...".
- Real-request retrospectives are Internal at minimum and stay out of this repo. Lessons that generalize may be added here as changes to skills, templates or processes, stated without any confidential detail.
