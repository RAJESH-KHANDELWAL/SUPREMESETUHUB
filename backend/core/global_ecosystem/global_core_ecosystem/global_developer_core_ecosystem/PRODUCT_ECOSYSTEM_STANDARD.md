# Product Ecosystem Standard
- One canonical Python manager per Core ecosystem; use `get_manager()` as the stable entry point.
- Keep provider/domain inventory in central catalog modules; do not duplicate registries inside every provider folder.
- Core owns identity, classification, capability metadata, policy and lifecycle coordination only.
- API owns OAuth/consent flows, SDK clients, network transport and provider request/response handling.
- Storage/database own persistence; engine/runtime owns queues, retries and execution; app/UI owns user workflows.
- Credentials are opaque external secret references only. Never commit tokens, API keys or private keys.
- A catalog entry is not proof of implementation, account entitlement, legal availability or live connectivity.
- Create provider-specific code only when a distinct responsibility is implemented and tested; no empty placeholder files.
- Master catalog module-index metadata is separate from its numbered unique-entry count.
