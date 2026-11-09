# BADA BUSINESS CONFIG ECOSYSTEM

Namespaced configuration for Bada Business integrations inside the Global Config Ecosystem.

## Default settings
- `enabled=False`: integration stays disabled until explicitly configured.
- `environment=development`.
- `require_approval=True`.
- `request_timeout_seconds=15` (validated range: 1–120).
- `default_locale=en-IN`.
- `resource_catalog_module=backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog`.

## Overrides
Use constructor overrides or `BADA_BUSINESS_*` environment variables. Boolean values accept true/false, 1/0, yes/no, and on/off. The timeout is parsed as an integer. Invalid values fail validation. Environment variables take precedence over explicit overrides.

Do not put API keys, passwords, tokens, referral URLs, or secrets in this package. Canonical Bada Business resources and links remain in `backend/global_ecosystem/global_bada_business_ecosystem/` and are not duplicated here.

This package defines configuration only; it does not activate integrations or connect to external Bada Business services.
