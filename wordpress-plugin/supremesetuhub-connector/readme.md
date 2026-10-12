# SUPREMESETUHUB Connector for WordPress

A WordPress plugin that connects a WordPress storefront to the deployed SUPREMESETUHUB FastAPI backend using server-side HTTPS requests.

## Install
1. Copy the `supremesetuhub-connector` directory into `wp-content/plugins/` or package this directory as a ZIP.
2. In WordPress Admin → Plugins, activate **SUPREMESETUHUB Connector**.
3. Open Settings → SUPREMESETUHUB and set the deployed backend API base URL (for example, `https://api.example.com`). Do not use a guessed URL; use the URL that actually serves the FastAPI `/health` endpoint.
4. Save, then use **Test Backend Connection**.
5. Add one of these shortcodes to a WordPress page:
   - `[supremesetuhub_status]`
   - `[supremesetuhub_pod_catalog market="IN"]`
   - `[supremesetuhub_digital_catalog market="IN"]`

## Current boundaries
- POD pricing and supplier costs are estimates; this is not a live fulfillment-provider quote.
- Digital catalog shows only designs published in the backend database.
- Payment checkout, order creation, print-provider fulfillment, and private download delivery are not implemented by this plugin.
- Do not paste hosting passwords, SSH keys, payment secrets, or database credentials into WordPress page content or shortcode attributes.
- The connector uses public read-only API routes only and caches catalog responses for five minutes.

## Backend endpoint requirements
- `GET /health`
- `GET /api/v1/print-on-demand/public/catalog?market=IN`
- `GET /api/v1/digital-marketplace/catalog?market=IN&limit=24`

The backend must be deployed and reachable over HTTPS before this plugin can connect.
