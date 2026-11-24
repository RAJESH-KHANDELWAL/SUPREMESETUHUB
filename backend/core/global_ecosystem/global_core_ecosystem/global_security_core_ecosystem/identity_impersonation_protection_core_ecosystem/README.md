# Identity and impersonation protection

**Domain ID:** `IDENTITY_IMPERSONATION_PROTECTION`  
**Parent ecosystem:** `GLOBAL-SECURITY-CORE-ECOSYSTEM`  
**Status:** `CORE_CATALOG_ONLY`

## Scope

Account takeover, impersonation, identity fraud and recovery safeguards.

## Package boundary

This package provides domain identity and governance metadata for discovery and catalog integration. It does not independently authenticate users, authorize actions, connect to providers, inspect workloads, store secrets, or enforce production controls. Runtime enforcement must be implemented and tested in the appropriate identity, API, application, storage, or infrastructure layer.

## Ownership and lifecycle

Keep the domain ID stable. Update this manifest and the parent catalog together when scope or metadata changes. Add implementation capabilities only with explicit contracts, tests, ownership, and security review.
