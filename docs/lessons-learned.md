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
