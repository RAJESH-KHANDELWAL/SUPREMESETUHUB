# CORE SERVICES BOUNDARY

This directory is reserved for capability-specific Core facades. Services must remain provider-neutral and metadata/control-plane oriented.

- Read catalog and lifecycle metadata through the canonical registry.
- Validate tenant context and capability identifiers.
- Do not persist personal data, resolve secret values, call provider APIs or execute user workflows.
- Keep application authorization and user consent in the application/security boundary.

**Current status:** shared read-only facade is implemented at the ecosystem root; capability-specific services are not yet implemented.
