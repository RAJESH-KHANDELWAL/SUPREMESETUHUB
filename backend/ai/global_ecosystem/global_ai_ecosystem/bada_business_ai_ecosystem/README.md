# BADA BUSINESS AI ECOSYSTEM

**Path:** `backend/ai/global_ecosystem/global_ai_ecosystem/bada_business_ai_ecosystem/`  
**Parent:** `GLOBAL AI ECOSYSTEM`  
**Layer:** AI

## Purpose

Provide AI-domain intelligence for the canonical Bada Business ecosystem:
resource understanding, program comparison, business learning, research,
resource recommendations, consent-based lead qualification and performance
analysis from supplied metrics.

## Ownership and boundaries

| Layer | Responsibility |
|---|---|
| Product resources | `backend/global_ecosystem/global_bada_business_ecosystem/` owns provider identity, official/referral URLs, programs, courses, products and events |
| AI | This package owns Bada Business-specific AI capabilities, agent profiles, evidence policies and workflow descriptions |
| CORE | Owns application/business rules, validation and business orchestration |
| ENGINE | Owns actual model/provider execution, tool dispatch and runtime lifecycle |
| API | Owns HTTP routes, authentication, request/response schemas and transport |

The AI package reads provider resources through `resource_adapter.py`; it does
not duplicate the provider's URLs, course catalog or program records. It does
not import API, CORE or ENGINE modules, initialize SDKs, read secrets, make
network requests or start autonomous workflows.

## Modules

- `catalog.py` — AI ecosystem identity and capability catalog
- `resource_adapter.py` — read-only access to the canonical provider catalog
- `agents.py` — Bada Business-specific AI agent profiles
- `workflows.py` — workflow definitions and step sequences
- `policies.py` — evidence, commercial, privacy and approval policies
- `service.py` — metadata/resource access and injected executor boundary

## Initial agents

- Bada Business Advisor
- Bada Business Program Guide
- Bada Business Learning Coach
- Bada Business Research Analyst
- Bada Business Growth Analyst
- Bada Business Resource Matcher

## Status

`AI_DOMAIN_FOUNDATION_READY` means the AI-domain structure and contracts are
defined. Runtime status remains `NOT_CONFIGURED` until a real executor is
explicitly wired through the composition root and verified with tests. This
package does not claim a Bada Business official developer API, partnership,
provider account access, live AI integration, current pricing or guaranteed
program outcomes.

## Network marketing and affiliate AI domains

The related AI-domain namespaces are organized under `network_marketing_direct_selling_business_ai_ecosystem/`, including the single YOUTAG business identity and the separate affiliate-marketing platform directory. YOUTAG owner referral metadata is maintained in the canonical GLOBAL ECOSYSTEM profile; this AI package does not duplicate or own the provider URL.
