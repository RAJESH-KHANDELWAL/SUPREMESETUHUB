# GLOBAL CORE ECOSYSTEM People, Referral and Follow-up Architecture

The referral implementation belongs to the MAIN BASE FOUNDATION layers. SUPREME and
SUPREME ECOSYSTEM remain separate systems and do not own duplicate CORE, ENGINE,
DATABASE, or STORAGE implementations.

## Layer map

- `backend/supreme.py`: SUPREME entry point only.
- `backend/supreme/supreme_ecosystem.py`: SUPREME ECOSYSTEM entry module.
- `backend/core/global_ecosystem/global_core_ecosystem/referral_service.py`: CORE orchestration and validation.
- `backend/engines/referral_engine.py`: person-stage rules, HTTPS referral validation and commission state transitions.
- `backend/database/referral_repository.py`: persistent records via the existing central `DatabaseService`.
- `backend/storage/referral_store.py`: STORAGE boundary between CORE and DATABASE.
- API endpoints remain in `backend/api/`; API code is not duplicated in CORE.

## CORE hierarchy

```text
backend/core/
└── global_ecosystem/
    ├── existing GLOBAL ECOSYSTEM modules
    └── global_core_ecosystem/
        ├── __init__.py
        └── referral_service.py
```

## Persistent records

The current database table names remain unchanged for backward compatibility:
`supreme_people`, `supreme_referral_links`, `supreme_referral_events`, and
`supreme_commissions`. They are created with `CREATE TABLE IF NOT EXISTS`; existing
tables are not dropped or renamed.

- People records include source, need category, contact preference/consent, stage and next follow-up.
- Referral links record platform/program, HTTPS URL, ownership and active state.
- Events retain auditable actions and metadata.
- Commissions record order reference, partner, amount in paise, currency and status.

## Safety and correctness

- `amount_paise=100` means INR ₹1.00.
- Commission starts as `PENDING`; it must not be presented as earned income until the partner confirms it.
- Allowed transitions are PENDING → APPROVED/REJECTED, APPROVED → PAID/REVERSED, and PAID → REVERSED for corrections.
- Person stages come from explicit responses/actions, not guesses about silence or mindset.
- `DO_NOT_CONTACT` turns off contact consent. Messaging is not implemented or sent by these layers.
- Referral URLs must be absolute HTTPS URLs.
- This architecture change preserves the central database service and existing table names.
