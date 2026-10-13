# SUPREME QIKINK WooCommerce Bridge

This plugin is a guarded integration between WooCommerce and Qikink's Open API. It is deliberately disabled until an administrator adds server-side constants and enables it. It does not configure payment gateways, create Qikink products, or activate the WordPress store.

## Important limitations

- The initial bridge submits **paid WooCommerce orders only** and is restricted to Indian shipping addresses in live mode.
- Every product or variation must have an exact Qikink SKU saved in its product data.
- If you use a design supplied through the Qikink "My Products" catalogue, leave all optional design fields empty. If using a custom design API flow, supply the design code, publicly accessible HTTPS design and mockup URLs, placement SKU, and positive width/height in inches.
- COD is not enabled by this initial bridge. Do not enable COD checkout expecting automatic Qikink submission.
- The plugin atomically claims an order by adding its `submitting` status before sending the supplier request, preventing concurrent payment-complete hooks from both submitting the same order. It intentionally does not automatically retry ambiguous failures. Check Qikink's dashboard before any manual recovery.
- The integration must first be tested with Qikink Sandbox credentials. Qikink may require sandbox test orders and approval before issuing Live API access.
- No live order is sent unless `SUPREME_QIKINK_ENABLE_ORDERS` is explicitly set to boolean `true`.

## Configure credentials securely

Do not add credentials to GitHub source, a WordPress page, shortcode, or frontend JavaScript. Add constants to the private `wp-config.php` on the WordPress server, above the line that says to stop editing. Use the Sandbox credentials first:

```php
define('SUPREME_QIKINK_ENV', 'sandbox'); // 'sandbox' or 'live'
define('SUPREME_QIKINK_CLIENT_ID', 'YOUR_QIKINK_CLIENT_ID');
define('SUPREME_QIKINK_CLIENT_SECRET', 'YOUR_QIKINK_SANDBOX_SECRET');
define('SUPREME_QIKINK_ENABLE_ORDERS', false); // keep false until mappings and tests are complete
```

After Qikink confirms live API access, replace the secret with the **Live** secret, change the environment to `live`, and enable orders only after a successful sandbox verification and an intentional production go-live decision:

```php
define('SUPREME_QIKINK_ENV', 'live');
define('SUPREME_QIKINK_CLIENT_ID', 'YOUR_LIVE_QIKINK_CLIENT_ID');
define('SUPREME_QIKINK_CLIENT_SECRET', 'YOUR_LIVE_QIKINK_CLIENT_SECRET');
define('SUPREME_QIKINK_ENABLE_ORDERS', true);
```

Never commit real values. Rotate any credential accidentally exposed in chat, logs, screenshots, or source control.

## Install

1. Download the plugin directory or package it as a ZIP with this folder at the ZIP root:
   `supreme-qikink-woocommerce-bridge/supreme-qikink-woocommerce-bridge.php`
2. In WordPress Admin, open **Plugins → Add New Plugin → Upload Plugin**, upload the ZIP, and activate it.
3. Confirm WooCommerce is active and the configuration notice is shown while the bridge remains disabled.
4. Open each simple product's **Product data → Inventory → Qikink fulfilment mapping** fields. For variable products, fill the Qikink fields on each variation.
5. Use an exact SKU from Qikink's product catalogue. Do not map the illustrative SUPREME catalog SKUs such as `POD-TEE` unless Qikink actually recognizes them.
6. Test a sandbox checkout with a small, controlled order. Verify that the order is paid in WooCommerce and that the matching test order appears in Qikink Sandbox.
7. Review WooCommerce order notes and the Qikink status displayed on the order details page.
8. Request and receive Live API approval from Qikink before changing the environment to `live`.

## Order safety

- The bridge listens to WooCommerce's `woocommerce_payment_complete` hook and verifies `$order->is_paid()`.
- It sends the supplier order only after payment confirmation.
- The generated Qikink order number is alphanumeric and limited to 15 characters.
- A submission error is recorded in the order note and no automatic retry is attempted because a network timeout can occur after the supplier has already accepted the order.
- If a request fails or times out, inspect Qikink's dashboard before taking recovery action. Do not blindly resubmit the same purchase.
- Run a real low-value production test only after the site is publicly accessible, checkout/webhooks are verified, prices and shipping are correct, and the Qikink Live API credentials are approved.

## Known next steps before public launch

- Add a supported manual recovery/reconciliation workflow for ambiguous API failures.
- Confirm Qikink's current token and order endpoint fields with Qikink support; API docs and account access may vary.
- Verify live product SKU/variant mapping, shipping fees, tax disclosures, returns policy, customer email notifications, and refund procedure.
- Run an end-to-end test from customer checkout through Qikink acceptance and tracking. A green GitHub build alone is not a live-store test.
