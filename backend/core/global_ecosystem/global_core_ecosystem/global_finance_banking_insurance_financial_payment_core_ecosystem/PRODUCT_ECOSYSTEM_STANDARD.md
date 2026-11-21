# Finance Ecosystem Product Standard

1. One canonical package per distinct capability; no duplicate domain folders.
2. Keep banking, insurance, lending, investment, accounting/tax and payment processing separate but interoperable.
3. Keep provider-specific adapters inside the owning domain; provider directories do not imply live connections.
4. Use shared identifiers and contracts; never duplicate customer, account, policy, transaction or ledger ownership.
5. Separate read models from transaction execution and ledger writes.
6. Require explicit authorization, idempotency, audit trails, reconciliation and least-privilege access for any future transaction service.
7. Apply jurisdiction-specific licensing, KYC/AML, sanctions, privacy, consumer-protection and retention requirements.
8. Do not store secrets, PAN/CVV, authentication factors or unencrypted account data in source control.
9. Add Python modules only for implemented Python responsibilities. Add PHP only when a real PHP runtime or integration boundary requires it.
10. A folder is a registered scaffold until code, tests, security review and operational evidence establish implementation.
