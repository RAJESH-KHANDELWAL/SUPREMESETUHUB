# GLOBAL AFFILIATE MARKETING BUSINESS CORE ECOSYSTEM

**Parent:** GLOBAL BADA BUSINESS CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM`

## Mission and ownership

This package owns canonical affiliate-platform identity metadata, program-rule validation, disclosure guardrails, lifecycle metadata, discovery and provider-neutral orchestration.

It does not perform provider authentication, API transport, click redirect hosting, attribution execution, payout processing, ledger settlement, user authentication, or persistence. Those belong to the API, ENGINE, DATABASE, STORAGE and application layers.

## Canonical structure

- `catalog.py`: canonical platform inventory, regional classification and lookup.
- `contracts.py`: repository and record contracts shared by CORE services.
- `models.py`: immutable platform identity model.
- `policies.py`: URL, disclosure, commission, status and activation guardrails.
- `service.py`: repository-injected program, referral and event business workflows.
- `module_service.py`: read-only platform discovery service.
- `orchestrator.py`: CORE status, discovery and workflow composition.
- `manager.py`: canonical manager and read-only 2,468 master-catalog bridge.
- `manager.php`: PHP 8+ structural and read-only master-catalog facade.
- `i_digitalpreneur_core_ecosystem/`: dedicated iDigitalPreneur CORE package, outside `platforms/`.
- `platforms/`: LeadsGuru and Millionaire Track platform-specific namespaces.

The former empty `global/`, `india/`, `affiliate_models/`, `compliance_disclosures/`, `integrations/`, `schemas/` and `tracking_analytics/` placeholder trees are represented by real catalog, model, contract and policy code rather than empty directories.

## Platform inventory and evidence

The catalog preserves 40 previously named Global/India affiliate-network candidates as `DISCOVERY_ONLY`. Their inclusion records a discoverable identity only; it does not assert that a program is currently open, available in a region, approved, connected, or commercially verified.

Platform CORE namespaces are retained separately:
- `I-DIGITALPRENEUR` — dedicated `i_digitalpreneur_core_ecosystem/` package.
- `LEADSGURU` — under `platforms/`.
- `MILLIONAIRE-TRACK` — under `platforms/`.

No ownership, commission, fee, eligibility, attribution, payout or contractual relationship is inferred between platforms. Program terms must be sourced from the relevant platform and verified before activation. Unknown commission rates remain unspecified.

## 2,468 master catalog

The single source of truth remains `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. This package reads it on demand and validates its declared counts. It does not copy, mutate, expand or claim ownership of the master catalog.

The currently declared snapshot is 2,468 target unique entries, 246 current unique entries, 2,222 remaining, 248 numbered source rows, 2 cross-reference rows and 13 sections. The 2,468 target is a planning target, not a requirement to create filler records.

Affiliate marketing maps to the master catalog's existing `S08_affiliate_business` entry. No new master-catalog entry is created by this package.

## Safety and lifecycle invariants

- An active program requires verified terms and a valid HTTP(S) terms URL.
- Affiliate disclosures must be present before a referral is created.
- Only non-negative monetary minor-unit integers are accepted for recorded events.
- Platform identity metadata is not proof of a live integration or account authorization.
- Secrets and access tokens are never stored in CORE.
- Payouts and settlement are outside this package.
