# Research Lane Web Setup

## 60-second summary

A secondary operator lane is more useful when it can perform independent web research without sharing runtime secrets casually. This pattern separates search and extraction backends, stores credentials outside the public repo, locks file permissions, and verifies behavior with live smoke checks before restart.

## Pattern

- Use a search backend for broad discovery.
- Use an extraction backend for page-level reading when needed.
- Keep provider credentials in a private env file or supported secret store.
- Restrict permissions on credential files.
- Smoke-test search and extraction separately.
- Make provider/backend metadata visible enough for audit, without exposing keys or quotas that should remain private.

## Why it matters

Research lanes can silently fall back to different providers, fail due to quota issues, or answer without knowing which backend was used. Operator-grade research should make the backend path observable without leaking sensitive values.

## Recommended wording

> Configured a secondary research lane with separated search/extraction backends, private credential storage, and smoke checks so web-current review could be audited without exposing provider secrets.

## Related

- [Hermes Secondary Operator Lane](hermes-secondary-operator-lane.md)
- [Security and Sanitization](security-and-sanitization.md)
