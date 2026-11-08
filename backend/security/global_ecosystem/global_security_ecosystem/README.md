# GLOBAL SECURITY ECOSYSTEM

Independent SECURITY domain runtime, aligned to the SERVER ecosystem's structural pattern while retaining SECURITY-only responsibilities.

## Ownership and separation

SECURITY owns security asset inventory, defensive capability catalog, provider registry, adapter contracts, authorization gate, runtime diagnostics, manager, service, and tests. It does not copy, wrap, import, or implement API transport, CORE orchestration, ENGINE execution internals, DATABASE persistence, or STORAGE backends. Existing authentication and authorization dependencies remain under `backend/security/dependencies.py`; this ecosystem does not replace them.

## Structure

- `catalog.py`: security providers and defensive capability definitions.
- `models.py`: SECURITY-owned asset and health value objects; secret-bearing metadata is rejected.
- `registry.py`: thread-safe in-process asset registry (not durable persistence).
- `provider_base.py`: explicitly injected provider adapter boundary.
- `provider_registry.py`: provider validation and registration.
- `operations.py`: defensive operation dispatch with mandatory authorization.
- `service.py` / `manager.py`: SECURITY runtime service and manager.

## Security controls and safe defaults

- No credentials, tokens, private keys, passwords, or secret values are stored in this package.
- Provider integrations are not imported or activated automatically.
- Unknown providers and capabilities are rejected.
- Provider registration is not proof of external connectivity; health is `NOT_PROBED` unless a real provider-specific probe is explicitly injected and invoked.
- No provider adapter means execution fails closed.
- An authorizer must be explicitly injected and return literal `True`; missing, false, or ambiguous authorization denies execution.
- Only catalogued `READ_ONLY` capabilities are enabled. Mutating security operations are intentionally not exposed by this initial runtime.
- Payloads are copied before dispatch. Provider handlers must not log credentials or return secret material.
- Asset metadata rejects common secret-bearing key names.
- Registries are process-local and not durable storage.

## Capability catalog

- `POSTURE.READ` — read authorized security posture/findings.
- `AUDIT.READ` — read authorized audit-event metadata.
- `POLICY.VALIDATE` — validate policy configuration without applying it.
- `PROVIDER.HEALTH` — inspect an explicitly configured provider health probe.

These are routing contracts, not claims of live integrations, compliance certification, or complete protection. Production security requires threat modelling, secure configuration, tested controls, incident response, patching, monitoring, and independent review.

## Provider catalog

Apple, AWS, Cloudflare, GitHub, Google, IBM, and Microsoft are catalog entries only. Availability and capability support must be verified against each provider's official documentation before enabling an integration.

## Tests

Run from repository root:

```bash
python -m unittest backend.security.global_ecosystem.global_security_ecosystem.test_security
```
