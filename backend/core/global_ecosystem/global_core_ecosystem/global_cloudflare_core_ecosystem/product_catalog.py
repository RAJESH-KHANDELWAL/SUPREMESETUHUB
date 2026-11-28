"""Canonical Cloudflare product and directory inventory.

Only Cloudflare-owned product families are exposed as products. Existing
third-party/affiliate placeholders are retained as directory records and are
explicitly excluded from the Cloudflare product registry.
"""
from __future__ import annotations

from typing import Any

ECOSYSTEM_ID = "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM"
PROVIDER = "cloudflare"

# (directory, product_id, display_name, domain_id, status)
_PRODUCTS = (
    ("access_zero_trust_cloudflare_core_ecosystem", "access_zero_trust", "Cloudflare Access", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("accounts_cloudflare_core_ecosystem", "accounts", "Cloudflare Accounts", "GOVERNANCE_IDENTITY", "DIRECTORY_PLACEHOLDER"),
    ("agents_cloudflare_core_ecosystem", "agents", "Cloudflare Agents", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("ai_gateway_cloudflare_core_ecosystem", "ai_gateway", "AI Gateway", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("ai_gateway_controls_cloudflare_core_ecosystem", "ai_gateway_controls", "AI Gateway Controls", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("ai_search_cloudflare_core_ecosystem", "ai_search", "AI Search", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("analytics_logpush_cloudflare_core_ecosystem", "analytics_logpush", "Logpush", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("api_shield_cloudflare_core_ecosystem", "api_shield", "API Shield", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("argo_smart_routing_cloudflare_core_ecosystem", "argo_smart_routing", "Argo Smart Routing", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("audit_logs_cloudflare_core_ecosystem", "audit_logs", "Audit Logs", "GOVERNANCE_IDENTITY", "DIRECTORY_PLACEHOLDER"),
    ("bot_management_cloudflare_core_ecosystem", "bot_management", "Bot Management", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("browser_isolation_cloudflare_core_ecosystem", "browser_isolation", "Browser Isolation", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("browser_run_cloudflare_core_ecosystem", "browser_run", "Browser Rendering", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("cache_cloudflare_core_ecosystem", "cache", "Cache", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("cloudflare_mesh_cloudflare_core_ecosystem", "cloudflare_mesh", "Cloudflare Mesh", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("cloudflare_one_cloudflare_core_ecosystem", "cloudflare_one", "Cloudflare One", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("containers_artifacts_cloudflare_core_ecosystem", "containers_artifacts", "Container Artifacts", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("containers_cloudflare_core_ecosystem", "containers", "Containers", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("d1_cloudflare_core_ecosystem", "d1", "D1 Database", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("data_localization_cloudflare_core_ecosystem", "data_localization", "Data Localization", "GOVERNANCE_IDENTITY", "DIRECTORY_PLACEHOLDER"),
    ("data_loss_prevention_cloudflare_core_ecosystem", "data_loss_prevention", "Data Loss Prevention", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("dns_cloudflare_core_ecosystem", "dns", "Cloudflare DNS", "DNS_DOMAIN_REGISTRY", "DIRECTORY_PLACEHOLDER"),
    ("dns_firewall_cloudflare_core_ecosystem", "dns_firewall", "DNS Firewall", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("durable_objects_cloudflare_core_ecosystem", "durable_objects", "Durable Objects", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("email_routing_cloudflare_core_ecosystem", "email_routing", "Email Routing", "EMAIL_SERVICES", "DIRECTORY_PLACEHOLDER"),
    ("email_security_cloudflare_core_ecosystem", "email_security", "Email Security", "EMAIL_SERVICES", "DIRECTORY_PLACEHOLDER"),
    ("email_service_cloudflare_core_ecosystem", "email_service", "Email Service", "EMAIL_SERVICES", "DIRECTORY_PLACEHOLDER"),
    ("gateway_zero_trust_cloudflare_core_ecosystem", "gateway_zero_trust", "Gateway", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("graph_ql_analytics_cloudflare_core_ecosystem", "graphql_analytics", "GraphQL Analytics", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("health_checks_cloudflare_core_ecosystem", "health_checks", "Health Checks", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("hyperdrive_cloudflare_core_ecosystem", "hyperdrive", "Hyperdrive", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("images_cloudflare_core_ecosystem", "images", "Cloudflare Images", "MEDIA_DELIVERY", "DIRECTORY_PLACEHOLDER"),
    ("k2_event_streams_cloudflare_core_ecosystem", "k2_event_streams", "Event Streams", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("kv_cloudflare_core_ecosystem", "kv", "Workers KV", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("load_balancing_cloudflare_core_ecosystem", "load_balancing", "Load Balancing", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("log_explorer_cloudflare_core_ecosystem", "log_explorer", "Log Explorer", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("magic_transit_cloudflare_core_ecosystem", "magic_transit", "Magic Transit", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("magic_wan_cloudflare_core_ecosystem", "magic_wan", "Magic WAN", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("network_firewall_cloudflare_core_ecosystem", "network_firewall", "Network Firewall", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("network_interconnect_cloudflare_core_ecosystem", "network_interconnect", "Network Interconnect", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("pages_cloudflare_core_ecosystem", "pages", "Cloudflare Pages", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("pages_functions_cloudflare_core_ecosystem", "pages_functions", "Pages Functions", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("queues_cloudflare_core_ecosystem", "queues", "Queues", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("r2_cloudflare_core_ecosystem", "r2", "R2 Object Storage", "DATA_STORAGE_MESSAGING", "DIRECTORY_PLACEHOLDER"),
    ("rate_limiting_cloudflare_core_ecosystem", "rate_limiting", "Rate Limiting", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("realtime_cloudflare_core_ecosystem", "realtime", "Cloudflare Realtime", "MEDIA_DELIVERY", "DIRECTORY_PLACEHOLDER"),
    ("registrar_cloudflare_core_ecosystem", "registrar", "Cloudflare Registrar", "DNS_DOMAIN_REGISTRY", "DIRECTORY_PLACEHOLDER"),
    ("security_cloudflare_core_ecosystem", "security", "Security Center", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("spectrum_cloudflare_core_ecosystem", "spectrum", "Spectrum", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("ssl_certificates_cloudflare_core_ecosystem", "ssl_certificates", "SSL Certificates", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("ssl_tls_cloudflare_core_ecosystem", "ssl_tls", "SSL/TLS", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("stream_cloudflare_core_ecosystem", "stream", "Cloudflare Stream", "MEDIA_DELIVERY", "DIRECTORY_PLACEHOLDER"),
    ("time_services_cloudflare_core_ecosystem", "time_services", "Time Services", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("tunnel_cloudflare_core_ecosystem", "tunnel", "Cloudflare Tunnel", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("turn_service_cloudflare_core_ecosystem", "turn_service", "TURN Service", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("turnstile_cloudflare_core_ecosystem", "turnstile", "Turnstile", "APPLICATION_SECURITY", "DIRECTORY_PLACEHOLDER"),
    ("vectorize_cloudflare_core_ecosystem", "vectorize", "Vectorize", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("waiting_room_cloudflare_core_ecosystem", "waiting_room", "Waiting Room", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("warp_cloudflare_core_ecosystem", "warp", "WARP", "ZERO_TRUST_ACCESS", "DIRECTORY_PLACEHOLDER"),
    ("web3_gateways_cloudflare_core_ecosystem", "web3_gateways", "Web3 Gateways", "NETWORK_EDGE", "DIRECTORY_PLACEHOLDER"),
    ("web_analytics_cloudflare_core_ecosystem", "web_analytics", "Web Analytics", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("workers_ai_cloudflare_core_ecosystem", "workers_ai", "Workers AI", "AI_DEVELOPER_PLATFORM", "DIRECTORY_PLACEHOLDER"),
    ("workers_cloudflare_core_ecosystem", "workers", "Cloudflare Workers", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("workers_for_platforms_cloudflare_core_ecosystem", "workers_for_platforms", "Workers for Platforms", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("workers_observability_cloudflare_core_ecosystem", "workers_observability", "Workers Observability", "OBSERVABILITY_ANALYTICS", "DIRECTORY_PLACEHOLDER"),
    ("workflows_cloudflare_core_ecosystem", "workflows", "Workflows", "DEVELOPER_COMPUTE", "DIRECTORY_PLACEHOLDER"),
    ("zones_cloudflare_core_ecosystem", "zones", "Zones", "DNS_DOMAIN_REGISTRY", "DIRECTORY_PLACEHOLDER"),
)

# Existing folders that are not Cloudflare product names. They are preserved
# for audit; no product/API capability is inferred from their presence.
_EXTERNAL_OR_UNVERIFIED = (
    "abelohost_cloudflare_core_ecosystem", "basin_cloudflare_core_ecosystem",
    "bangbros_cloudflare_core_ecosystem", "brazzers_cloudflare_core_ecosystem",
    "ccbill_cloudflare_core_ecosystem", "clips4sale_cloudflare_core_ecosystem",
    "crakrevenue_cloudflare_core_ecosystem", "epoch_cloudflare_core_ecosystem",
    "evilangel_cloudflare_core_ecosystem", "exoclick_cloudflare_core_ecosystem",
    "fansly_cloudflare_core_ecosystem", "faphouse_cloudflare_core_ecosystem",
    "loyalfans_cloudflare_core_ecosystem", "manyvids_cloudflare_core_ecosystem",
    "naughtyamerica_cloudflare_core_ecosystem", "nsfwinfra_cloudflare_core_ecosystem",
    "onlyfans_cloudflare_core_ecosystem", "paxum_cloudflare_core_ecosystem",
    "pornhub_cloudflare_core_ecosystem", "realitykings_cloudflare_core_ecosystem",
    "segpay_cloudflare_core_ecosystem",
)

def list_products() -> list[dict[str, Any]]:
    return [
        {"product_id": pid, "name": name, "provider": PROVIDER,
         "domain_id": domain, "directory": directory, "status": status,
         "implemented": False, "live_connection_verified": False}
        for directory, pid, name, domain, status in _PRODUCTS
    ]

def list_directory_audit() -> list[dict[str, str]]:
    products = {row[0] for row in _PRODUCTS}
    return (
        [{"directory": name, "classification": "CLOUDFLARE_PRODUCT_PLACEHOLDER"}
         for name in sorted(products)]
        + [{"directory": name, "classification": "EXTERNAL_OR_UNVERIFIED_PLACEHOLDER"}
           for name in _EXTERNAL_OR_UNVERIFIED]
        + [{"directory": "catalog_cloudflare_core_ecosystem",
            "classification": "CORE_CATALOG_PACKAGE"}]
    )

def get_product(product_id: str) -> dict[str, Any] | None:
    needle = product_id.strip().casefold()
    if not needle:
        return None
    return next((item for item in list_products()
                 if item["product_id"].casefold() == needle
                 or item["name"].casefold() == needle
                 or item["directory"].casefold() == needle), None)

def product_summary() -> dict[str, Any]:
    products = list_products()
    audit = list_directory_audit()
    return {"success": True, "provider": PROVIDER,
            "product_count": len(products), "directory_audit_count": len(audit),
            "products": products, "directory_audit": audit}
