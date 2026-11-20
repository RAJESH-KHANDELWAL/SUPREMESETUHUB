# Expanded Domain Core Architecture

```
Global Domain Core Manager
├── Legacy provider directory inventory (preserved)
├── Sector taxonomy (domain service areas)
├── Curated provider discovery registry (source-aware status)
├── Registry/Registrar and TLD governance boundary
├── DNS, security, lifecycle, TLS, discovery, marketplace, compliance sectors
└── Adapter readiness contract (catalog-only until verified)
```

Provider and sector entries are metadata; transport, credentials, persistence, execution, and live verification belong to separate layers. Avoid provider-per-folder growth: individual providers are registry records, while folders represent architecture modules.
