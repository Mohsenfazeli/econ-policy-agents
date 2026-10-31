# Adapters: running the team in different tools

The files in this repo are the canonical definitions. They do not depend on any one product. This page shows how to load them into common tools. Tool features change often, so check each tool's current documentation before relying on the details below.

Today the team runs as Grok Bot assistants, one assistant per role. Nothing in the repo assumes that.

## What every adapter needs

For each role, an adapter needs three things:

1. **The system prompt**: the body of `agents/<role>/system-prompt.md` (everything after the frontmatter).
2. **A short description** for routing: the `description` field in the same file's frontmatter.
3. **The skills that role uses**: listed in [`org/team.yaml`](../org/team.yaml). Either load the `SKILL.md` files as skills, or paste the relevant ones into the assistant's knowledge or instructions.

Also give every assistant the shared rules: [`org/governance.md`](../org/governance.md), [`org/communication-protocol.md`](../org/communication-protocol.md) and [`library/style-guide.md`](../library/style-guide.md).

## Chat assistants (one assistant per role)

This is the simplest set-up and the one in use today.

1. Create one assistant per role, named exactly as in `org/team.yaml` (for example, "QA Reviewer").
2. Paste the system prompt body into the assistant's instructions.
3. Attach the role's skills and the shared rules as knowledge files, if the tool supports it; otherwise paste the short versions.
4. Mohsen acts as the message bus: he gives the request to the Lead PM, then passes each handoff message to the named specialist and the reply back to the Lead PM.
5. Never attach private or confidential material to an assistant unless the tool is approved for that material (see [`org/confidentiality-and-data-handling.md`](../org/confidentiality-and-data-handling.md)).

## Claude Code subagents

[Claude Code subagents](https://code.claude.com/docs/en/sub-agents) are Markdown files in `.claude/agents/` with `name` and `description` frontmatter, followed by the system prompt.

1. Copy `agents/<role>/system-prompt.md` to `.claude/agents/<role>.md` in a private working repo.
2. Keep `name` and `description`. Replace `tools-guidance` with a `tools` list that matches the role card's limits (for example, the QA Reviewer gets read-only tools).
3. Copy the skills folders into the location your Claude Code version reads skills from (see [Claude Code skills](https://code.claude.com/docs/en/skills)).

## CrewAI

[CrewAI agents](https://docs.crewai.com/en/concepts/agents) take `role`, `goal` and `backstory`. Map them like this:

| CrewAI field | Source in this repo |
| --- | --- |
| `role` | `display_name` in `org/team.yaml` |
| `goal` | `purpose` in `org/team.yaml` |
| `backstory` | System prompt body |
| `allow_delegation` | `true` for Lead PM only |
| Task `expected_output` | The skill's "Outputs" and "Done when" sections |
| Task `human_input` | `true` for any task that ends at the approval gate |

Use the [hierarchical process](https://docs.crewai.com/en/learn/hierarchical-process) with the Lead PM as `manager_agent`.

## AutoGen AgentChat

In AutoGen AgentChat, each role becomes an assistant agent whose system message is the prompt body. Use a [selector group chat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html) with a custom selector function that always routes through the Lead PM, and add a user proxy for Mohsen's approvals ([human-in-the-loop](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html)).

## LangChain / LangGraph

Use the [subagents pattern](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents): the Lead PM is the main agent, and each specialist is wrapped as a tool whose description comes from `org/team.yaml`. Use [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) to pause at the QA and approval gates.

## Keeping adapters in sync

Adapters are copies. When a role or skill changes here, regenerate the adapter files. Do not edit prompts inside a tool and leave this repo out of date; change the repo first, through a pull request.
