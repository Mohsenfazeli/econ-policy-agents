# Design rationale

This note explains how the repo is structured and why. It summarizes what common practice looked like when the repo was built (October 2026), what was adopted, what was adapted, and what was left out. Every source below is a public page that was checked when this note was written.

## The short version

| Decision | Borrowed from | Why |
| --- | --- | --- |
| A root `AGENTS.md` that tells any coding agent how to work in this repo | AGENTS.md open format | One predictable file that many tools read, with no vendor lock-in |
| One folder per agent, with a role card and a separate, ready-to-paste system prompt | Claude Code subagents, CrewAI role/goal/backstory | Keeps the human-readable job description apart from the machine-facing prompt |
| Skills as `skills/<name>/SKILL.md` with `name` and `description` frontmatter | Agent Skills specification | Portable, loads only when needed, reusable across roles |
| A single team registry in `org/team.yaml` | CrewAI YAML config, LangChain subagent descriptions | One source of truth for role names, so files stay consistent |
| A manager (Lead PM) that routes work to only the specialists needed | CrewAI hierarchical process, LangChain subagents pattern, Anthropic orchestrator-workers | Matches how a real team lead staffs a file; avoids every agent talking to every other agent |
| Structured handoff messages with explicit context | LangChain handoffs guidance, OpenAI agent guide | Handoffs are where context is lost; a fixed format reduces that |
| An independent QA Reviewer gate and a human final approver | Anthropic evaluator-optimizer, AutoGen human-in-the-loop, CrewAI `human_input` | Generated work needs a separate check, and accountability stays with a person |
| A RACI matrix with exactly one Accountable per activity | PMI RACI guidance | Removes "nobody owns it" and "everybody owns it" failure modes |
| A Definition of Done for every deliverable type | Scrum Guide 2020 | Makes "finished" a checklist, not a feeling |
| Risk log, escalation triggers, least-privilege tools | NIST AI RMF and Generative AI Profile, OWASP Top 10 for LLM Applications, OpenAI agent guide | Agentic systems fail in known ways: invented content, prompt injection, too much autonomy |
| Confidentiality and AI-use rules aligned with Canadian public-sector guidance | BC gen AI policy, Government of Canada generative AI guide | The owner works in the BC public service; the team's rules should be at least as strict |
| Blameless retrospectives | Google SRE book | Lessons get recorded only if people (and agents) are not blamed for surfacing them |
| `CHANGELOG.md` and semantic versions | Keep a Changelog, Semantic Versioning | Changes to prompts and rules are traceable |

## 1. Repo-level agent instructions: AGENTS.md

[AGENTS.md](https://agents.md/) is an open, plain-Markdown format described as "a README for agents": a predictable place for the build steps, conventions and constraints a coding agent needs. It has no required fields, supports nested files (the closest file wins), and is read by many tools. It is now stewarded under the Linux Foundation's Agentic AI Foundation ([agents.md](https://agents.md/), [GitHub repo](https://github.com/agentsmd/agents.md)).

**Adopted.** The root [`AGENTS.md`](../AGENTS.md) tells any agent that edits this repo the non-negotiable rules, the role names it must use, and the checks to run. It is deliberately short and points to `org/` for detail.

## 2. Agent definitions: role card plus system prompt

[Claude Code subagents](https://code.claude.com/docs/en/sub-agents) are Markdown files with YAML frontmatter (`name`, `description`, optional `tools`, `model`) followed by the system prompt. They live in `.claude/agents/` (project) or `~/.claude/agents/` (user). The documentation stresses a focused `description` (it drives delegation) and restricting tools per subagent.

[CrewAI agents](https://docs.crewai.com/en/concepts/agents) are defined by `role`, `goal` and `backstory`, with options such as `allow_delegation` (off by default). Tasks carry a `description` and an `expected_output` ([CrewAI tasks](https://docs.crewai.com/en/concepts/tasks)).

**Adopted, in a tool-agnostic form.** Each `agents/<role>/` folder has:

- `role-card.md`: for humans. Purpose, responsibilities, inputs and outputs, handoffs, quality bar, and "must never" rules. This is the equivalent of a job description.
- `system-prompt.md`: for machines. Frontmatter (`name`, `description`, `tools-guidance`) and a prompt body that can be pasted into any assistant, or dropped into `.claude/agents/` with minor edits (see [adapters](adapters.md)).

Splitting the two keeps the prompt short (a prompt is not the place for a full job description) while keeping the job description reviewable.

**Not adopted.** Vendor-specific fields (model names, tool allowlists in a particular syntax) are not in the canonical files. They belong in the adapter layer for each tool, because tools and models change faster than roles do.

## 3. Reusable procedures: Agent Skills

The [Agent Skills specification](https://agentskills.io/specification) defines a skill as a folder containing `SKILL.md` with YAML frontmatter. `name` (lowercase, hyphens, must match the folder) and `description` (what it does and when to use it) are required. The body holds step-by-step instructions. Optional `scripts/`, `references/` and `assets/` folders hold extra material. Skills use "progressive disclosure": only the name and description load at start-up, the body loads when the skill is triggered, and other files load only if needed. The spec recommends keeping `SKILL.md` under 500 lines.

Anthropic's [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), the [engineering post introducing skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) and the public [anthropics/skills](https://github.com/anthropics/skills) repo follow the same structure. [Claude Code skills](https://code.claude.com/docs/en/skills) use the same `SKILL.md` format.

**Adopted.** Every skill in [`skills/`](../skills/) follows the spec: folder name equals `name`, a description that says *when* to use it, numbered steps, defined outputs, and a "done when" checklist. A small `metadata` block records which roles own and use the skill. The check script validates the frontmatter.

**Why skills and roles are separate.** A role is *who* is accountable; a skill is *how* a task is done. Several roles use the same skill (for example, the Econometrician and the Applied Economist both use forecasting). Keeping methods in skills avoids copying the same procedure into several prompts and letting them drift apart. LangChain lists "skills" as its own multi-agent pattern for the same reason ([LangChain multi-agent overview](https://docs.langchain.com/oss/python/langchain/multi-agent)).

## 4. Coordination pattern: a lead that routes, not a group chat

Common patterns in current frameworks:

- **Manager or supervisor.** CrewAI's [hierarchical process](https://docs.crewai.com/en/learn/hierarchical-process) uses a manager agent that allocates tasks by role and validates outcomes ([processes](https://docs.crewai.com/en/concepts/processes)). LangChain's [subagents pattern](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents) has a main agent call specialists as tools; specialists return results to the main agent, not to the user, and each works in a clean context.
- **Handoffs.** LangChain's [handoffs guidance](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs) warns that you must decide exactly what context passes between agents, or downstream agents receive malformed or bloated history.
- **Group chat with a selector.** AutoGen AgentChat [teams](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html) include round-robin and [selector group chat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html), where a model picks the next speaker from participant descriptions.
- **Workflows first.** Anthropic's [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) separates fixed *workflows* (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) from open-ended *agents*, and advises starting with the simplest pattern that works and adding complexity only when it clearly helps.

**Adopted.** The Lead PM is the single router (orchestrator-workers). It picks only the specialists a request needs, writes a handoff for each, and assembles the result. Specialists report back to the Lead PM, not to Mohsen directly, except for escalations. The standard pipelines in [`processes/`](../processes/) are fixed workflows with known stages; the Lead PM uses judgment only when choosing which stages a request needs.

**Not adopted.** Free-form group chat as the default. With 11 roles, letting any agent speak next makes it hard to see who owns what and adds cost. Agents can still consult each other, but through a logged handoff, not an open thread.

## 5. Quality gates and human approval

- Anthropic's **evaluator-optimizer** pattern pairs a generator with a separate evaluator that gives feedback in a loop; it works best when evaluation criteria are clear ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)).
- AutoGen's [human-in-the-loop guide](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html) shows a user proxy that blocks until a person approves, recommended for short approve or reject decisions. LangGraph supports pausing a graph for human input with [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts). CrewAI tasks have a `human_input` flag for human review of a final answer ([CrewAI tasks](https://docs.crewai.com/en/concepts/tasks)).
- OpenAI's [practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) recommends layered guardrails, rating tools by risk (read-only or write, reversible or not), and human intervention on two triggers: repeated failure, and high-risk or irreversible actions.

**Adopted.** Three gates, described in [`org/governance.md`](../org/governance.md):

1. **Scope gate.** Mohsen confirms the project charter for anything beyond a small request.
2. **QA gate.** The QA Reviewer checks every deliverable against a written checklist and gives an explicit pass or fail, with severity and a suggested fix for each issue. The author cannot be the reviewer.
3. **Approval gate.** Nothing is sent, published, merged or deployed without Mohsen's explicit approval. Any irreversible action needs approval first, whatever stage the work is at.

Escalation triggers follow the OpenAI guide's logic: two failed attempts at the same step, any confidentiality doubt, any irreversible action, or any disagreement the Lead PM cannot resolve.

## 6. Decision rights: RACI

PMI describes RACI as assigning Responsible, Accountable, Consulted and Informed for each task or decision, with one rule that "carries the whole model": exactly one Accountable per outcome ([PMI on stakeholder management and RACI](https://www.pmi.org/blog/stakeholder-management-raci)).

**Adopted.** [`org/decision-rights-raci.md`](../org/decision-rights-raci.md) has one Accountable per activity. Mohsen is Accountable for every external release; the Lead PM is Accountable for planning and assembly; each specialist is Accountable for the technical soundness of its own work product; the QA Reviewer is Accountable for the pass or fail verdict. Agents cannot be Accountable for anything that leaves the team.

## 7. Definition of Done

The [Scrum Guide](https://scrumguides.org/scrum-guide.html) defines the Definition of Done as a formal description of the quality an increment must meet; work that does not meet it cannot be released.

**Adopted.** Each skill ends with "Done when" criteria, and [`org/operating-principles.md`](../org/operating-principles.md) sets a team-wide minimum (sources cited, assumptions logged, QA passed, Mohsen approved). Not adopted: sprints and Scrum events. Requests here vary too much in size for a fixed cadence.

## 8. Risk, security and the limits of autonomy

- The [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) organizes AI risk work into Govern, Map, Measure and Manage. Its [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1) lists risks specific to generative AI, including confabulation (confident, false content) and information security.
- The [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) ranks [prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) first and lists [excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) (too much functionality, permission or autonomy, including from a compromised peer agent) as a top risk.

**Adopted.**

- A [risk log template](../templates/risk-log.md) and a standing team risk register in [`org/governance.md`](../org/governance.md), using the NIST functions as a light structure rather than a compliance exercise.
- Least privilege: each role card states what the agent may and may not touch. Only the Automation Engineer writes code, and only on branches.
- Content fetched from the web or from documents is treated as data, not instructions. Agents do not follow instructions embedded in sources they read.

## 9. Confidentiality and AI use in the Canadian public sector

- The BC government's [Policy on the use of generative AI](https://digital.gov.bc.ca/ai/gen-ai-policy/) requires employees to protect sensitive information (no confidential or personal information in publicly available gen AI tools), review outputs for accuracy, completeness and currency, and edit for government style. Its guidance on [reviewing gen AI outputs](https://digital.gov.bc.ca/ai/outputs/) lists what to fact-check (names, dates, numbers, references to laws, quotes and citations) and warns that links may be outdated or lead nowhere. The [draft responsible use principles](https://digital.gov.bc.ca/ai/draft-responsible-use-principles/) start with transparency.
- The Government of Canada [Guide on the use of generative AI](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html) sets out the FASTER principles (Fair, Accountable, Secure, Transparent, Educated, Relevant). The [Directive on Automated Decision-Making](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592) covers systems that assist or replace human judgment in administrative decisions.

**Adopted.** [`org/confidentiality-and-data-handling.md`](../org/confidentiality-and-data-handling.md) and [`org/ai-use-policy.md`](../org/ai-use-policy.md) apply these ideas as team rules: public repo holds public material only; work data never goes into tools that are not approved for it; every figure, date, name and citation is checked against the source; AI assistance is disclosed to Mohsen. The team does not make or automate administrative decisions about people; it supports analysis that a person reviews and owns. Where the owner's employer has stricter rules, the employer's rules win.

## 10. Learning loop and change control

- Google's SRE book describes [blameless postmortems](https://sre.google/sre-book/postmortem-culture/): written records of what happened, impact, root causes and follow-up actions, focused on fixing systems rather than blaming people.
- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [Semantic Versioning](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) are widely used conventions for recording changes.
- GitHub [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) can require reviews before merging.

**Adopted.** [`processes/retrospective.md`](../processes/retrospective.md) is blameless and ends with concrete changes to prompts, skills or templates. Every change to the operating system goes through a pull request, is recorded in [`CHANGELOG.md`](../CHANGELOG.md), and is merged by Mohsen. Recommending branch protection on `main` is listed as a setup step in the README.

## What was deliberately left out

- **Framework code.** The repo contains no CrewAI, AutoGen or LangGraph application. Those frameworks change quickly, and the value here is the operating model, not one implementation. [`docs/adapters.md`](adapters.md) shows how the files map onto each tool.
- **Agent memory or vector stores.** Context lives in `library/` as readable files. Private context lives outside this repo.
- **Autonomous publishing or deployment.** No agent has authority to release anything.
- **Personas with invented backstories.** CrewAI encourages a `backstory`; here, each role states its working standards instead. Invented biographies add nothing to quality and conflict with the no-fabrication rule.
