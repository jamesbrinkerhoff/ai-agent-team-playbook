# How do agents know who owns what?

Keep one routing map in a shared file. Every agent reads it. When work arrives that the agent does not own, it sends the work to the owner and tells the coordinator.

## What does a routing map look like?

| Work | Owner |
|---|---|
| Ads, ad spend, tracking pixel | Media buyer |
| Pages, checkouts, forms, page integrations | Funnel builder |
| Organic content and video | Content studio |
| Event registrations, reminders, attendance, follow-ups by segment | Event operations |
| Sales call prep, proposals, pipeline cleanup | Deal desk |
| Onboarding and client deliverables | Client delivery |
| Weekly brief, cross-team priorities, docs, anything with no owner | Coordinator |

## What happens when two agents both touch the same thing?

Name one owner and one helper. For example, the funnel builder owns the page and the media buyer helps with the tracking on it. Write the split in both role files.

## Where should the routing map live?

In the shared repo, in one coordination file that every role file links to. Ours is called `HOW-WE-COORDINATE.md`. It also holds the messaging rules, the model routing rules, the approval rules, and the list of shared memory locations.

## Should agents talk to the owner directly?

Agents report to the coordinator. The coordinator is the only agent that briefs the owner on team-wide priorities. Individual agents still bring their own drafts to the owner for approval, but the owner gets one weekly brief instead of seven.
