# WordPress Fluent Snippet / SUPREME ECOSYSTEM Bridge

## What this integration does

- The FastAPI service already serves the main frontend from `frontend/index.html` at `/`.
- It already serves the personal SUPREME frontend from `frontend/supreme/index.html` at `/api/v1/frontend/supreme`.
- This change adds public aliases `/api/v1/frontend/global-business-ecosystem` and `/api/v1/frontend/global-business-ecosystem/health` for the main ecosystem page so WordPress can embed it explicitly.
- The separately packaged **SUPREMESETUHUB Ecosystem Bridge** WordPress plugin contains the user's provided Fluent Snippets HTML/CSS as isolated assets and offers shortcodes for Home, Global Business Ecosystem, Contact, YOUTAG WELLNESS, Bada Business, POD catalog and backend health.

## WordPress plugin setup

Install `supremesetuhub-ecosystem-bridge.zip` through WordPress Admin → Plugins → Add New Plugin → Upload Plugin, then activate it. Open Settings → SUPREMESETUHUB Bridge and set the deployed FastAPI HTTPS base URL.

Shortcodes:
- `[supreme_ecosystem_home]` — embeds the backend-served global ecosystem homepage.
- `[supreme_snippet_home]` — imported Home snippet.
- `[supreme_global_business_ecosystem]` — imported global business ecosystem snippet.
- `[supreme_contact]`
- `[supreme_youtag_wellness]`
- `[supreme_bada_business]`
- `[supreme_pod_catalog market="IN"]`
- `[supreme_backend_status]`

## Security and launch limitations

The Fluent Snippets export's generated `index.php`, `.htaccess`, and secret-type configuration value are not copied into the plugin. The stale nested Home fetch was removed to avoid recursive/duplicate homepage loading. Imported snippets render directly in the page with scoped styles; embedded frames are not used.

POD catalog pricing is indicative only. This plugin does not implement checkout, payment capture, order creation, refunds or supplier fulfilment. Do not accept payments until those flows are implemented and tested. The backend must be deployed and reachable over HTTPS; a GitHub merge alone does not deploy code to Render or install the plugin on Hostinger.
