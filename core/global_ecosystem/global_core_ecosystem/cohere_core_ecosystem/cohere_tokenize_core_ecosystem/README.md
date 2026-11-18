# COHERE TOKENIZE CORE ECOSYSTEM

**Ecosystem ID:** `COHERE-TOKENIZE-CORE-ECOSYSTEM`  
**Parent:** COHERE CORE ECOSYSTEM  
**Capability:** `tokenize`  
**Domain:** `text_processing`  
**Status:** `contract_only`

## Responsibility

Define text tokenization request contracts. CORE does not tokenize through a provider SDK or claim tokenizer/model availability.

## Request contract

- `text`: non-empty text string
- `model`: optional model identifier

## Standard package layout

This package follows the Google product-Core package convention: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, and `tests/`. The PHP caller-context contract is located at `authentication/contract.php`.

## Layer boundaries

CORE owns capability identity, request contracts, validation, policy metadata, lifecycle vocabulary and readiness. API owns transport and provider response normalization. ENGINE owns SDK execution, retries, timeouts and scheduling. DATABASE/STORAGE own persistence and artifacts. Application/UI owns sessions, consent and workflows.

No credentials, API calls, model execution, persistence or UI are implemented in this package. Live operations remain disabled until separately approved API/ENGINE adapters, secure credentials, entitlement checks and integration tests are verified.
