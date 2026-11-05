# Global Finance, Banking & Insurance API Ecosystem

This package consolidates the former root-level `finance_banking_insurance/`
and `finance_banking_insurance_api_ecosystem/` entry points.

The maintained Finance, Banking & Insurance implementation remains in
`industry_api_ecosystems/finance_banking_insurance/`. This global package
re-exports that implementation and shares its package path; it does not create
a duplicate catalog, service, schema, or route implementation.

Coverage intent: India + Global. Status: taxonomy/API scaffold only. This is not
a bank, insurer, lender, investment adviser, regulated financial service, or
proof of live provider integrations.


## Global Payment Business API Ecosystem

Payment platforms and payment-service provider packages are grouped under the child folder `global_payment_business_api_ecosystem/`. This includes PayPal, Stripe, Epoch, Paxum, Segpay, Verotel and CCBill. Payment processing, gateways, merchant services, checkout, billing, payout and settlement references belong here; banking, lending, insurance, investment and accounting remain in their respective Finance categories.
