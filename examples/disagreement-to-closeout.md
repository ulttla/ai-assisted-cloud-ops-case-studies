# Example: Disagreement to Closeout

This is a public-safe synthetic example of how a multi-lane AI engineering workflow handles disagreement before publishing a result.

## Scenario

A portfolio page is being updated to describe a long-running AI-assisted development campaign.

## Builder proposal

> The AI system can run autonomous 12-hour development sessions and publish validated results.

## Reviewer finding

The wording is too strong. It can imply unattended production autonomy and publishing without a human approval gate.

## Fact-check / risk note

A safer claim needs to preserve three boundaries:

1. the work is supervised;
2. long efforts are split into restartable chunks;
3. publishing and deployment stay human-approved.

## Adopted wording

> Supervised AI development campaigns have been validated up to 12 hours using restartable chunks, review gates, and evidence-based closeouts.

## Validation after adoption

- Public package scan: passed.
- Link check: passed.
- Claim scan: no unsupported autonomous deployment language.
- Release status: ready for review; external publishing remains approval-gated.

## Closeout note

Reviewer disagreement was adopted. The final wording keeps the capability visible while avoiding overclaiming autonomy or approval bypass. This is the intended value of the control-plane pattern: multiple lanes can speed up work without removing engineering judgment.
