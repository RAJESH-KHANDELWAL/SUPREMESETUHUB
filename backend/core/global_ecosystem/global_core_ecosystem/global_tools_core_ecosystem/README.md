# GLOBAL TOOLS CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/`

## Curated inventory

- **28 provider families** represented by provider metadata facades.
- **124 curated product/tool families** in `product_ecosystem_index.json`.
- **20 responsibility domains** in `domain_catalog.py`.
- Provider families include Atlassian, Adobe, Anthropic, Apple, AWS, Cloudflare, Cohere, CrakRevenue, DeepSeek, DigitalOcean, ExoClick, GitHub, Google, Hugging Face, IBM, Meta, Microsoft, Mistral AI, NVIDIA, OpenAI, Oracle, PayPal, Salesforce, Shopify, Slack, Stripe, TrafficJunky and Twilio.

The inventory is a curated repository-aligned baseline, not an exhaustive census of every worldwide vendor, product, SKU, plan, model or API. Product entries are families for discovery, not individual deployable integrations.

## Architecture

`catalog.py` owns provider identity; `product_catalog.py` and the JSON index own product discovery; `domain_catalog.py` and `domain_runtime.py` own domain classification; `contracts.py` and `policy.py` own tenant/result contracts and metadata guardrails; `module_service.py` and `integrations/registry.py` resolve provider metadata; `orchestrator.py`, `service.py`, and `manager.py` provide discovery and the public entry point; `manager.php` is a thin metadata facade; `services/inventory_service.py`, `tools/validate_tools_catalog.py`, and `test_global_tools_core.py` support inventory and verification. Each provider family has one thin manager facade; shared logic is not duplicated.

## Layer boundaries

Core owns provider/product identity, classification, capability metadata, policy and readiness. API ecosystems own OAuth, SDK clients, HTTP transport, webhooks and response normalization. Runtime/integration layers own execution; storage/database layers own durable state and secret references. Never store tokens, passwords, API keys or client secrets here. Sensitive admin, publishing, messaging, payment, campaign-spend and destructive actions require explicit authorization and audit. Catalogue registration does not prove API availability, entitlement or live connection.

## Extension rules

Reuse existing provider ecosystems and avoid duplicate provider ownership. Catalogue-only products do not need individual directories. Add a provider only when it has a distinct vendor identity and a relevant tool/platform surface. Update provider catalog, product index, manifest, validator, tests and master implementation registry together. Keep live-connection flags false until deployment authentication and provider smoke tests pass.
