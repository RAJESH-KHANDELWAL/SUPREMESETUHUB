# GLOBAL DATABASE ECOSYSTEM

This package is the provider-adapter layer below `backend/database/global_ecosystem/`.

```text
backend/database/
└── global_ecosystem/
    └── global_database_ecosystem/
        ├── provider_base.py
        ├── registry.py
        ├── google_database_ecosystem/
        ├── aws_database_ecosystem/
        ├── microsoft_database_ecosystem/
        ├── proton_database_ecosystem/
        └── mega_database_ecosystem/
```

Each provider has its own package and implementation files. The central database remains the system of record for SUPREME-owned connection records, permissions, sync state, and audit metadata. Provider data is accessed only through official APIs or other authorized methods; provider credentials belong in secret management, never in source files or ordinary database rows.

**Scope of this change:** package layout, capability metadata, and a local registry only. `connection_status: not_configured` is intentional: these files do not claim that provider accounts are connected or that live sync is implemented. Google/AWS/Microsoft can later receive database-specific clients; Proton and MEGA are represented as privacy/storage service ecosystems, not assumed to be database engines. Add PHP only in a provider integration that actually runs in a PHP environment (for example, a WordPress plugin), rather than duplicating Python backend logic in PHP.