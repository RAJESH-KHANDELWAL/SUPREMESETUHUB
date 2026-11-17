# GLOBAL SOFTWARE CORE ECOSYSTEM

Provider-neutral control plane for discovering and governing software platforms across Bharat and global markets.

## Repository boundary
This package owns software-provider metadata, capability contracts, lifecycle states, policy metadata and orchestration plans. It does not execute third-party software, call provider APIs, exchange OAuth tokens, or store credentials.

## Initial provider inventory
Adobe, Apple, AWS, GitHub, Atlassian and Microsoft are the initial repository-aligned provider families. This inventory is intentionally non-exhaustive.

## Layout
- `contracts.py`: stable provider and capability contracts
- `catalog.py`: provider registry and discovery
- `policy.py`: scope, security and compliance gates
- `module_service.py`: provider-neutral lifecycle operations
- `orchestrator.py`: deterministic orchestration plans
- `service.py`: public facade
- `integrations/`, `services/`, `tools/`: shared extension points
- Provider directories: isolated provider metadata and adapters

## Status semantics
All entries are catalog metadata only. A provider is not connected merely because it is registered. Live connectivity, credentials, API availability and operational health must be verified independently.

## Security
Credentials must remain in an approved external secret manager. Store only secret references and least-privilege scope metadata here. Enforce tenant isolation, consent, licensing, data residency and audit requirements before any future adapter is enabled.
