# Global Finance, Banking, Insurance & Financial Payment Core Ecosystem

This is the canonical finance-domain umbrella for global and Bharat-facing finance capabilities. It covers banking, insurance, financial markets, investment, lending, accounting, tax, treasury, compliance, financial infrastructure and payment processing.

## Architecture
- Existing payment-provider, rail, checkout, billing, payout, risk and compliance packages are preserved in place.
- Finance and insurance packages are added as direct domain packages.
- Shared contracts and policy are defined once at this root; domain packages own their specialized capabilities.
- Provider names are integration targets, not claims of active integrations.
- No live banking, payment, lending, investment or insurance transaction is performed by this catalogue.

## Scope boundaries
- Payment processing is distinct from deposit-taking banking, lending, insurance underwriting and investment management.
- Regulated activities require jurisdiction-specific authorization, KYC/AML, privacy, consumer-protection and security controls.
- Credentials, cardholder data, bank account secrets and sensitive financial records must never be committed to this repository.

## Entry points
- `catalog.py`: canonical package and domain catalogue.
- `manager.py`: read-only package/domain lookup.
- `service.py`: service facade for catalogue queries.
- `policy.py`: scope and safety boundaries.
- `test_core_domains.py`: catalogue integrity tests.

All packages remain scaffolds until separately implemented, reviewed and tested.
