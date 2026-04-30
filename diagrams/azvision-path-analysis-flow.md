# AzVision Path Analysis Flow

Text summary: AzVision starts from a source resource, evaluates candidate topology, NSG rules, route-table next hops, protocol and port filters, then returns an allowed, blocked, or unknown verdict with supporting evidence.

```mermaid
flowchart LR
  S[Source resource] --> T[Topology candidate path]
  T --> N[Effective NSG evaluation]
  N --> R[Route table next-hop evaluation]
  R --> P[Protocol and port filters]
  P --> V[Allowed / blocked / unknown verdict]
  V --> E[Evidence stack shown to user]
```
