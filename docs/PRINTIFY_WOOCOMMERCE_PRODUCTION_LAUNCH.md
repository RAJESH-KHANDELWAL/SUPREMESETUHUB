# SUPREMESETUHUB — Printify + WooCommerce Production Launch

## Correct provider
The intended POD provider for this launch is **Printify**, not Qikink. Do not use the Qikink bridge PR for this Printify setup.

## Fastest supported integration
Prefer Printify's native WooCommerce connection rather than building a parallel custom order-submission bridge. Official instructions:
- https://help.printify.com/hc/en-us/articles/4483637152401-How-can-I-connect-my-WooCommerce-store-to-Printify
- https://printify.com/woocommerce/

## Store connection checklist
1. In WordPress, verify the canonical public site URL in Settings → General. Use the exact public site URL shown by Visit Site; do not add /shop or a page path.
2. In WordPress, go to Settings → Permalinks. Choose any option other than Plain and save.
3. In WooCommerce, review Settings → Advanced and follow Printify's current instructions for the legacy REST API. Do not enable deprecated APIs unless the official guide specifically requires it for the current connection.
4. In Printify, open Manage my stores → Connect/Add a new store → WooCommerce and enter the exact canonical site URL.
5. Install Printify's official WooCommerce shipping plugin if required by the current Printify setup, then configure and test shipping.
6. Publish one simple, mapped product from Printify into WooCommerce. Verify variants, retail price, product images, shipping settings and stock/availability.
7. Keep the store in Coming Soon/private mode until checkout and fulfilment tests pass.
8. Place a controlled test order using the supported test path. Verify it appears in Printify, shipping and production costs are understood, and production/fulfilment status is visible.
9. Before opening sales, verify live payment mode, refund handling, taxes, shipping rates, customer emails, privacy/returns policy and support contact.

## Credential safety
The native Printify ↔ WooCommerce integration normally uses the account connection flow and does not require pasting a Printify API token into a public website field. If a custom API integration is later required, store the Printify personal access token only in the server-side secret manager/environment. Never commit it to GitHub or paste it into WordPress page content.

## Launch status
A GitHub repository change cannot connect the Printify account to WordPress, publish products into the account, change WordPress settings, take payments, or verify a real order. The launch is only complete after the WordPress/Printify connection and end-to-end order are verified.
