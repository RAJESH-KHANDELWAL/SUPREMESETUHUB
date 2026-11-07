# Global PayPal API Ecosystem

Canonical provider-owned PayPal REST API catalog for the SUPREMESETUHUB platform.

- Provider ID: `paypal`
- Main catalog: `paypal_api_ecosystem.py`
- Service-family catalogs: 13
- Authentication model: OAuth 2.0 client credentials
- Production API base: `https://api-m.paypal.com`
- Sandbox API base: `https://api-m.sandbox.paypal.com`
- Live connection: **not verified**

## Service families

- Checkout (`checkout`)
- Orders (`orders`)
- Payments (`payments`)
- Payouts (`payouts`)
- Subscriptions (`subscriptions`)
- Invoicing (`invoicing`)
- Billing Plans (`billing_plans`)
- Vault Payment Methods (`vault_payment_methods`)
- Webhooks (`webhooks`)
- Identity and OAuth (`identity_oauth`)
- Disputes (`disputes`)
- Transaction Search (`transaction_search`)
- Merchant Onboarding (`merchant_onboarding`)

Each service-family directory contains its own provider catalog module. These are catalog scaffolds, not completed operational integrations.

## Credentials and environments

Configure `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` in the deployment secret manager. Keep sandbox and production credentials separate. Never commit secrets or log access tokens.

Use the official OAuth endpoint for the selected environment, cache tokens only until expiry, and send credentials only to the matching API environment.

## Payment safety and reliability

- Verify webhook signatures before trusting event payloads.
- Use PayPal-supported idempotency mechanisms for payment mutations.
- Validate merchant account eligibility, currency, country, and product capabilities.
- Do not treat a successful OAuth token request as proof that every PayPal product is enabled.
- Test against sandbox before any production rollout.
- Do not mark this provider live until authenticated API and webhook tests pass.

## Official documentation

- [PayPal REST APIs](https://developer.paypal.com/api/rest/)
- [Authentication](https://developer.paypal.com/api/rest/authentication/)
- [Webhooks](https://developer.paypal.com/api/rest/webhooks/)
- [Orders API](https://developer.paypal.com/docs/api/orders/v2/)
- [Payments API](https://developer.paypal.com/docs/api/payments/v2/)
