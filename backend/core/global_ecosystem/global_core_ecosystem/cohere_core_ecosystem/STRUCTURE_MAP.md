# Cohere CORE Structure Map

Root: backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/

cohere_core_ecosystem/
|-- README.md
|-- ARCHITECTURE.md
|-- PRODUCT_ECOSYSTEM_STANDARD.md
|-- COHERE_CORE_IMPLEMENTATION_STATUS.md
|-- STRUCTURE_MAP.md
|-- __init__.py
|-- ecosystem_config.py
|-- ecosystem_manifest.json
|-- catalog.py
|-- product_catalog.py
|-- product_ecosystem_index.json
|-- domain_catalog.py
|-- contracts.py
|-- policy.py
|-- module_service.py
|-- orchestrator.py
|-- manager.py
|-- service.py
|-- php/
|   |-- CohereCoreContract.php
|-- cohere_classify_core_ecosystem/
|-- cohere_command_core_ecosystem/
|-- cohere_embed_core_ecosystem/
|-- cohere_rerank_core_ecosystem/
|-- cohere_tokenize_core_ecosystem/
|-- cohere_shared_compatibility/
|-- cohere_shared_configuration/
|-- cohere_shared_contracts/
|-- cohere_shared_documentation/
|-- cohere_shared_events/
|-- cohere_shared_exceptions/
|-- cohere_shared_orchestration/
|-- cohere_shared_security/
|-- cohere_shared_testing/
|-- cohere_shared_utilities/
|-- cohere_shared_validation/

## Capability package layout

Every cohere_<capability>_core_ecosystem/ package follows the Google product-Core standard:

cohere_<capability>_core_ecosystem/
|-- README.md
|-- __init__.py
|-- contracts.py
|-- service.py
|-- ecosystem_config.py
|-- ecosystem_manifest.json
|-- authentication/
|   |-- contract.php
|-- capabilities/
|-- docs/
|-- events/
|-- lifecycle/
|-- models/
|-- schemas/
|-- security/
|-- services/
|-- tests/
    |-- test_contracts.py

The package-level duplicate php/ directory is not used; the PHP authentication-context contract is owned by authentication/.

## Capability inventory

| Package | Capability | Domain |
|---|---|---|
| cohere_classify_core_ecosystem | classify | language_understanding |
| cohere_command_core_ecosystem | command | text_generation |
| cohere_embed_core_ecosystem | embed | vector_representation |
| cohere_rerank_core_ecosystem | rerank | language_understanding |
| cohere_tokenize_core_ecosystem | tokenize | text_processing |

## Provider-wide shared areas

- cohere_shared_compatibility
- cohere_shared_configuration
- cohere_shared_contracts
- cohere_shared_documentation
- cohere_shared_events
- cohere_shared_exceptions
- cohere_shared_orchestration
- cohere_shared_security
- cohere_shared_testing
- cohere_shared_utilities
- cohere_shared_validation

## Boundaries

CORE owns contracts, validation, capability metadata, policy, lifecycle and readiness. API owns transport and provider authentication adapters. ENGINE owns execution and retries. DATABASE/STORAGE own persistence and artifacts. Application/UI owns user workflows. Live calls remain disabled until the integration and security release gates pass.
