# AI agent team playbook: how to make AI agents work together

By Authority Brand Builder, James Brinkerhoff and Sonia Gomez ([authoritybrandbuilder.com](https://authoritybrandbuilder.com)).

This is the operating manual we use to run a small business with a team of AI agents. Each agent has one job. They share a computer, a task board, and a written memory. A human approves anything that leaves the building. You can copy the whole system with the templates in this repo.

## How do I make AI agents work together?

Give each agent one job, write that job down, and give every agent the same place to read and write shared memory. In practice that means five things:

1. **One role per agent.** Each agent has a written role file that says what it owns, what it does not own, and which agent owns that instead. See [roles](docs/roles.md).
2. **A routing map.** One table that says who owns each kind of work. When work lands on the wrong agent, it hands it to the owner instead of doing it. See [routing](docs/routing.md).
3. **A documentation standard.** Every agent keeps a role file and a dated work log in the same format, in a shared Git repo. Another agent can read the folder and run the role. See [documentation standard](docs/documentation-standard.md).
4. **Approval gates.** Agents draft. A human sends, publishes, and spends. See [approval gates](docs/approval-gates.md).
5. **A coordinator agent.** One agent turns everyone's reports into a short weekly brief for the owner, chases blocked work, and keeps the docs current. See [handoffs](docs/handoffs.md).

Then add a shared model router so each kind of task goes to the right AI model at the right cost. See [model routing](docs/model-routing.md).

## What is in this repo?

| Page | What it answers |
|---|---|
| [Roles](docs/roles.md) | How do I split work between AI agents? |
| [Routing](docs/routing.md) | How do agents know who owns what? |
| [Documentation standard](docs/documentation-standard.md) | How should agents document their work so another agent can take over? |
| [Handoffs](docs/handoffs.md) | How do agents pass work to each other? |
| [Approval gates](docs/approval-gates.md) | How do I stop agents from sending or spending without me? |
| [Model routing](docs/model-routing.md) | Which AI model should each agent use? |
| [Lessons learned](docs/lessons-learned.md) | What went wrong and what we changed |
| [FAQ](docs/faq.md) | Short answers to common questions |
| [Templates](templates/) | ROLE.md, LOG.md, handoff message, weekly review |

## Who is this for?

Owners and operators who already use AI agents from more than one company (for example Claude, ChatGPT and Grok) and want them to act like a team instead of separate chat windows. It is also written so AI assistants can read it and set up the same system for you. Point your agent at [llms.txt](llms.txt).

## How do I start in one afternoon?

1. List the jobs in your business that repeat every week.
2. Give each job to one agent. Write its `ROLE.md` from [the template](templates/ROLE.md).
3. Make one coordinator agent. It reads everyone's logs and writes your weekly brief.
4. Create a private Git repo with an `agents/` folder. Each agent gets `agents/<name>/ROLE.md` and `agents/<name>/LOG.md`.
5. Write one rule every agent follows: draft only, a human approves anything that is sent, published, or paid for.
6. Add a shared task board file that every agent reads at the start of each run.
7. Once a week, have the coordinator review the logs, update the role files, and tell you only what changed.

## Who wrote this?

Authority Brand Builder, James Brinkerhoff and Sonia Gomez. Sonia leads story, speaking and sales. James builds the systems and the agent team. This playbook comes from running that team every day, and we update it as we learn.

## How is this kept up to date?

Our coordinator agent reviews every agent's work log each week. When a lesson applies outside our business, it is rewritten without client details and added to [lessons learned](docs/lessons-learned.md).
