# GLOBAL CLOUDFLARE CORE ECOSYSTEM

**Ecosystem ID:** `GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM`  
**Parent:** `GLOBAL-CORE-ECOSYSTEM`  
**Runtime source of record:** `backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py`

## Purpose

This package is the provider-level Core control plane for Cloudflare. It owns Cloudflare identity metadata, product discovery, capability declarations, lifecycle/readiness metadata and policy boundaries.

It follows the product-package model documented by `google_core_ecosystem/PRODUCT_ECOSYSTEM_STANDARD.md`: one provider Core registry, one manifest-backed package per canonical product, ten responsibility folders per product, and explicit separation of Core from API, storage, database, runtime and application layers.

## Canonical products

The runtime Cloudflare catalog currently defines ten products: DNS, CDN, Workers, Pages, R2, Workers KV, D1, Zero Trust, Web Application Firewall and Cloudflare API. The Core product index is derived from that catalog; it is not a second provider source of truth.

## Layer ownership

- **CORE (this package):** provider/product identity, capability metadata, lifecycle contracts, readiness, policy and safe summaries.
- **API:** Cloudflare REST transport, token injection, request/response handling and provider-specific service adapters. Existing source: `backend/global_ecosystem/global_cloudflare_ecosystem/client.py`.
- **ENGINE:** orchestration, jobs and workflows.
- **DATABASE:** durable records and migrations.
- **STORAGE:** object/file asset persistence.
- **SECURITY / IDENTITY:** authorization, tenant identity, secret management and audit policy.
- **APPLICATION:** user sessions, consent and UI.

Do not duplicate the Cloudflare HTTP client or store API tokens in Core.

## Safety and status

The runtime catalog currently marks Cloudflare as `catalog_only` and `live_connection_verified=False`. Core status is therefore catalog-only. The presence of a product folder or API adapter source does not prove an authenticated account connection or production readiness.

No live API calls, zone/DNS mutations, deployments, resource provisioning or persistence are performed by this Core package.
