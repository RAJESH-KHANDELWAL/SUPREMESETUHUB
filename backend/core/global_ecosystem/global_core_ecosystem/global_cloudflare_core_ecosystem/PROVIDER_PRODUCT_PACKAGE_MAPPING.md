# Cloudflare Core product and legacy-folder mapping

**Canonical source:** `backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py`  
**Core standard:** `google_core_ecosystem/PRODUCT_ECOSYSTEM_STANDARD.md`

## Canonical runtime products

| Runtime product ID | Core package | Existing folder relationship |
|---|---|---|
| `dns` | `dns_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `cdn` | `cdn_cloudflare_core_ecosystem` | New canonical package; `cache` remains an unverified alias candidate |
| `workers` | `workers_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `pages` | `pages_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `r2` | `r2_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `kv` | `kv_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `d1` | `d1_cloudflare_core_ecosystem` | Existing exact-name placeholder, now populated with Core scaffold |
| `zero_trust` | `zero_trust_cloudflare_core_ecosystem` | New canonical package; Access/Gateway/Tunnel folders remain candidates |
| `waf` | `waf_cloudflare_core_ecosystem` | New canonical package; Security/API Shield folders remain candidates |
| `api` | `api_cloudflare_core_ecosystem` | New canonical package; catalog/API-related folders remain candidates |

The mappings above follow the runtime product IDs. A similarly named legacy folder is not assumed to be a complete implementation.

## Legacy and unverified folders

The 89 directories present before this change were all placeholders containing only `.gitkeep`. The following names are preserved. They are not automatically treated as canonical product IDs, provider integrations or completed service modules.

`abelohost`, `access_zero_trust`, `accounts`, `agents`, `ai_gateway`, `ai_gateway_controls`, `ai_search`, `analytics_logpush`, `api_shield`, `argo_smart_routing`, `audit_logs`, `bangbros`, `basin`, `bot_management`, `brazzers`, `browser_isolation`, `browser_run`, `cache`, `catalog`, `ccbill`, `clips4sale`, `cloudflare_mesh`, `cloudflare_one`, `containers_artifacts`, `containers`, `crakrevenue`, `d1`, `data_localization`, `data_loss_prevention`, `dns`, `dns_firewall`, `durable_objects`, `email_routing`, `email_security`, `email_service`, `epoch`, `evilangel`, `exoclick`, `fansly`, `faphouse`, `gateway_zero_trust`, `graph_ql_analytics`, `health_checks`, `hyperdrive`, `images`, `k2_event_streams`, `kv`, `load_balancing`, `log_explorer`, `loyalfans`, `magic_transit`, `magic_wan`, `manyvids`, `naughtyamerica`, `network_firewall`, `network_interconnect`, `nsfwinfra`, `onlyfans`, `pages`, `pages_functions`, `paxum`, `pornhub`, `queues`, `r2`, `rate_limiting`, `realitykings`, `realtime`, `registrar`, `security`, `segpay`, `spectrum`, `ssl_certificates`, `ssl_tls`, `stream`, `time_services`, `tunnel`, `turn_service`, `turnstile`, `vectorize`, `waiting_room`, `warp`, `web3_gateways`, `web_analytics`, `workers_ai`, `workers`, `workers_for_platforms`, `workers_observability`, `workflows`, `zones`.

Some names resemble Cloudflare services/capabilities; others appear to be third-party brands, vendors or platforms. Their exact ownership and intended role require review against official sources and repository references before any migration. No classification here asserts a partnership or Cloudflare affiliation.

## Reconciliation rules

1. Keep the runtime catalog as the sole source of canonical Cloudflare product IDs.
2. Do not register every folder as a product.
3. Review candidate service folders against official Cloudflare documentation before adding them to the runtime catalog.
4. Keep third-party systems in a separately governed integration/workload taxonomy, not as Cloudflare products.
5. Preserve legacy paths until references and ownership are audited.
