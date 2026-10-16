# SUPREMESETUHUB — Printify WooCommerce setup (ON HOLD)

## Current provider decision

**Do not connect or activate Printify for this launch. Qikink is the only selected print-on-demand provider.** This file is retained to prevent older setup notes from being mistaken for the current plan.

Use the current Qikink-only setup instructions instead:
- [POD Hostinger provider setup](POD_HOSTINGER_PROVIDER_SETUP.md)
- [Master ecosystem roadmap](../issues/38) (repository issue #38)
- [Global People Engine + POD Revenue Launch](../issues/55) (repository issue #55)

## Why this is on hold

- No Printify store connection, product publishing, order sync, shipping configuration, or fulfillment has been verified.
- Do not install a second provider integration or publish products through Printify unless the owner explicitly changes the provider decision.
- Do not copy Printify credentials or API tokens into WordPress pages, GitHub, or source code.

## WordPress launch gates still relevant to Qikink

1. Confirm the canonical WordPress URL in Settings → General and save a non-Plain permalink structure.
2. Confirm WooCommerce checkout and country-specific shipping zones/methods.
3. Confirm Qikink account authorization, exact product/variant SKUs, print-file mapping, and shipping eligibility.
4. Keep live supplier submission disabled until the Qikink sandbox/test flow passes.
5. Verify payment webhooks, duplicate-order protection, cancellations/refunds, tracking, customer notifications, and reconciliation.
6. Do not claim a live integration until a test order is confirmed in both WooCommerce and Qikink.

GitHub code or CI success does not connect a provider account or configure a live WordPress store.
