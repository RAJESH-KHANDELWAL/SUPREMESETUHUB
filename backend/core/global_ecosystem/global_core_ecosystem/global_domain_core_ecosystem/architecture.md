# Domain Core Architecture

```text
GLOBAL CORE
└── GLOBAL DOMAIN CORE
    ├── Catalog and provider identity
    ├── Domain capability categories
    ├── Provider-neutral contracts
    ├── Fail-closed policy
    ├── Read-only service facade
    └── Metadata-only orchestrator

API       -> routes, HTTP schemas, transport, endpoint adapters
ENGINE    -> runtime execution and provider workflows
DATABASE  -> domain records, DNS state, lifecycle history, audit persistence
STORAGE   -> certificate and export artifacts
IDENTITY  -> tenant identity and authentication context
SECURITY  -> authorization, secrets, consent and audit enforcement
```

Core stores no credentials and performs no external network calls. Provider-specific implementation status is always explicit and never inferred from a folder or catalog entry.
