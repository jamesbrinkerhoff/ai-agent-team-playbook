# How do AI agents pass work to each other?

With a short written message that a busy agent can act on without asking a question. Every handoff names the file, the ask, the deadline, and whether the owner has approved it.

## What goes in a handoff message?

```
To: <agent>
From: <agent>
Urgent: yes / no
What: one line
Where: path to the file or folder
Ask: what you want the receiver to do
Deadline: date, or "none"
Approved by owner: yes / no / not needed
```

See [the handoff template](../templates/HANDOFF.md).

## How do you mark something urgent?

Our messaging tool has a priority flag. Priority on wakes the receiving agent now. Priority off holds the message until that agent's next scheduled run. We use priority only when the receiver is blocked or the owner is waiting. Everything else waits.

## Which handoffs happen every week?

- The media buyer sends winning ad hooks to the content studio.
- Event operations sends hot leads to the deal desk and recordings to the content studio.
- The deal desk sends objections to the content studio as content ideas, and win and loss reasons to the coordinator and the media buyer.
- The deal desk sends new clients to client delivery.
- Everyone sends numbers and blockers to the coordinator.

## How do agents share a task list?

One task board file in the shared workspace. Every agent reads it at the start of each run and edits only its own rows. Status is one of todo, doing, blocked, done. A column says whether the owner needs to decide something.

## What does the coordinator send the owner?

One weekly brief. It starts with the result that matters most this week, then the next two priorities, then the decisions the owner needs to make. It skips anything that did not change.
