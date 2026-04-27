# Interview Guide

## 30-second answer

I use AI as part of a governed engineering workflow, not as unchecked automation. For my Azure network analysis work, I separated planning, implementation, review, fact-checking, and risk review, then validated the result with targeted backend tests and frontend build checks before treating it as ready.

## 2-minute answer

The most useful project example is AzVision Network Path Analysis. The challenge was that topology reachability is not enough to decide if a path is actually allowed in Azure. NSG direction, NIC and subnet NSG composition, service tags, route table next hops, and port filters all affect the answer.

I used an AI-assisted workflow to move faster, but kept the structure conservative: one orchestrator, separate review lanes, explicit validation, and no public/deploy action without approval. The result was a path-analysis hardening slice that improved verdict evidence and kept `unknown` as a valid result when data was incomplete.

## Questions to expect

### How exactly did AI help?

AI helped with planning, implementation drafts, review, and documentation. The important part is that the workflow separates generation from validation. I did not treat model output as final without review and test evidence.

### What was your role?

I owned the architecture, scope, risk boundaries, review process, and final decisions. AI lanes accelerated work and provided independent critique, but the engineering judgment stayed with me.

### Why is this relevant to cloud architecture?

Cloud architecture work often involves ambiguous data, operational risk, and cross-layer reasoning. This example shows how I approach those problems: conservative modeling, explicit evidence, and safe execution boundaries.

### What would you improve next?

I would add synthetic public demo fixtures, expand visual evidence in the UI, and validate more Azure edge cases with controlled sample exports.

## Strong phrases

- "I separate AI generation from engineering validation."
- "I prefer conservative `unknown` results over false confidence when cloud data is incomplete."
- "The goal was not full automation; the goal was governed acceleration."
- "I keep public portfolio artifacts sanitized and approval-gated."

## Phrases to avoid

- "AI built everything for me."
- "Fully automated cloud troubleshooting."
- "Enterprise-grade platform" unless the scope and production status are clearly defined.
- Any private runtime, account, hosting, or credential details.
