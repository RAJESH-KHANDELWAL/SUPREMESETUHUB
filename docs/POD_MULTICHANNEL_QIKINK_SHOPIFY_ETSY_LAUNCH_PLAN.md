# SUPREMESETUHUB Multi-Channel POD Launch Plan

**Owner decision:** Qikink is the only selected print-on-demand fulfilment provider. Printify remains on hold. The storefront/sales channels in scope are WordPress + WooCommerce, Shopify, and Etsy.

## Non-negotiable launch boundary

This document is a reviewed implementation plan, not proof that any store is connected. Do not enable live fulfilment, create real customer orders, or report revenue until each channel's authorization, SKU mapping, shipping/tax, payment, refunds, tracking, and end-to-end test order have been verified.

## Channel-by-channel integration path

### 1. WordPress + WooCommerce — Qikink
- Use Qikink's official WooCommerce plugin/authentication flow.
- Verify the store is shown as connected in the Qikink seller dashboard.
- Push a sample original design/product and verify variant IDs, size/color, SKU/design SKU, prices, product images, shipping zones, taxes, checkout, order import, tracking and cancellation/refund handling.
- Keep the custom SUPREME Qikink bridge disabled until its payload contract and sandbox test are proven.
- Official Qikink guide: https://qikink.com/help/integrations/integrating-your-woocommerce-store/

### 2. Shopify — Qikink
- Use Qikink's official Shopify app; authenticate using the Qikink dashboard flow and OTP inside the official services. Never place credentials or OTPs in GitHub issues, source code, or chat.
- Confirm the Shopify store appears as connected in Qikink.
- Create/push one test product and confirm variant/SKU mapping and fulfilment location.
- Keep real order processing disabled until shipping, tax, checkout/payment, cancellation/refund, tracking and one end-to-end test order are verified.
- Official Qikink guide: https://qikink.com/help/integrations/integrating-your-shopify-store/

### 3. Etsy — separate sales-channel adapter; Qikink-native connection not assumed
- Current Qikink integration documentation lists Shopify and WooCommerce integrations; do not claim a native Qikink Etsy connector unless Qikink confirms it in writing.
- Etsy can permit production partners for items based on the seller's original designs, but the seller must disclose the production partner and accurately represent dispatch/manufacturing details. Generic resale or unmodified wholesale products are not eligible.
- Before listing, confirm Etsy shop onboarding/payment eligibility for the seller's country, item eligibility, production-partner disclosure, image rules, shipping origin/processing times, fees/taxes, and the current Etsy API/automation terms.
- Only then choose a supported path: Etsy API integration using authorized app credentials and webhooks, or a clearly documented manual order workflow. Never scrape Etsy or bypass its API/marketplace rules.
- Do not automatically submit Etsy orders to Qikink unless an authorized integration or tested operational workflow exists. Unmapped orders must remain on hold.
- Etsy policy references:
  - https://help.etsy.com/hc/en-us/articles/23948763872151-Does-Etsy-Allow-Drop-Shipping-or-Reselling
  - https://help.etsy.com/hc/en-us/articles/360000336547-Working-with-Production-Partners-on-Etsy
  - https://www.etsy.com/legal/creativity/

## Shared SUPREMESETUHUB architecture

- Treat WooCommerce, Shopify, and Etsy as distinct sales-channel adapters, not as one assumed universal connector.
- Normalize channel orders into a common internal order record while preserving the source channel, source order ID, line items, currency, tax, shipping, payment state and customer-consent requirements.
- Use idempotency keys based on channel + source order ID + event/action so retries cannot create duplicate fulfilment submissions.
- Keep separate states for payment authorized/captured, order eligible for fulfilment, provider accepted, shipped/tracking assigned, refunded/cancelled, and reconciled. A channel order or successful API response is not proof of settlement or bank credit.
- Store secrets only in approved server-side secret storage/environment settings. Never commit API keys, tokens, passwords, OTPs or customer personal data.
- Use least-privilege OAuth scopes, verify webhook signatures, reject stale/duplicate events, log redacted diagnostics, retry transient failures with limits, and send permanent failures to a review queue.
- Keep test/sandbox and production credentials and data separate.

## WordPress API base URL check

The WordPress connector currently defaults to `https://api.rajeshkhandelwalofficial.com`, while the owner dashboard links to `https://supremesetuhub-3v4e.onrender.com/health`. These are different hosts. Do not assume either is the correct production base without testing both the health endpoint and required API routes. In WordPress Settings → SUPREMESETUHUB, configure the confirmed HTTPS API base (host only, no trailing slash/path), save it, and run **Test Backend Connection**. The expected result must confirm health and the POD catalog route; then test required digital/people routes separately.

## Acceptance checklist

- [ ] Correct API base confirmed by live health and catalog tests.
- [ ] WooCommerce–Qikink official connection verified; product variants/SKUs mapped.
- [ ] Shopify–Qikink official connection verified; product variants/SKUs mapped.
- [ ] Etsy shop eligibility and payment onboarding confirmed for seller's country.
- [ ] Etsy original-design and production-partner disclosures complete.
- [ ] Etsy integration route approved and authorized; no unsupported direct Qikink link assumed.
- [ ] Shipping origin, delivery estimates, shipping prices, taxes and return/refund policies reviewed for each channel/market.
- [ ] Payment webhooks, signature checks, idempotency, order/refund/cost ledger and reconciliation tested.
- [ ] One non-customer test order/sample per supported channel completed with no duplicate fulfilment.
- [ ] Customer emails, tracking, cancellations and support escalation verified.
- [ ] Only after all gates pass: owner explicitly approves live order submission.

## Verification sources

- Qikink integrations overview: https://qikink.com/help/integrations/
- Qikink Shopify: https://qikink.com/help/integrations/integrating-your-shopify-store/
- Qikink WooCommerce: https://qikink.com/help/integrations/integrating-your-woocommerce-store/
- Etsy production partner policy: https://help.etsy.com/hc/en-us/articles/360000336547-Working-with-Production-Partners-on-Etsy
- Etsy dropshipping/reselling policy: https://help.etsy.com/hc/en-us/articles/23948763872151-Does-Etsy-Allow-Drop-Shipping-or-Reselling
