# COHERE RERANK CORE ECOSYSTEM

**Ecosystem ID:** `COHERE-RERANK-CORE-ECOSYSTEM`  
**Parent:** COHERE CORE ECOSYSTEM  
**Capability:** `rerank`  
**Domain:** `language_understanding`  
**Status:** `contract_only`

## Responsibility

Define query/document relevance-ranking contracts. CORE does not rank documents or invoke models.

## Request contract

- `query`: non-empty query string
- `documents`: non-empty sequence of document strings
- `top_n`: optional positive integer

## Standard package layout

This package follows the Google product-Core package convention: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, and `tests/`. The PHP caller-context contract is located at `authentication/contract.php`.

## Layer boundaries

CORE owns capability identity, request contracts, validation, policy metadata, lifecycle vocabulary and readiness. API owns transport and provider response normalization. ENGINE owns SDK execution, retries, timeouts and scheduling. DATABASE/STORAGE own persistence and artifacts. Application/UI owns sessions, consent and workflows.

No credentials, API calls, model execution, persistence or UI are implemented in this package. Live operations remain disabled until separately approved API/ENGINE adapters, secure credentials, entitlement checks and integration tests are verified.
