# Global Finance, Banking & Insurance API Ecosystem

This is the **sole canonical implementation** for Finance, Banking & Insurance. The former root-level `finance_banking_insurance/` package has been moved into this folder; its catalogue, service, schemas, routes and category documentation now live here.

**Canonical domain ID:** `finance_banking_insurance`  
**Coverage:** India + Global  
**Status:** taxonomy/API scaffold only; not a bank, insurer, lender, investment adviser, regulated financial service, or proof of live provider integrations.

## Architecture
- The 15 finance categories remain the canonical category structure.
- Previously separate finance-support identifiers map into the relevant canonical categories through `LEGACY_CATEGORY_CROSSWALK`.
- The central domain registry and industry router import this package directly.
- `investment_finance_support_business_api_ecosystem/` remains a compatibility facade; it does not own a duplicate taxonomy.
- `global_payment_business_api_ecosystem/` contains payment-platform and payment-service provider packages such as PayPal, Stripe, Epoch, Paxum, Segpay, Verotel and CCBill.

## API
- `GET /industries/finance-banking-insurance/status`
- `GET /industries/finance-banking-insurance/categories`
- `GET /industries/finance-banking-insurance/categories?q=...`
- `GET /industries/finance-banking-insurance/categories/{category_id}`

## Compliance boundary
This is a taxonomy and discovery scaffold, not a live directory, financial advice engine, payment rail, lender, insurer, investment product, government-benefit eligibility engine, or production integration. Category membership does not verify a provider, professional licence, product, scheme, or government affiliation. Verify official sources, jurisdiction, licensing and eligibility before displaying claims.
