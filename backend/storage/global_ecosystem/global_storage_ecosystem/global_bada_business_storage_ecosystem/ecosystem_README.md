# GLOBAL BADA BUSINESS Ecosystem Foundation

## Storage responsibilities
- Business ecosystem identity and taxonomy
- Platform-specific metadata namespaces
- Referral and campaign metadata definitions
- Business record lifecycle and retention metadata
- Health/readiness contracts

## Separation rules
- Keep affiliate platform records separated by platform identity.
- Keep YOUTAG Wellness and Recharges app data separated beneath the canonical YOUTAG business namespace.
- Keep network marketing/direct selling records distinct from affiliate marketing records.
- Do not mix leads, customer consent, commissions, transactions or payout records across platforms.
- Store secrets only in an approved secret manager; never in repository files.

## Layer boundaries
STORAGE owns taxonomy and metadata. API/integration layers own vendor clients, authentication, webhooks and external network calls. The central database owns production persistence. This package does not itself upload, download, pay commissions or contact external services.

## Readiness
FOUNDATION_READY is not proof of a live provider connection, program eligibility, referral attribution, earnings or payout. Mark an integration CONNECTED only after authorized credentials, live health checks and end-to-end tests pass.
