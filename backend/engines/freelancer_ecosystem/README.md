# GLOBAL FREELANCER ECOSYSTEM

This engine connects the freelancer API layer to SUPREMESETUHUB's central database
and existing storage engine.

## Layer connections

- API: `backend/api/global_freelancer_ecosystem.py`
- Engine: `backend/engines/freelancer_ecosystem/manager.py`
- Central database repository: `backend/database/freelancer_ecosystem.py`
- Core catalog: `backend/core/global_ecosystem/global_core_ecosystem/catalog.py`
- API hierarchy: `backend/api/global_ecosystem/global_api_ecosystem.py`
- Physical file bytes: existing `StorageEngine` and authenticated `/api/v1/storage/files` routes.

## Current foundation capabilities

Owner-scoped metadata record types: PROFILE, SERVICE, PORTFOLIO, PROJECT,
APPLICATION, and WORK_HISTORY. Records start as DRAFT by default. Payloads are
bounded JSON objects; file bytes are not placed inside database rows. Optional
storage asset references are accepted only after the existing storage engine
confirms the current actor can view each asset.

## HTTP routes

- `GET /api/v1/global-freelancer-ecosystem/status`
- `GET /api/v1/global-freelancer-ecosystem/catalog`
- `GET /api/v1/global-freelancer-ecosystem/records`
- `POST /api/v1/global-freelancer-ecosystem/records`
- `GET /api/v1/global-freelancer-ecosystem/records/{record_id}`

All routes require a valid authenticated session. Record reads are scoped to the
authenticated actor. This initial foundation does not expose public job listings,
submit applications to third-party marketplaces, process payments, verify jobs,
or claim any external provider is connected.

## Safety and rollout

The database table is created additively with `CREATE TABLE IF NOT EXISTS` and
does not modify or delete existing tables. Production readiness remains false
until the real deployment's database durability, file storage, provider
authorization, backups, restore tests, and deployment behavior are verified.
