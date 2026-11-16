# Finance, Banking & FinTech — 20-Domain Coverage Map

**Ecosystem sequence:** #04  
**Canonical package:** `finance_banking_insurance`  
**Coverage intent:** India + Global  
**Status:** Taxonomy and API-discovery scaffold; not a regulated financial service.

This map expands the existing 15-category taxonomy into 20 user-facing business domains. It deliberately reuses the canonical taxonomy instead of creating a second, duplicate finance ecosystem.

| # | Business domain | Canonical category mapping |
|---:|---|---|
| 01 | Banking & Digital Banking | `banking_and_deposits` |
| 02 | UPI & Instant Payments | `payments_and_remittances` |
| 03 | Global Payments & Remittance | `payments_and_remittances`, `foreign_exchange_and_trade_finance` |
| 04 | Payment Gateways & Processors | `payments_and_remittances`, `fintech_and_financial_software` |
| 05 | Credit & Lending | `lending_and_credit` |
| 06 | Loans & Business Financing | `lending_and_credit`, `corporate_finance_and_advisory` |
| 07 | NBFC & Microfinance | `microfinance_and_inclusion`, `lending_and_credit` |
| 08 | Insurance & Reinsurance | `insurance_services`, `insurance_broking_and_claims` |
| 09 | Stock Market & Trading | `capital_markets_and_brokerage` |
| 10 | Mutual Funds & ETFs | `capital_markets_and_brokerage`, `wealth_and_investment_advisory` |
| 11 | Investment & Wealth Management | `wealth_and_investment_advisory` |
| 12 | Personal Finance | `financial_education`, `fintech_and_financial_software` |
| 13 | Business Finance | `corporate_finance_and_advisory`, `accounting_and_bookkeeping` |
| 14 | Accounting & Bookkeeping | `accounting_and_bookkeeping` |
| 15 | Taxation & GST | `accounting_and_bookkeeping` |
| 16 | Financial Compliance & KYC | `risk_and_compliance` |
| 17 | Fraud Detection & Risk Management | `risk_and_compliance` |
| 18 | Cryptocurrency & Blockchain Finance | `fintech_and_financial_software`, `risk_and_compliance` |
| 19 | Financial Technology & AI | `fintech_and_financial_software` |
| 20 | Global Financial Infrastructure | `payments_and_remittances`, `foreign_exchange_and_trade_finance`, `risk_and_compliance` |

## Regulatory and safety boundaries

- Listing a domain does not make this platform a bank, lender, NBFC, insurer, broker, investment adviser, payment aggregator, exchange, tax practitioner, or regulated intermediary.
- Actual financial products, advice, onboarding, KYC/AML, payment processing, lending, insurance distribution, securities activity, custody, and cross-border transfers must be provided only through appropriately authorised entities and compliant integrations.
- Do not store card PINs, CVVs, passwords, OTPs, private keys, or full authentication secrets in this taxonomy service.
- Provider listings and regulatory status must be independently verified against the relevant official regulator and jurisdiction before publication.
- Crypto/blockchain coverage is descriptive and compliance-gated; it is not an endorsement, investment recommendation, or transaction facility.
- India-specific implementations must be reviewed against applicable RBI, SEBI, IRDAI, PFRDA, FIU-IND, GST and data-protection requirements, as relevant to the exact activity. Global coverage requires jurisdiction-by-jurisdiction review.

## Implementation note

The canonical category IDs remain defined in `catalog.py`. This document is a discovery and governance crosswalk; it does not introduce duplicate category registries or claim that live provider integrations exist.
