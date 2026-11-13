# SUPREMESETUHUB — MAIN BASE FOUNDATION WordPress Plugin

This is the single branded WordPress plugin used by both official WordPress installations.

- Plugin name: **SUPREMESETUHUB**
- Central system: **MAIN BASE FOUNDATION**
- Source of truth: this repository's `wordpress-plugin/supremesetuhub-connector/` directory
- Install the same plugin package on both websites; configure each site's API base URL independently.
- Each WordPress site keeps its own users, settings, content, and database. This plugin does not merge or migrate site databases.

## Installation

1. In WordPress Admin, open **Plugins → Add New Plugin → Upload Plugin**.
2. Upload the generated `supremesetuhub.zip` package and activate it.
3. Open **Settings → SUPREMESETUHUB**.
4. Set the public HTTPS API base URL for the MAIN BASE FOUNDATION deployment.
5. Save, then use **Test Backend Connection**.

## Available shortcodes

- `[supremesetuhub_status]`
- `[supremesetuhub_pod_catalog market="IN"]`
- `[supremesetuhub_digital_catalog market="IN" limit="24"]`
- `[supreme_ecosystem_home]`
- `[supreme_snippet_home]`
- `[supreme_global_business_ecosystem]`
- `[supreme_contact]`
- `[supreme_youtag_wellness]`
- `[supreme_bada_business]`
- `[supreme_print_on_demand]`
- `[supreme_backend_status]`

Catalog output is informational. Payment, checkout, fulfilment, and paid-download delivery require separate integrations and must not be assumed active.

## Deployment

The repository's Hostinger workflow deploys this same plugin source to both configured plugin directories. The second target must be configured as the protected GitHub Environment variable `HOSTINGER_WP_PLUGIN_DIR_IBC`; never guess the path.
