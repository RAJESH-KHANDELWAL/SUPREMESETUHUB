# GLOBAL AI CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/`

## Mission
Provider-neutral control plane for AI provider identity, capabilities, tenant context, policy metadata, lifecycle, readiness, model/service/tool catalogs and cross-provider orchestration.

## Inventory
- 17 AI providers registered from the existing Global AI API catalogue.
- 17 thin provider facades, each linked to its canonical provider-specific CORE and API catalogue.
- 24 adjacent platforms retained as compatibility integrations, not AI model providers.
- 15 capability contracts, 10 service contracts, 9 tool specifications and 6 integration contracts.

## Provider CORE facades
OpenAI, Anthropic, Google, AWS, Microsoft, IBM, Meta, Apple, NVIDIA, Cohere, Mistral, DeepSeek, Hugging Face, Oracle, Adobe, Cloudflare and NSFWInfra point to their canonical CORE packages in the repository. This layer does not duplicate their product trees.

## Adjacent platforms
Hosting, content publishers, creator platforms, payment providers and advertising networks are separated from AI model providers. Their existing `*_ai_core_ecosystem` folder names are preserved as compatibility aliases and point to Hosting, Video, Platforms, Payments or Integrations CORE. They are not listed in `AI_PROVIDERS`.

## Existing execution boundary
The existing `service.py` and executor-injected `GlobalAICoreService` are preserved. It imports no API SDK, credential store or ENGINE implementation. New `ecosystem_service.py` is read-only and does not execute inference.

## Layer ownership
| Layer | Responsibility |
|---|---|
| GLOBAL AI CORE | identity, capability metadata, contracts, policy, lifecycle, readiness, orchestration |
| GLOBAL AI API | provider authentication, SDK/HTTP transport, endpoint adapters, response normalization |
| GLOBAL AI ENGINE | inference execution, routing, retries, queues, fallbacks, agent runtime |
| DATABASE / STORAGE | records, usage, prompts, datasets, files and artifacts |
| Application | sessions, consent, user workflows and UI |

Secrets never belong in CORE. Catalog registration does not prove API entitlement, model availability, user consent or live connectivity. Specialized or age-restricted services require appropriate legal, age, consent and provider-policy checks in their owning layers.
