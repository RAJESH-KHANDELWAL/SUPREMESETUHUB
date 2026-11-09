# BADA BUSINESS CONFIG ECOSYSTEM

Namespaced configuration for Bada Business integrations inside the Global Config Ecosystem.

## Default settings
- `enabled=False`: integration stays disabled until explicitly configured.
- `environment=development`.
- `require_approval=True`.
- `request_timeout_seconds=15` (validated range: 1–120).
- `default_locale=en-IN`.
- `resource_catalog_module=backend.bada_business_ecosystem.platform_resources.catalog`.

Override settings through explicit constructor overrides or `BADA_BUSINESS_*` environment variables. For example, `BADA_BUSINESS_ENABLED` is parsed as the raw string from the environment, so callers should provide boolean overrides directly until a typed environment parser is added. Do not put API keys, passwords, tokens, referral URLs, or secrets in this package. Canonical Bada Business resources and links remain in `backend/bada_business_ecosystem/` and are not duplicated here.

This package defines configuration only; it does not activate integrations or connect to external Bada Business services.
