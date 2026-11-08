# Global Business Ecosystem — Intelligence Layer

A general-purpose, India-first and global-ready Business domain intelligence
package. It extends the established Business domain; it does not create a
parallel record store or duplicate the existing API.

## Capabilities

- **Business profile intelligence:** explainable completeness and documentation
  signals based on supplied profile fields.
- **Readiness scoring:** deterministic documentation-readiness indicator with
  maturity bands and transparent assumptions.
- **Risk signals:** missing profile fields, incomplete compliance evidence,
  declared non-compliance, and missing platform verification.
- **Action planning:** prioritized operational follow-up tasks derived from
  assessment signals.
- **Portfolio comparison:** compare profile-documentation readiness without
  claiming market ranking, profitability, creditworthiness or viability.
- **Provider boundary:** typed provider contract and explicit registry for
  optional future AI/market-data adapters. No provider is enabled by default.

## Architecture and ownership

- Existing domain model: `backend/businesses/model.py`
- Existing persistence/service: `backend/businesses/service.py` and
  `backend/businesses/connection.py`
- Existing authenticated API and owner checks:
  `backend/api/businesses.py`
- Shared persistence remains the `business_profiles` table through
  `backend.database.service.DatabaseService`.
- This package owns intelligence orchestration only. It does not own API
  transport, CORE orchestration, ENGINE execution, DATABASE, STORAGE, SECURITY
  or SERVER infrastructure.

## Current API surface

Import `GlobalBusinessEcosystemService` from this package and call:
- `health()`
- `assess(business_id)`
- `action_plan(business_id)`
- `compare(business_ids)`
- `provider_capabilities()`

Callers must enforce the existing business ownership/authorization checks
before exposing any assessment or comparison results.

## Scoring and limitations

The readiness score is a deterministic profile-documentation heuristic, not
an AI model prediction. It does not assess financial health, legal compliance,
creditworthiness, fraud, business success, or investment suitability.
All user-supplied data is treated as unverified. No external registry,
government, credit bureau, LLM or live market source is queried.

External adapters must be independently implemented, security-reviewed,
credential-managed and tested before they are registered as enabled/live.
