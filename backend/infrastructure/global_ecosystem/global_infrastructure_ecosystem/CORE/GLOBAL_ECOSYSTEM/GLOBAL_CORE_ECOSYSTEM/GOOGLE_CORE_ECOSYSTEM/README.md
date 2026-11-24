# GOOGLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`

## Mission

Google Core is the provider-level control plane and canonical capability inventory for Google product families. It coordinates:
- provider and product identity, registration and lifecycle;
- product-family and cross-product domain classification;
- capability metadata, tenant context and policy boundaries;
- product discovery, dependency mapping, readiness and health;
- boundaries to Google API, Storage, Database, Runtime/Engine and Application layers;
- language-neutral result contracts for Python and PHP consumers.

## Coverage model
The runtime catalog contains 129 Google offerings. Each offering has a dedicated product Core package with ten product-specific subfolders, product metadata, Python contracts and a PHP authentication-context contract. Existing family-level modules are retained for compatibility. Catalog entries do not imply public API availability or live integration; verify official documentation, scopes and eligibility before enabling operations.

## Core domains

- Provider Governance
- Identity, Access and Administration
- Workspace and Collaboration
- Cloud Infrastructure and Networking
- Storage, Databases and Data Platforms
- AI, Machine Learning and Intelligence
- Analytics and Observability
- Maps, Geospatial and Travel
- Developer and Application Platform
- Android and Mobile
- Security, Privacy and Compliance
- Advertising, Commerce and Monetization
- Search, Publishing and Discovery
- Media, Video and Audio
- Business, Education and Local Services
- Payments, Wallet and Subscriptions
- Consumer Devices and Smart Home
- Language, Accessibility and Productivity
- Specialty and Cross-product Services

## Layer ownership

| Layer | Owns |
|---|---|
| Google Core | Product identity, domain classification, capability policy, lifecycle, orchestration, readiness |
| Google API Ecosystem | OAuth flows, Google SDK clients, API transport, response normalization |
| Google Storage Ecosystem | Durable records, tenant isolation, retention and backups |
| Google Database Ecosystem | Database engines, schemas, queries, migrations and transactions |
| Google Runtime/Engine | Jobs, retries, queues, scheduling and execution |
| Application/UI | User sessions, consent screens, user workflows and product UI |

Core must not duplicate API clients, token exchange, persistence, queue execution or product UI.

## Python implementation

- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: tenant-context and capability metadata checks; not a substitute for OAuth or application authorization.
- `module_service.py`: reusable read-only product Core service.
- `catalog.py`: canonical 23-family Core inventory.
- `product_catalog.py`: all 129 currently registered runtime offerings with Core-family routing metadata.
- `domain_catalog.py`: 19-domain taxonomy, category assignment, inventory and coverage summary.
- `orchestrator.py`: product/domain discovery, health, offering inventory and dependency map.
- `service.py`: public ecosystem status and registry integration.

Each of the 23 product-family packages retains its dedicated `service.py` entry point.

## PHP interoperability

`php/GoogleCoreContract.php` is a PHP 8+ JSON contract validator/normalizer for PHP applications consuming Core result payloads. It performs no network I/O and does not duplicate Google APIs or OAuth.

## Security and lifecycle rules

1. Tenant and actor identity must come from the authenticated application layer.
2. Registered capabilities do not prove user authorization, Google OAuth consent, product entitlement or API availability.
3. Secrets, access tokens, refresh tokens and private keys must never be committed or exposed in status payloads.
4. Use least-privilege scopes and explicit consent; use Cloud IAM/workload identity for Cloud workloads where appropriate.
5. Destructive, administrative, publishing, billing and write capabilities require explicit authorization and audit.
6. Products without a verified API adapter remain catalog-only or eligibility-gated.
7. A live connection is reported only after deployment-level authentication and provider smoke tests succeed.

## Current implementation boundary

This package provides a catalog, taxonomy, policy metadata and orchestration foundation. It does **not** claim all Google products are integrated, every listed product has a public API, or any Google account/project is connected. API credentials and external verification are not present in this repository's Core catalog.
