# GLOBAL SOCIAL MEDIA CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/`  
**Layer:** CORE

## Mission

A provider-neutral, India-first and globally extensible control plane for social-platform identity, platform-family classification, capability metadata, tenant context, policy boundaries, lifecycle state, discovery, readiness and dependency mapping.

## Inventory

- 112 provider entries are sourced from the existing Global Social Media API catalog.
- The existing Meta family package is retained as a separate family aggregator.
- 113 direct-child platform/family packages are preserved at this root.
- Existing `integrations/`, `services/` and `tools/` shared directories remain at this root.
- Every platform package follows the Google product-Core package convention: `README.md`, `__init__.py`, `contracts.py`, `ecosystem_config.py`, `ecosystem_manifest.json`, `service.py`, plus `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/` and `tests/`.

## Core responsibilities

- Canonical platform and family registration
- Platform category and capability discovery
- Tenant/actor context validation
- Metadata-only authorization classification
- Age-restriction and consent-policy flags for applicable platforms
- Lifecycle, readiness, health and dependency metadata
- Stable Python and PHP result contracts

## Layer boundaries

| Layer | Owns |
|---|---|
| Social Media Core | Platform identity, taxonomy, capability metadata, policy, lifecycle, readiness and orchestration |
| Social Media API | Provider API documentation, OAuth/API adapters, HTTP transport and response normalization |
| Social Media Engine | Scheduling, queues, retries and execution |
| Database | Structured persistence, schemas and transactions |
| Storage | Media assets, files, retention and backups |
| Application/UI | User sessions, consent, publishing workflows and user interface |

Core does not perform API calls, login, token exchange, scraping, publishing, media hosting, queue execution or persistence.

## API access and connection status

The `api_access` field is copied as a cautious discovery hint from the existing API catalog. It is not a guarantee of public availability, free access, approval, permission or regional eligibility. Every platform remains disconnected and catalog-only until a separately implemented adapter passes authorization and deployment-level smoke tests.

## Safety and governance

Age-restricted platform metadata is not age verification. Any future integration must independently enforce lawful age assurance, informed consent, privacy, rights, regional law and platform terms. This Core package does not generate, scrape, host or distribute explicit media.

## Current implementation boundary

This is a registry and control-plane foundation. It does not claim that 112 providers are integrated or that any account is connected.
