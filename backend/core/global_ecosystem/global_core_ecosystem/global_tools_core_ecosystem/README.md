# GLOBAL TOOLS CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/`

## Curated baseline

- 11 provider families: Atlassian, Amazon Web Services, CrakRevenue, ExoClick, GitHub, Google, Microsoft, OpenAI, Salesforce, TrafficJunky, Twilio.
- 56 curated product/tool families in `product_ecosystem_index.json`.
- 20 responsibility domains in `domain_catalog.py`.

This is a curated baseline, not an exhaustive list of every worldwide vendor, product, SKU, plan or API. Expand only with distinct, verified offerings.

## Architecture

`catalog.py` owns provider identity; `product_catalog.py` and the JSON index own product discovery; `domain_catalog.py` and `domain_runtime.py` own domain classification; `contracts.py` and `policy.py` own tenant/result contracts and metadata guardrails; `module_service.py` and `integrations/registry.py` resolve provider metadata; `orchestrator.py`, `service.py`, and `manager.py` provide discovery and the public entry point; `manager.php` is a thin metadata facade; `services/inventory_service.py`, `tools/validate_tools_catalog.py`, and `test_global_tools_core.py` support inventory and verification. Each existing provider folder receives a provider-specific manager; common logic is not duplicated.

## Layer boundaries

Core owns provider/product identity, classification, capability metadata, policy and readiness. API ecosystems own OAuth, SDK clients, HTTP transport, webhooks and response normalization. Runtime/integration layers own execution; storage/database layers own durable state and secret references. Never store tokens, passwords, API keys or client secrets here. Sensitive admin, publishing, messaging, payment, campaign-spend and destructive actions require explicit authorization and audit. Catalogue registration does not prove API availability, entitlement or live connection.

## Extension rules

Reuse existing provider folders. Catalogue-only products do not need individual directories. Add providers/domains only for distinct ownership/responsibility. Update index, manifest, validator, tests and master registry together. Keep live-connection flags false until deployment authentication and provider smoke tests pass.
