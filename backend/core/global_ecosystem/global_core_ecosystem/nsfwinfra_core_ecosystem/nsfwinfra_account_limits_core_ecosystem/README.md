# ACCOUNT LIMITS INFRA CORE ECOSYSTEM

**Parent:** NSF Winfra Core Ecosystem  
**Package:** `nsfwinfra_account_limits_core_ecosystem/`  
**Ecosystem ID:** `NSFW-INFRA-ACCOUNT-LIMITS-CORE`

## Scope

Metadata and policy definitions for account/tenant resource quotas, usage windows, rate and concurrency limits, warning thresholds, reset schedules, plan/entitlement references and enforcement boundaries. Actual metering, billing, authorization and enforcement belong to their dedicated layers.

## Capability metadata

- `QUOTAS`
- `USAGE_LIMITS`
- `RATE_LIMITS`
- `PLAN_ENTITLEMENT_REFERENCES`
- `RESOURCE_LIMITS`
- `LIMIT_POLICY_METADATA`
- `WARNING_THRESHOLDS`
- `RESET_WINDOWS`
- `ABUSE_PREVENTION_METADATA`
- `READINESS`

## Package interface

- `manager.py`: canonical package manager, status and capability inventory.
- `__init__.py`: public package exports.

The manager reports `CORE_CATALOG_ONLY`; it does not execute infrastructure operations, persist records, call APIs, or claim verified live connections. Authorization, secrets, transport, execution and persistence remain in their designated layers. Add package files only for concrete additional responsibilities.
