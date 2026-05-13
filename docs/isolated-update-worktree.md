# Isolated Update Worktree Pattern

## 60-second summary

When an assistant runtime has local operating patches, updating directly in the live checkout is risky. The isolated update worktree pattern preserves the current state, compares the upstream delta, applies local patches in a disposable worktree, and identifies conflicts before touching the live environment.

## Why it matters

AI operator workstations often accumulate local fixes: restart handling, channel behavior, status reporting, prompt hygiene, or tool metadata patches. A normal package update can overwrite those assumptions.

## Pattern

1. Record the current live version and git state.
2. Preserve local changes on a named branch or commit.
3. Create a disposable integration worktree from the target upstream.
4. Apply local patches there first.
5. List conflicts and behavior changes before promotion.
6. Prepare rollback anchors and smoke tests.
7. Promote only after approval and evidence.

## Public-safe evidence

A useful closeout should include:

- upstream delta size or scope, summarized without private paths;
- preserved branch or rollback anchor;
- conflict categories;
- smoke matrix;
- go/no-go recommendation.

## Recommended wording

> Used an isolated integration worktree to test assistant-runtime update conflicts before touching the live checkout, preserving local operating patches and rollback anchors.

## Related

- [Operator Resilience and Update Safety](operator-resilience-and-update-safety.md)
- [Security and Sanitization](security-and-sanitization.md)
