# Finance Core Product and Engineering Standard

1. One canonical package per distinct finance capability or provider.
2. Keep banking, insurance, lending, investments, accounting, risk and payments separate but interoperable.
3. Provider directories are discovery records, not proof of commercial relationship, API access or live integration.
4. Require tenant/actor context, least privilege, idempotency and immutable audit records in future transaction services.
5. Keep ledger ownership, settlement and reconciliation explicit.
6. Apply jurisdiction-specific licensing, KYC/AML, sanctions, privacy and consumer-protection requirements.
7. Store credentials and cryptographic material only in an approved external secret manager.
8. Never commit card security codes, plaintext bank credentials, private keys, seed phrases or unencrypted financial records.
9. Keep Core read-only. Transaction execution belongs in separately authorized API/service layers.
10. Add Python or PHP modules only when an implemented runtime responsibility requires them.
11. A package remains CORE_CATALOG_ONLY until implementation, tests, security review and operational evidence are verified.
