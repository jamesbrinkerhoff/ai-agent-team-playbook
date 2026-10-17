# How should AI agents document their work so another agent can take over?

Each agent keeps two files in a shared Git repo: a role file that says how to do the job, and a work log that says what was done. If an agent is replaced, the new one reads both and continues.

## What is the folder layout?

```
agents/
  README.md               the documentation standard
  HOW-WE-COORDINATE.md    routing map, messaging, model routing, approvals, shared memory
  <agent>/ROLE.md         what the role is and how to run it
  <agent>/LOG.md          dated work log, newest entry on top
```

## What goes in each log entry?

```
## YYYY-MM-DD HH:MM · short title
- Did: what was done.
- Why: the request or reason.
- Files: paths created or changed.
- Approvals: what the owner approved, or "waiting on owner".
- Next: the next step and who owns it.
- Lesson: (optional) anything the team should learn from this.
```

One entry per working session that changed something. If nothing changed, write nothing.

## What should never go in the docs?

- Secrets, API keys, tokens, or passwords. Name the environment variable instead.
- Account IDs that are not needed to do the job.
- Raw call transcripts or customer personal details.
- Invented numbers. Label every estimate as an estimate.

## Who keeps the docs current?

Each agent writes its own log. The coordinator reviews all logs once a week, updates the role files when a job has changed, and pulls out lessons for the whole team.

## Why use Git instead of a chat history?

Chat history disappears, and other agents cannot read it. A Git repo has dated history, works with every AI company's tools, and any agent with read access can rebuild the context. It also shows who changed what and when.

## How do agents commit if they cannot run Git?

Ours hand the change to a cloud coding agent that writes straight to the repo. Any agent that can read files can still read the docs.
