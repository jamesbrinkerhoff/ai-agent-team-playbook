# Which AI model should each agent use?

Route each kind of task to the cheapest model that does it well, through one shared script that every agent calls. The script logs the agent, the task, the model, the tokens and the cost of every call.

## How does a shared model router work?

Every agent calls the same command with a route name, the prompt, and its own name. The router picks the model for that route, tries backup models if the first one fails, and writes a row to a usage log. A monthly spending cap stops calls once it is reached, and only the owner can raise it.

## Which model for which job?

| Job | Model tier |
|---|---|
| Tagging, extraction, bulk summaries, transcripts | Fast low-cost models |
| Research | A strong research model |
| First drafts of copy | A mid-tier writing model |
| Strategy and analysis | A top reasoning model |
| One final polish on a finished draft | The top writing model, once |
| Code and automations | A coding model |
| Images | An image model |

Our setup drafts on a mid-tier Claude model, uses the top Claude model for strategy and one final polish, and sends legwork to low-cost models such as DeepSeek and Gemini Flash.

## Why polish only once?

Most of our model spend went to the top model polishing drafts over and over. Drafting on a mid-tier model and polishing once at the end keeps the top model for the step where it matters. Our own estimate, not yet measured, is that this cuts that cost by about half.

## What can go wrong with a router?

The one that hurt us: a model ran out of output tokens while it was still planning, and the router saved its planning notes as if they were the draft. The fix was to make the router stop with an error when that happens, and to warn whenever the output is the model's reasoning instead of an answer. Check that a draft starts with the deliverable before you polish it.

A second one: the router reported success on answers the model had cut off at the token limit. A success code is not proof the output is complete. Check the end of every long output, count the items you asked for, and treat an answer that stopped at the limit as a failure.

## How should agents log model use?

One fixed name per agent, and one name for tests. If an agent logs under two names, its costs look split and you cannot compare agents.

## How do we keep AI-sounding phrases out of the writing?

Every agent runs a cleanup pass on copy before handing it over. It removes em dashes, stock phrases like "not just X, but Y," and the words AI models overuse. If a passage is hard to follow, the agent rewrites it in plain language.
