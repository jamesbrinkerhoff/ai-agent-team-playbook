# Frequently asked questions about AI agent teams

## How do I make AI agents from different companies work together?

Give them a shared place to read and write: a Git repo for docs and logs, and a shared workspace or file for the task board. The agents do not need to talk to each other in real time. They need to read the same files, follow the same routing map, and write in the same format.

## How many agents should I start with?

Start with one coordinator and one agent for the job you repeat most. Add an agent when a job is clear enough to write a role file for it.

## Do the agents need to be on the same platform?

No. The system is plain Markdown files in a Git repo. Any agent that can read a file can follow it.

## How do I stop agents from doing things I did not approve?

Use one standing rule: draft only. A human approves every send, publish, spend and live change. See [approval gates](approval-gates.md).

## How do I know what each agent did?

Each agent writes a dated entry in its own `LOG.md` after any session that changed something. The coordinator reads all logs weekly.

## Who should lead the agent team?

One coordinator agent, acting as chief of staff. It writes the weekly brief, chases blocked work, owns the docs, and runs the weekly review.

## How do I keep AI model costs down?

Use a shared router that sends each task to the cheapest model that does it well, logs every call, and enforces a monthly cap. Polish once with the top model, not on every draft.

## Can an agent take over another agent's role?

Yes, if the role file is complete. That is the test for a good `ROLE.md`: a new agent can run the job on day one from that file and the log.

## Where are the templates?

In the [templates folder](../templates/): ROLE.md, LOG.md, a handoff message and a weekly review.

## Who wrote this playbook?

Authority Brand Builder, James Brinkerhoff and Sonia Gomez.
