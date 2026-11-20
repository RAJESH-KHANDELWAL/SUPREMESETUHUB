# Communication Core Architecture

```text
GLOBAL CORE ECOSYSTEM
  └── GLOBAL COMMUNICATION CORE ECOSYSTEM
      ├── Provider inventory and classification
      ├── Domain taxonomy
      ├── Orchestrator (read-only)
      ├── Service health/status
      ├── Policy boundaries
      └── PHP interoperability facade
```

The package references the master catalog read-only. Provider adapters are a future integration boundary, not implied by directory names. Provider-specific implementation requires a documented API contract, tenant-scoped authorization, external secret references, privacy/retention controls, audit events and tests.

Sensitive operations such as sending messages, exporting contacts, placing calls or moderating content require explicit authorization. Restricted services require age, consent, legal and trust/safety review.
