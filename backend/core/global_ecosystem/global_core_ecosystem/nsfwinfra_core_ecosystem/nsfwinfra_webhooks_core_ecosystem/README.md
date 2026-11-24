# WEBHOOKS INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_webhooks_core_ecosystem/`. ID: `NSFW-INFRA-WEBHOOKS-CORE`.

## Scope
Contracts/policy for subscriptions, event schemas, endpoints, signing refs, retries, timeouts, limits, delivery attempts, dead-letter, idempotency, ordering, SSRF validation and readiness. Delivery external.

## Capability metadata
- `SUBSCRIPTION_METADATA`
- `EVENT_REGISTRY_AND_SCHEMAS`
- `ENDPOINT_METADATA`
- `DELIVERY_CONFIGURATION`
- `SIGNING_AND_SECRET_REFERENCES`
- `RETRY_AND_BACKOFF_POLICY`
- `TIMEOUTS_AND_RATE_LIMITS`
- `DELIVERY_ATTEMPT_METADATA`
- `FAILED_DELIVERY_AND_DEAD_LETTER_REFERENCES`
- `IDEMPOTENCY`
- `ORDERING_GUARANTEE_METADATA`
- `ENDPOINT_HEALTH_METADATA`
- `SSRF_AND_ENDPOINT_VALIDATION_POLICY`
- `AUDIT_REFERENCES`
- `READINESS`

## Interface
- `manager.py`: status and capability metadata.
- `__init__.py`: public exports.

Metadata-only; no infrastructure execution, API calls, persistence or verified-live claim. Auth, secrets, transport, runtime and storage are separate layers.
