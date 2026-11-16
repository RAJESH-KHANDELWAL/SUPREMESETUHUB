# TOOLS BOUNDARY

This directory is reserved for safe discovery and administrative metadata tools exposed by Individual Core.

- Tools must be read-only by default and tenant-scoped where user context is involved.
- Destructive, financial, identity, health and age-restricted actions require explicit application authorization and audit.
- Do not expose provider credentials, personal records or secret material.
- Runtime execution belongs to the Engine/API layers, not this Core catalog.

**Current status:** reserved boundary; no live execution tools are registered.
