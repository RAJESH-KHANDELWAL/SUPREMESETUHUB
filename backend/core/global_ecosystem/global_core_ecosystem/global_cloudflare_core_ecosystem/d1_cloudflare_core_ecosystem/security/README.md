# SECURITY — Cloudflare Product Core

**Status:** scaffold documentation; no product-specific runtime implementation is enabled.

Threat model, least-privilege permission mapping, audit requirements, secret references and abuse-prevention boundaries.

## Completion gate
- Cite official Cloudflare documentation and verification date.
- Define typed contracts and validation before runtime use.
- Keep API transport and credentials outside Core.
- Add focused offline tests and security review.
- Do not claim live connectivity, entitlement or production readiness without evidence.
