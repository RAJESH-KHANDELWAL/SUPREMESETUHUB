# GLOBAL DOMAIN CORE ECOSYSTEM Architecture

```
GLOBAL DOMAIN CORE ECOSYSTEM
├── GLOBAL DOMAIN REGISTRY OPERATORS CORE ECOSYSTEM
├── GLOBAL ICANN IANA GOVERNANCE CORE ECOSYSTEM
├── GLOBAL GTLD REGISTRARS CORE ECOSYSTEM
├── GLOBAL CCTLD REGISTRIES CORE ECOSYSTEM
├── GLOBAL DNS AUTHORITATIVE HOSTING CORE ECOSYSTEM
├── GLOBAL DNS RECURSIVE RESOLVERS CORE ECOSYSTEM
├── GLOBAL DNSSEC CORE ECOSYSTEM
├── GLOBAL DNS SECURITY CORE ECOSYSTEM
├── GLOBAL TLS CERTIFICATE AUTHORITIES CORE ECOSYSTEM
├── GLOBAL DOMAIN MARKETPLACES CORE ECOSYSTEM
└── ... remaining catalog sectors
```

All 39 sector entries are generated from `sector_catalog.py`, registered in `catalog.py`, and exposed via manager APIs. Ecosystem display names must start with GLOBAL and end with CORE ECOSYSTEM; IDs start with GLOBAL and end with CORE-ECOSYSTEM.

Provider and sector records are metadata only. Transport, credentials, persistence, execution, and live verification remain separate layers. Provider-per-folder growth is avoided: provider identities are registry records.
