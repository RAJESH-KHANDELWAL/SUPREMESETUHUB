# SUPREME People, Referral and Follow-up Architecture

This package is SUPREME-owned and is separate from the existing MAIN BASE FOUNDATION
layers at `backend/core`, `backend/engines`, `backend/database` and `backend/storage`.

## Layer map

- `backend/supreme/supreme.py`: SUPREME parent metadata and layer registry.
- `backend/supreme/core/referral_service.py`: orchestration and validation.
- `backend/supreme/engines/referral_engine.py`: explicit person-stage rules, HTTPS referral validation and commission state transitions.
- `backend/supreme/database/referral_repository.py`: persistent records via the existing `DatabaseService`.
- `backend/supreme/storage/referral_store.py`: storage boundary between core and repository.
- Existing API routes remain in `backend/api`; API work is not duplicated here.

## Persistent records

- `supreme_people`: person source, needs shared voluntarily, contact preference/consent, stage and next follow-up.
- `supreme_referral_links`: platform/program, referral URL, WhatsApp contact, personal/team ownership and active state.
- `supreme_referral_events`: auditable events and metadata.
- `supreme_commissions`: order reference, partner, amount in paise, currency and commission state.

## Safety and correctness

- `amount_paise=100` means INR ₹1.00.
- Commission starts as `PENDING`; it must not be presented as income earned until the partner confirms it.
- Allowed transitions are PENDING → APPROVED/REJECTED, APPROVED → PAID/REVERSED, and PAID → REVERSED for corrections.
- Person stages are set from explicit responses/actions, not inferred from silence or guessed mindset.
- `DO_NOT_CONTACT` is a stage for suppression workflows. Messaging is not implemented or sent by these layers.
- Referral URLs must be absolute HTTPS URLs. Platform-specific link validation and conversion webhooks/reconciliation are follow-up integration work.
- Tables are created with `CREATE TABLE IF NOT EXISTS`; existing tables are not dropped.
- These modules are implementation foundations. Runtime import tests and database tests must pass before deployment is described as production-ready.
