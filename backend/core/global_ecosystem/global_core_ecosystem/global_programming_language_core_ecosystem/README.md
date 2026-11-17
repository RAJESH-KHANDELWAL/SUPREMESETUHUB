# GLOBAL PROGRAMMING LANGUAGE CORE ECOSYSTEM

A dedicated, read-only CORE control plane for programming languages, language types, runtimes, compilers, specifications, toolchains and developer-language metadata. It is a direct sibling of `global_human_language_core_ecosystem/` under `global_core_ecosystem/`.

## Architecture
- `catalog.py`: stable ecosystem registry and compatibility facade
- `domain_catalog.py` + `catalog.json`: canonical 26-domain taxonomy
- `language_catalog.py`: curated, explicitly non-exhaustive language/type records
- `contracts.py`: typed tenant, result, secret-reference and language contracts
- `policy.py`: tenant-context, capability and metadata-redaction boundaries
- `module_service.py`: reusable read-only domain service
- `orchestrator.py`: domain/language discovery and health summaries
- `service.py`: public control-plane service
- `shared_support/`: cross-cutting support contracts and conventions

## Classification boundary
General-purpose and systems languages are distinct from markup (HTML/XML), stylesheets (CSS), database query languages (SQL), and data-serialization formats (JSON/YAML). A category does not imply that every member is a general-purpose executable language.

## Runtime and security boundary
CORE stores metadata and policy only. It does not compile or execute user code, install packages, invoke compilers, or prove that a runtime is present. Any execution must occur in a separately provisioned, isolated sandbox with resource limits, dependency controls, license checks and security review.

## Coverage and tiers
The catalog is intentionally non-exhaustive. Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme describes service/governance tiers, not guaranteed compiler availability, language support or production runtime entitlement.

## API
`ProgrammingLanguageCoreEcosystemService` exposes status, health, domain and language discovery. `ProgrammingLanguageDomainCoreService` provides policy-aware metadata for one registered domain. Passing a CORE capability check is not authorization to execute code or access external systems.
