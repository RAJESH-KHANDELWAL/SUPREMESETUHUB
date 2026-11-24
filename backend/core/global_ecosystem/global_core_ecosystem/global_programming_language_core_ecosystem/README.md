# GLOBAL PROGRAMMING LANGUAGE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_programming_language_core_ecosystem/`  
**Reference architecture:** Google Core Ecosystem's metadata control-plane pattern.  
**Master planning reference:** `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (whole-ecosystem planning taxonomy, not implementation proof).

## Mission and coverage
A canonical read-only CORE registry for executable languages, paradigms, language families, dialects, shells, query DSLs, markup, stylesheets, serialization/configuration, build languages, hardware/shader languages, smart-contract languages, proof/verification languages, compilers/interpreters, runtimes, standards, toolchains and developer tooling.

Classifications are distinct: general-purpose executable languages; systems/embedded; scripting/shell; functional/logic; scientific/data; query/DB; markup; stylesheet; serialization/configuration; build/automation DSL; UI/template DSL; hardware-description/shader/GPU; smart contract/crypto; proof/verification; education/visual; and binary targets. Cross-domain membership is allowed.

## Stable 26-domain taxonomy
The existing 26 domain packages remain the organizational taxonomy. Scope descriptions are broadened; no fixed empty folders are generated. Language records can map to multiple domains and paradigms.

## CORE architecture
- `manager.py`: canonical entry point for status, health, catalog, domains, language search/lookup, tiers and domain manager access.
- `catalog.py`: registry, compatibility facade, capabilities and tier metadata.
- `catalog.json`: 26 domain definitions and scope.
- `domain_catalog.py`: validated domain discovery.
- `language_catalog.py`: curated languages, dialects, DSLs and adjacent format metadata; searchable and non-exhaustive.
- `contracts.py`: typed tenant, secret reference, language record, readiness and result contracts.
- `policy.py`: metadata redaction and tenant/capability guardrails.
- `module_service.py`: read-only per-domain service.
- `orchestrator.py`: language/domain discovery and health.
- `service.py`: public service facade.
- `ecosystem_manifest.json`: identity, scope, tiers and layer boundaries.
- `tests/test_core_domains.py`: integrity and API behavior tests.

## Tiers
Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme. Tier labels describe catalog/governance and possible service levels, not installed compiler/runtime/package availability or execution entitlement.

## Layer boundaries
CORE owns identity, taxonomy, metadata, policy, discovery, lifecycle and readiness. API owns external registries, provider adapters and transport. Storage owns durable records/artifacts and retention. Database owns schemas/migrations/transactions. Runtime/Engine owns compiler/interpreter execution, sandbox, jobs, queues and quotas. Application/UI owns IDE/workspace and user flows.

CORE does not execute code, compile, install packages, run builds, call external APIs, store secrets or validate licensing. Execution must use a separately provisioned isolated sandbox, dependency controls, quotas, audit and security review.

## Master catalog relationship
The 2468-target master catalog is the planning taxonomy for the whole ecosystem. This CORE includes relevant computer/software/technology/developer topics without copying unrelated entries or manufacturing counts. Records are individually meaningful and coverage remains curated/non-exhaustive.

## Current coverage status
- Domain packages: 26.
- Curated language and language-adjacent metadata inventory: see `language_catalog.py`; not exhaustive.
- Runtime/compiler execution and external integrations: not performed or verified.
- Credentials: external secret-store references only.
