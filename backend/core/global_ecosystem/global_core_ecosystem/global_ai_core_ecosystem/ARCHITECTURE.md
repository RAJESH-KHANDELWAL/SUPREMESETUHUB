# GLOBAL AI CORE Architecture

1. Application authenticates the caller and supplies tenant/actor context.
2. CORE validates request shape, provider registration and capability metadata.
3. Provider facade resolves the canonical provider-specific CORE package.
4. API owns provider authentication, transport and endpoint normalization.
5. ENGINE owns inference, routing, retries, queues and agent runtime.
6. DATABASE/STORAGE own persistence and artifacts.
7. Application presents results.

Provider facades are thin references; they do not duplicate provider product trees, SDKs, OAuth, tokens or transport. Adjacent non-AI partner folders remain compatibility aliases routed to canonical domain CORE packages. The existing executor-injected GlobalAICoreService remains the execution boundary; the new registry services are read-only.
