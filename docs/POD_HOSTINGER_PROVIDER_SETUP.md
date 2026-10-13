# SUPREME POD plugins: Hostinger deployment and provider connection

This setup has three separate layers: GitHub deploys SUPREME-owned plugin files; WordPress connects to each provider; provider accounts handle product publishing and fulfilment.

## GitHub → Hostinger (one-time)

Under **Repository → Settings → Secrets and variables → Actions**, use the `production` environment.

Secrets (never paste passwords in chat):
- `HOSTINGER_FTP_SERVER`: `147.93.17.121` (hostname/IP only, no `ftp://`)
- `HOSTINGER_FTP_USERNAME`: `u664492673`
- `HOSTINGER_FTP_PASSWORD`: the FTP password set in Hostinger hPanel

Variables:
- `HOSTINGER_POD_PLUGIN_DIR`: `public_html/wp-content/plugins/supreme-print-on-demand/`
- `HOSTINGER_QIKINK_BRIDGE_DIR`: `public_html/wp-content/plugins/supreme-qikink-woocommerce-bridge/`

The hPanel shows `public_html` as the upload folder. Before first deployment, confirm the FTP account maps that relative path to this domain's WordPress install. Do not use the absolute `/home/u664492673/...` filesystem path as the FTP path.

The workflow validates PHP syntax and deploys only these two SUPREME-owned plugin directories. It does not install or activate plugins, configure provider accounts, publish products, or enable Qikink order submission. Remote cleanup is disabled.

## Printify → WooCommerce

1. In WordPress, Settings → Permalinks; choose anything except Plain and save.
2. In Printify, Manage my stores → Connect/Add new store → WooCommerce.
3. Enter the canonical website URL exactly as WordPress Settings → General / Visit Site shows (no `/shop` or page path) and approve the connection.
4. Install/activate Printify for WooCommerce shipping plugin only if required by Printify's current instructions. Check currency: Printify shipping rates are USD; for a non-USD WooCommerce store, use an explicitly configured shipping strategy rather than assuming conversion.
5. Publish one test product from Printify. Check product, variants, images, price, shipping and order sync before opening the store.

Official guide: https://help.printify.com/hc/en-us/articles/4483637152401-How-can-I-connect-my-WooCommerce-store-to-Printify

## Qikink → WooCommerce

1. In the Qikink seller dashboard, open Integrations → WooCommerce and start the connection.
2. Follow the official plugin install/auth flow, enter the Qikink account username/email, verify OTP and approve WooCommerce access.
3. Confirm the store is listed as connected in Qikink. Push one product and verify size/color variants and SKU.
4. Keep the custom SUPREME Qikink bridge disabled until sandbox tests, exact Qikink SKU/design/placement mapping, and provider order payload requirements are verified. Never enable live order submission just to test connectivity.

Official guide: https://qikink.com/help/integrations/integrating-your-woocommerce-store/

## Launch gate

Keep the WooCommerce store in Coming Soon/private mode until both provider connections, products, shipping, taxes, payment, customer emails, refunds/returns, and end-to-end test orders are verified. A successful GitHub upload alone is not a live POD integration. Never store provider tokens or passwords in source code.
