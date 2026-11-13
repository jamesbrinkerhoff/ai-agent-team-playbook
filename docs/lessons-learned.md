# What have we learned running an AI agent team?

These come from our weekly team reviews. Each one changed how the agents work.

## Results move the goal, builds do not

Agents are good at building. A week can fill up with research, pages and plans while nothing reaches a customer. Every week now names one revenue action (calls booked, follow-ups sent) ahead of new builds, and the weekly brief leads with it.

## Lock the target customer before building assets

When the target customer changed several times in one week, assets built earlier no longer matched. Now every draft gets a one-line check against the current customer rules before it goes to the owner. When a rule changes, each agent lists the assets it owns that now conflict.

## Trust the payment system over the ad platform

The ad platform reported zero purchases on a campaign that had made real sales. Reading the payment gateway directly showed the truth. Revenue numbers now come from the payment system and the CRM, not the ad dashboard.

## Web research is a guess until a sales call confirms it

Agents can produce convincing research from public sources. We label it as a hypothesis, test it with ads and calls, and log what customers actually said after each call.

## Have agents check each other

One agent reviewing another's research caught that the main conclusions rested on web sources, not our own calls. Cross-checks between roles are now part of the routine.

## Every plan needs a named owner for the manual steps

Some tools cannot be fully driven by an API. Any plan that needs clicks in a web app now names who does them.

## Draft only works

Every send, publish and spend goes through the owner. We had one slip: a browser helper clicked Publish when it meant Discard and pushed unsaved edits live. Now any helper driving a web app has to name the exact button before it clicks anything that publishes, sends or deletes.

## Polish once, at the end

See [model routing](model-routing.md). Repeated top-model polishing was most of our model spend.

## Watch for planning notes saved as drafts

If a model hits its output limit mid-thought, make the tooling fail loudly instead of saving partial reasoning.

## One log name per agent

Agents logging under several names made per-agent cost reports useless until we fixed it.

## Done means checked live

A fix reported as done was still wrong a day later. The platform had not kept the first save, and nobody looked again. Now, after any change to a live page, email, workflow or tool, the agent fetches the live version and checks it before it reports. The report says what was fetched, when, and what it showed. A teammate's "done" counts as a claim until someone re-checks it.

## One rule change, one sweep

When the owner changed a rule several times in one week, each change caused a round of cleanup, and one set of changes took three passes. Now one agent leads the sweep. It lists every old phrase, name and synonym, searches every working file for each one, and checks any relayed decision against the owner's own words before editing. Any brief that carries a fact like a price names the line in the main business file it came from.

## A success code does not mean the output is complete

Our router reported success on drafts that the model had cut off at the token limit. About twenty calls in one week stopped at exactly a round limit, so some outputs were likely incomplete and nobody noticed. The fix we proposed is to treat a cut-off answer as a failure and log why each call stopped. Until then, check the end of every long output and count the items you asked for.

## Check names and figures against the original recording

An older transcript heard a client's result wrong, and our files spelled a client's name wrong. Going back to the raw audio and to the person's own introduction in the video fixed both. Quotes, figures and names now come from the original recording, not from a summary of it.

## Back up before every edit

Two older documents were rewritten when they should have been left alone. Both came back from the dated backup copies the agent made before editing. Every agent makes a dated backup before it changes a file, and asks before it edits history documents.

## Give each shared file one owner at a time

Two agent runs edited the same deploy files at once and almost broke a live page. Now one run owns a file while it works. The agent re-reads the file right before it writes and edits by anchor, so it never overwrites someone else's change.

## Ask every agent for one improvement a week

Some agents logged good lessons but proposed no changes. Now each agent files at least one proposal backed by evidence each week, or says plainly why it has none.


## Write the lesson when the job ends, not on Friday

In one week several agents did a lot of real work but wrote no learning notes. The weekly review had to rebuild the week from work logs, and the lessons from those days were mostly lost. One agent, the coordinator, missed its own notes two weeks running. Now every job ends with two lines in the same step: one in the work log and one learning note that says what happened, what went wrong and what to change.

## Upload and check new files before a page goes live

A page went live for about a minute with a broken image, because the new image had not been uploaded before the switch. Now, before any version with a new image, video or file goes live, the agent uploads it first and checks that its web address loads. If it does not load, the change waits.

## Pass the owner's exact approval with the change

A live change was stopped because the only message passed along from the owner was "thx". It shipped once someone found the real approval. Now any hand-off of a live change includes the owner's exact approving words, where they said them, and when. A helper without that quote prepares the change and waits.

## Check the vendor's plan before offering an option

An agent offered the owner an access option that the current software plan did not include. Before an agent offers a plan, login or integration choice, it checks that plan's limits in the vendor's own documents.

## Proposals need answers, not more proposals

Improvement proposals piled up for two weeks with no yes or no, so nothing changed. Now any proposal older than two weeks goes back to the owner in one short list, one line each, so it can be approved or turned down in a few minutes.

## Only a real customer proves the whole system

Every part of a sales funnel was tested on its own: pages, payments, emails, bookings and tracking. The parts that connect them can only be proven by one real order going all the way through. Once the build is done, that one real test comes before any new page or email.

## Cold-read scores only

Self-graded craft reviews inflate, mostly by changing which checks are N/A. Fix the N/A set first, keep it identical before and after, and record only a separate cold reader's totals.

## Inventory gate before more list-building

If handed-off names are sitting unworked for more than about two weeks, stop adding names until outreach starts. Tell the coordinator instead of padding the pile.

## Clear, save, then curl-check embeds

After pasting custom code into a page builder, clear the box, save, and fetch the public preview for the page wrapper and a known marker before reporting "saved."

## Shared blocks need a twin grep

When shared wording changes, search every live page including A/B twins for the old string and put every hit in the paste and verify loop.

## Re-hash pinned inputs at start and end

If an upstream file moves while you work, stop the ship. A pin written from a stale hash is a false green.

## Human blockers need reach-proof and a dated escalate

Confirm the ask reached the person (share plus acknowledgment). Escalate the first weekday after the ask date; do not wait for the last routine day. Calendar holds for owners stay with the coordinator after the owner's own words.

## Templated skill lines are rulings for craft

On locked template pieces, mark signature lines as rulings before craft flips. Only claims or compliance may change them.

## Log the decision the day you hear it

An answer the owner gives in one agent's chat, or on a quick-pick card, is invisible to every other agent. The agent who hears it writes a row in the shared decision log that day, with the owner's own words and the time. Without that row, other agents cannot verify the decision and will keep their confirm flags open.

## When a date moves, sweep every record

A date or offer change goes stale in plans, briefs, task blockers and scheduled drafts unless someone searches for the old value. Search every shared record for it before calling the move done.

## Fix access once instead of working around it

A spending cap on a shared model key, a token that lacks a scope, or a script that gets blocked for sending no user agent will cost several agents a workaround each run. Log the gap where the whole team can see it and get it fixed once.

## Keep confirm tags out of visible text from the first draft

Put every placeholder or "to confirm" note in a hidden comment plus the review file, never in visible page text. Visible tags block the publish at the moment the owner says go.

## Rebuild right before deploy, then check every changed line live

When the owner is still sending edits, rebuild the preview from the current file just before each deploy, then fetch the live preview and search it for every line changed in that pass.

## A triggered message reaches every path that fires the trigger

Do not write "as promised" for a promise only one path saw. When a deadline applies to one buying path only, name that path in the deadline line.

## Stamp times from the clock and name gaps precisely

Take every time in a log or file header from the system clock, never an estimate. When a transcript is missing a passage, call it a transcript gap until a second source, such as captions or the video, shows whether it was really never said.
