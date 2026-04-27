# ADR 0003 — Sanitized Case-Study Repository Instead of Raw Setup Dump

## Status
Accepted.

## Context
A raw personal automation setup can contain private paths, account details, runtime configuration, credentials, logs, or operational patterns. Publishing it directly can create unnecessary security and privacy risk.

## Decision
Publish a curated case-study repository first. It should document architecture, decisions, validation, and synthetic examples without raw private runtime state.

## Consequences
- Safer public release.
- Stronger hiring narrative.
- Less impressive to readers looking for a turnkey clone, but more appropriate for professional portfolio use.
