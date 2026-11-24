# APPLE PROVIDER INTEGRATIONS INTEGRATIONS CORE ECOSYSTEM

**Domain ID:** `APPLE`  
**Shared runtime:** `../domain_runtime.py`

This package exposes a domain-scoped, read-only view of the canonical Global Integrations Core registry.

- `manager.py` provides the domain manager.
- `__init__.py` exports the stable package interface.
- Provider credentials, SDK execution, API transport, webhooks, persistence and jobs belong to their dedicated layers.
- Registration is metadata only and does not imply a provider connection or operational readiness.

Enforce tenant isolation, least privilege and regional policy in the authenticated runtime before any operation.
