# Global Developer Core Architecture

```text
GLOBAL CORE ECOSYSTEM
└── GLOBAL DEVELOPER CORE ECOSYSTEM
    ├── Canonical catalog (28 module/domain references)
    ├── Product/provider inventory facade
    ├── Domain taxonomy (19 domains)
    ├── Tenant and secret-reference contracts
    ├── Policy and authorization boundaries
    ├── Shared domain runtime
    ├── Provider/module metadata service
    ├── Orchestrator and service facade
    └── PHP interoperability facade
```

## Layer ownership
| Layer | Responsibility |
|---|---|
| Core | Identity, catalog, capability metadata, policy and lifecycle |
| API | OAuth, SDKs, HTTP clients, provider transport and response normalization |
| Storage | Durable connection metadata, retention and backups |
| Database | Schemas, migrations, queries and transactions |
| Engine/runtime | Queues, retries, scheduling and execution |
| App/UI | Sessions, consent screens and user workflows |

Python is canonical; PHP is an interoperability facade. Provider directories are inventory boundaries, not proof of working adapters.

## Master catalog
The 2468-target master catalog remains the source of truth for numbered ecosystem topics. Developer Core is linked only through `ecosystem_module_index`; this metadata does not change the numbered count.

## Security
Authenticated tenant and actor context must be supplied by the application layer. Sensitive capabilities require explicit authorization and audit. Never store credential material in Core. Catalog presence does not prove provider availability or live connectivity.
