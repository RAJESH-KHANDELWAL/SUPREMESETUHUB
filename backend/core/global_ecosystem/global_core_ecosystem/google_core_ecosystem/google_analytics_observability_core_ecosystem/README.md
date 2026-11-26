# ANALYTICS AND OBSERVABILITY

**Google Core domain ID:** `ANALYTICS_AND_OBSERVABILITY`  
**Shared runtime:** `../domain_runtime.py`

This package exposes a domain-scoped, read-only view of the canonical Google offering inventory.

- `manager.py` provides the domain manager and its discovery methods.
- `__init__.py` exports the stable package interface.
- Product-specific implementation remains in the existing `google_*_core_ecosystem/` packages.
- OAuth, API transport, persistence, background jobs and UI remain owned by their dedicated layers.

A listed offering or capability does not imply account entitlement, authorization, API availability or a live provider connection.
