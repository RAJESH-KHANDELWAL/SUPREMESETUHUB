# Finance, Banking, Insurance & Business Support API Ecosystem

**Canonical domain ID:** `finance_banking_insurance`  
**Canonical implementation:** `industry_api_ecosystems/finance_banking_insurance/`  
**Coverage:** India + Global

## Unified scope
This single ecosystem owns banking and deposits, payments and remittances, lending and credit, insurance and claims, wealth and investment education, capital markets, accounting and tax, fintech, microfinance, corporate finance, grants and schemes discovery, MSME finance support, export finance, pensions, risk and compliance, and financial education.

## Architecture
- The 15 existing finance categories remain the canonical category structure.
- Previously separate finance-support identifiers are mapped into the relevant canonical categories through `LEGACY_CATEGORY_CROSSWALK`.
- The central domain registry imports this package as the single finance domain.
- `investment_finance_support_business_api_ecosystem/` remains only as a compatibility facade; it no longer owns an independent taxonomy.
- `finance_banking_insurance_api_ecosystem/` is a public import alias to the same implementation.

## API
- `GET /industries/finance-banking-insurance/status`
- `GET /industries/finance-banking-insurance/categories`
- `GET /industries/finance-banking-insurance/categories?q=...`
- `GET /industries/finance-banking-insurance/categories/{category_id}`

## Data and compliance boundaries
This is a taxonomy and discovery scaffold, not a live directory, financial advice engine, payment rail, lender, insurer, investment product, government-benefit eligibility engine, or production integration. Category membership does not verify a provider, professional licence, product, scheme, or government affiliation. Verify official sources, jurisdiction, licensing and eligibility before displaying claims. Financial recommendations, transactions, KYC/AML, privacy, security and cross-border services require specialist legal and compliance review.
