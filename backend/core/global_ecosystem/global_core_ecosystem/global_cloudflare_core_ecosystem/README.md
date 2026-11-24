# Global Cloudflare Core Ecosystem

A read-only control plane for Cloudflare product metadata and domain routing.

## Responsibilities
- Maintain a single product inventory with explicit domain ownership.
- Expose product lookup, domain inventory, health, dependency metadata and a directory audit.
- Read the existing backend master catalog (target 2468) without copying or changing it.
- Provide a PHP interoperability facade while Python remains the canonical manager.

## Safety and implementation status
Existing product directories are placeholders, not deployed adapters. No Cloudflare API calls, credentials, provisioning, DNS changes, traffic changes, billing actions or persistence are performed by this Core layer. External or unverified directories are retained in the audit but excluded from the Cloudflare product registry.
