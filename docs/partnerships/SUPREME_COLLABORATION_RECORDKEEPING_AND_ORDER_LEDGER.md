# SUPREME COLLABORATION RECORDKEEPING & ORDER-BENEFIT LEDGER

## Purpose and status
Maintain traceable written records of every proposal, permission, commercial term, qualifying order/referral, calculation, settlement, dispute and termination. This is an operating standard, not a live database feature until implemented.

## Required linked records
1. Partner identity and authority verification.
2. Original proposal, source/date, purpose, scope and requested permissions.
3. Signed agreement PDF plus editable source, version, signatures/acceptance evidence and schedules.
4. Permission register: permission/scope, approver, timestamp, expiry and revocation.
5. Integration register: provider, environment, approved scopes, technical owner, secret reference (never secret value), tests and offboarding.
6. Order/attribution ledger and evidence.
7. Settlement statement with opening balance, additions, reversals, adjustments, payable, paid reference and closing balance.
8. Change/dispute log with evidence and resolution.
9. Closure record: termination, revoked access, data handling and final reconciliation.

## Order-benefit ledger fields
| Field | Requirement |
|---|---|
| ledger_entry_id | Unique immutable ID |
| collaboration_id | Links signed agreement |
| agreement_version | Version effective for event |
| provider_id | Platform/merchant source |
| provider_order_ref | Minimal source order reference |
| event_type | Lead, referral, paid/completed order, refund, chargeback, adjustment, payout |
| event_timestamp | ISO 8601 timestamp with timezone |
| attribution_evidence_ref | Approved referral/campaign/CRM evidence |
| source_status | Status verified against source provider |
| eligible_base_minor | Eligible base in minor currency units |
| currency | ISO 4217 currency code |
| rate_or_fixed_minor | Agreed rate/amount and model |
| calculated_benefit_minor | Calculation result |
| hold_or_reversal_minor | Refund/chargeback/hold adjustment |
| approved_payable_minor | Payable after signed rules and review |
| reviewed_by / reviewed_at | Reviewer and timestamp |
| payout_reference | Safe payment/settlement reference |
| dispute_status | None/open/resolved and case reference |
| evidence_location | Access-controlled reference, not public URL |

Use integer minor units for money in production, explicit currency and agreement-defined rounding. Never overwrite past ledger entries: add a dated reversal/correction. Do not store unnecessary customer data, payment-card details, passwords or secret tokens.

## Reconciliation control
For each agreement and settlement period, derive eligible events from source-verified records; apply the signed formula and approved adjustments; account for refunds, cancellations, chargebacks and holds under the agreement; calculate proposed payable; obtain reviewer approval; record actual settlement and remaining balance. The signed agreement governs the exact formula, taxes/fees, timing, caps and rounding.

## Approval gates
1. Proposal received — not an approved partnership.
2. Identity and authority checked.
3. Scope and each permission approved.
4. Commercial schedule completed and accepted by both parties.
5. Agreement signed/accepted and archived.
6. Least-privilege integration tested.
7. Order/referral and refund cases reconciled using test data.
8. Both sides approve written go-live checklist.
9. Reconciliation reviewed before payout.
10. Closure, revocation and final statement completed.

Any missing mandatory gate means pending/blocked.

## Evidence integrity and retention
- Store final records in access-controlled storage with backup and version history.
- Preserve original signed artifacts and metadata. A checksum can detect later changes but does not alone prove identity, authority or legal validity.
- Record date/time/timezone, actor, action and source evidence. Never backdate; use dated amendments.
- Give each party a copy of the final agreement and applicable statements.
- Define retention/deletion by contract and applicable law; do not retain personal data indefinitely by default.
- Never commit secrets, full payment details or sensitive customer data to public Git history.

## Future CSV/database registers
Create protected records for collaboration register, permission register, order-benefit ledger, settlement register and change/dispute log. Blank templates must contain no real customer/partner data. Live entries belong in access-controlled database/storage, not public Git history.

## Implementation limitation
These documents do not implement a live records system. Production use requires authenticated access, role-based permissions, append-only audit events, safe exports, backup/restore tests, retention/deletion workflow and security tests. Obtain legal/accounting review for the applicable jurisdiction and business model.
