# Global Communication Core Architecture

```text
GLOBAL CORE ECOSYSTEM
└── GLOBAL COMMUNICATION CORE ECOSYSTEM
    ├── Canonical catalog and provider/platform references
    ├── Domain taxonomy (28 domains)
    ├── Shared provider metadata service
    ├── Shared domain discovery runtime
    ├── Contracts (tenant, secret reference, readiness, result)
    ├── Policy (authorization, privacy, age/consent, safety)
    ├── Orchestrator and service facade
    └── PHP interoperability facade
```

## Ownership
| Layer | Owns |
|---|---|
| Communication Core | Provider identity, service discovery, taxonomy, capabilities, lifecycle and policy metadata |
| Communication API | OAuth/consent, provider SDKs, HTTP/SIP/RTC transport, request/response normalization |
| Storage | Durable connection metadata, retention and backups |
| Database | Schemas, migrations, queries and transactions |
| Runtime/Engine | Jobs, queues, retries, scheduling and execution |
| Application/UI | User sessions, consent screens and user workflows |

Python is canonical; PHP is an interoperability facade. Provider-specific packages must be responsibility-driven. Shared domain/provider logic stays centralized until a package has a distinct implementation need.

## Master catalog
The 2468-target master catalog remains the single source for numbered ecosystem topics. Communication Core is referenced in its separate `ecosystem_module_index`; module references do not increment the 2468-entry count. Core reads this catalog only.

## Security and readiness
Tenant and actor identity must come from the authenticated application layer. Sensitive operations require explicit authorization and audit. Never store tokens, API keys or private keys here. Catalog presence does not imply API availability, entitlement, authorization or a live connection. No provider network calls, delivery, telephony, video transport or persistence occur in Core.
