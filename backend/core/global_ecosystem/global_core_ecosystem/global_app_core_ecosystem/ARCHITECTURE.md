# GLOBAL APP CORE — ARCHITECTURE

## 1. Control-plane boundary

Global App Core is a read-only catalog and policy-metadata layer. It identifies application providers and classifies their app types, domains, capabilities and declared lifecycle state. It does not launch, install, authenticate to, call or operate third-party applications.

## 2. Source-of-truth flow

```text
backend/global_ecosystem/global_app_ecosystem/providers.py
                         |
                         v
              Global App Core catalog
              |        |          |
              v        v          v
          Provider   App types   Domain taxonomy
          identity   & platforms & maturity levels
              |
              v
       Core policy + safe snapshots
              |
              v
       API / Engine / Database / Storage
       (separate owning layers; no Core bypass)
```

## 3. Ownership contracts

- **Core:** identity, discovery, classification, policy metadata, lifecycle/readiness descriptions.
- **API:** provider-specific authentication, OAuth, secrets, SDK/HTTP transport and retries.
- **Engine:** adapters, workflow orchestration and explicit execution.
- **Database:** structured state and transactions.
- **Storage:** durable files and media.
- **UI:** user interaction, consent and presentation.

Dependencies must flow from runtime layers into Core contracts only where needed; Core must not import provider SDKs or perform network I/O.

## 4. Canonical package convention

Each provider package uses:
`authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, `tests/`.

The Google provider package is the structural reference. A folder is not considered implemented merely because it exists; it needs a documented contract and tests appropriate to its responsibility.

## 5. Readiness semantics

- `CATALOG_ONLY`: provider exists in the discovery catalog; no integration claim.
- `DOCUMENTED`: requirements and boundaries documented.
- `SCAFFOLD`: integration contract and non-operational scaffold exist.
- `CONFIGURED`: owning API/Engine layer has configuration evidence.
- `LIVE_VERIFIED`: authenticated smoke test and runtime evidence have succeeded.

Core reports the registry's evidence. It does not promote a provider to a higher state by inference.

## 6. Security

Core snapshots use an allow-list and recursive secret-key filtering. Credentials and tokens must never be returned by catalog or health endpoints. Tenant/actor context is descriptive metadata only; authorization remains with the authenticated application and owning execution layer.

## 7. Non-goals

No provider API calls, OAuth exchanges, app installation, user account mutation, messaging, payment, publishing, file persistence, adapter execution or automatic startup.
