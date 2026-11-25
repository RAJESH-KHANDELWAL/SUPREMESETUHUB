# COHERE COMMAND CORE ECOSYSTEM

**Ecosystem ID:** `COHERE-COMMAND-CORE-ECOSYSTEM`  
**Parent:** COHERE CORE ECOSYSTEM  
**Capability:** `command`  
**Domain:** `text_generation`  
**Status:** `contract_only`

## Responsibility

Define text-generation and conversational request contracts. CORE validates request shape only; it does not generate text or call a model.

## Request contract

- `message`: non-empty prompt/message string
- `chat_history`: optional sequence of mapping objects
- `model`: optional model identifier

## Standard package layout

This package follows the Google product-Core package convention: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, and `tests/`. The PHP caller-context contract is located at `authentication/contract.php`.

## Layer boundaries

CORE owns capability identity, request contracts, validation, policy metadata, lifecycle vocabulary and readiness. API owns transport and provider response normalization. ENGINE owns SDK execution, retries, timeouts and scheduling. DATABASE/STORAGE own persistence and artifacts. Application/UI owns sessions, consent and workflows.

No credentials, API calls, model execution, persistence or UI are implemented in this package. Live operations remain disabled until separately approved API/ENGINE adapters, secure credentials, entitlement checks and integration tests are verified.
