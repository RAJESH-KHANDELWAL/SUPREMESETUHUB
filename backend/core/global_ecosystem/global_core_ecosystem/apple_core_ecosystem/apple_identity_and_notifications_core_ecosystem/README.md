# IDENTITY AND NOTIFICATIONS

**Apple Core domain ID:** `IDENTITY_AND_NOTIFICATIONS`  
**Shared runtime:** `../domain_runtime.py`

Sign in with Apple identity metadata and APNs notification classification.

This package exposes a domain-scoped, read-only view of the canonical Apple offering inventory.

- `manager.py` provides the domain manager and discovery methods.
- `__init__.py` exports the stable package interface.
- Product-specific implementation remains in the existing `apple_*_core_ecosystem/` packages.
- Apple API transport, authorization, persistence, background jobs and UI remain owned by their dedicated layers.

A listed offering or capability does not imply account entitlement, authorization, API availability or a live Apple connection.
