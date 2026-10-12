# SUPREME Global Digital Sales

This marketplace is digital-download-only. It has no physical products, printing, packing or shipping workflow.

## Country coverage vs checkout availability
The catalog can be browsable globally, but checkout must be enabled country-by-country after confirming payment-provider support, legal restrictions, seller obligations, tax treatment and customer rules. Do not enable every country with a blanket flag. This migration does not yet populate every ISO country or claim all countries are payment/legal supported.

## Currency
The migration seeds a useful starter set of ISO 4217 currencies, not the full official currency list. Import maintained ISO country and currency reference data before enabling country-specific checkout. Currency minor-unit precision varies; do not assume all currencies have two decimals. FX conversions require a reputable live provider, a timestamp and expiry, plus clear final pricing before payment.

## Tax
No tax rates are guessed or prefilled. The tax table records jurisdiction, rate, effective dates, source URL, registration status and verification status. Verify whether digital downloads are taxable and whether the seller must register, collect, invoice or file in each jurisdiction. Use a qualified tax professional for seller-specific obligations. Checkout policy denies sales unless the country tax state is VERIFIED.

## Payments
- UPI is for India checkout through a properly activated payment provider. Put the exact verified UPI VPA in server secrets; a phone number alone is not automatically a valid VPA.
- PayPal India account holders can receive international payments subject to account verification and compliance requirements; PayPal says domestic Indian payments cannot be received. Verify current official guidance before activating.
- Payment methods are seeded disabled and NOT_CONFIGURED. Provider accounts, keys, KYC and webhooks have not been activated by this code.
- Never put payment secrets in GitHub or frontend JavaScript. Real checkout requires provider order creation, signed webhook verification, idempotency, reconciliation and secure time-limited downloads.

## Global trends and events
The campaign calendar stores country-targeted event dates, sources and verification status. Populate it from current reputable sources and verify dates, cultural context and IP rights. Do not assume every country celebrates the same events. Validate trend hypotheses against actual visits, conversion and sales.

## Apply migration and test
1. Import database/schema.sql, then database/migrations/002_global_markets_payments_taxes.sql into a disposable MySQL 8 database.
2. Import and verify maintained ISO country/currency reference data.
3. Configure server secrets and provider sandbox credentials.
4. Verify country-specific taxes and selling restrictions.
5. Test payment signatures, webhooks, duplicate events, failed payments and secure download links.
6. Enable live checkout only country-by-country after KYC, tax and provider approval.

This is a schema/policy foundation, not a live payment or tax engine. It does not create provider accounts, connect live FX/trend feeds, populate every country, or guarantee sales. The USD 4.6 million target is a business goal, not a guaranteed outcome.
