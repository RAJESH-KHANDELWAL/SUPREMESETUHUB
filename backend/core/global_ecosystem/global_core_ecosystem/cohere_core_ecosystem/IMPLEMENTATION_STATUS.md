# Cohere CORE Implementation Status

**Current declared state:** `interface_only`  
**Live provider calls:** disabled

This status describes files present in this CORE package. It does not claim that a Cohere account, API key, model entitlement or live provider connection has been configured.

## Implemented

| Area | Present implementation | Boundary |
|---|---|---|
| Capability registry | classify, command, embed, rerank, tokenize | Metadata only; each catalog mode is `contract_only` |
| Shared contracts | `CapabilityRequest`, `CoreResult` | In-memory dataclasses |
| Capability contracts | Five capability-specific request dataclasses and validators | Local input checks; no provider call |
| Shared service | Registry lookup and generic input mapping validation | Does not yet dispatch to capability validators |
| Manager | Public facade for listing and validating capabilities | Delegates to shared service |
| Policy | Blocked-operation guard | Does not replace application authorization |
| Security | Secret-field name check | Does not store, retrieve or inject secrets |
| Schema helper | Required-field/payload-shape check | Not a full provider schema |
| Lifecycle/events/models | State enum, event contract and capability descriptor | Definitions only; no worker or event bus |
| PHP | Capability and basic request-shape validator | No network I/O |
| Tests | Three unit tests for registry and shared validation | Not integration or provider smoke tests |

## Not implemented or not enabled

- Cohere HTTP/API transport or SDK adapter.
- Live classify, command, embed, rerank or tokenize operations.
- Secure credential injection, token exchange or authentication adapter.
- ENGINE execution, retries, timeouts, queues or scheduling.
- DATABASE persistence, STORAGE artifacts or migrations.
- Provider-side model discovery, billing, training, fine-tuning, deployment or deletion.
- Verified account entitlement, production readiness or live service health.

## Known implementation gap

Capability-specific `validate_request()` functions exist in the five product/capability packages, but the shared `CohereCoreService.validate()` currently checks only:
- whether the capability is registered; and
- whether `inputs` is mapping-like.

It does not route the request into the corresponding capability validator. The public manager therefore does not yet enforce all capability-specific rules.

## Required work before enabling live traffic

1. Add explicit request-to-capability dispatch in the shared service.
2. Align shared input payloads with each capability dataclass and reject malformed fields.
3. Add tests for every capability validator, unknown fields, invalid types and policy denials.
4. Implement API/ENGINE adapters in their designated layers.
5. Add secure runtime credential injection and tenant-level authorization.
6. Add integration tests, provider smoke tests, observability and deployment checks.
7. Update the manifest status only after evidence supports the change.

## Security constraints

Never commit provider secrets. Do not infer API availability or authorization from catalog registration. Destructive, administrative, billing and provider-write actions must be handled by explicitly authorized and audited workflows outside CORE.
