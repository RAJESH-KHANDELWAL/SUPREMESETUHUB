# META ECOSYSTEM

Canonical hierarchy: `backend/global_ecosystem/meta_ecosystem/`

This namespace/catalog scaffold follows the Google ecosystem layout. Each product has an independent namespace directory.

## Architecture boundaries

- This layer owns global Meta product namespaces and the catalog.
- CORE, API, ENGINE, DATABASE, credentials, and runtime implementations remain in their separately owned architecture layers.
- No CORE/API/ENGINE/DATABASE implementation is copied into these namespace folders.
- Namespace presence does not claim a working integration, authentication, or production readiness.

## Product namespaces

- `meta_facebook_ecosystem/`
- `meta_instagram_ecosystem/`
- `meta_whatsapp_ecosystem/`
- `meta_messenger_ecosystem/`
- `meta_threads_ecosystem/`
- `meta_meta_business_suite_ecosystem/`
- `meta_meta_ads_ecosystem/`
- `meta_meta_pixel_ecosystem/`
- `meta_conversions_api_ecosystem/`
- `meta_meta_business_manager_ecosystem/`
- `meta_meta_commerce_manager_ecosystem/`
- `meta_meta_pages_ecosystem/`
- `meta_meta_groups_ecosystem/`
- `meta_meta_events_ecosystem/`
- `meta_meta_developer_platform_ecosystem/`
- `meta_meta_graph_api_ecosystem/`
- `meta_meta_webhooks_ecosystem/`
- `meta_meta_login_ecosystem/`
- `meta_meta_app_events_ecosystem/`
- `meta_meta_horizon_ecosystem/`
