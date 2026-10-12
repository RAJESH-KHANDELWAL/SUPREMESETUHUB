# SUPREME PRINT ON DEMAND

A standalone WordPress plugin that renders the public SUPREMESETUHUB POD catalog using the FastAPI public catalog endpoint.

## Install and configure
1. Upload the packaged ZIP in **WordPress Admin → Plugins → Add New Plugin → Upload Plugin**.
2. Activate **SUPREME PRINT ON DEMAND**.
3. Open **Settings → SUPREME PRINT ON DEMAND** and enter the deployed HTTPS FastAPI base URL, without a trailing slash or endpoint path.
4. Create a WordPress page named **SUPREME PRINT ON DEMAND** and insert this shortcode in a Shortcode block:

```
[supreme_print_on_demand market="IN"]
```

Use `market="GLOBAL"` for the USD market where supported.

## Important
The plugin reads `GET /api/v1/print-on-demand/public/catalog?market=IN`. It displays planning estimates only. It does not take payments, create orders, connect a supplier, or fulfil purchases.
