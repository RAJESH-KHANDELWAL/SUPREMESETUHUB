"""Cloudflare product and capability catalog; metadata is not proof of live access."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

CLOUDFLARE_CAPABILITIES: dict[str, tuple[str, ...]] = {
    "connectivity": ("authoritative_dns", "domain_registration", "proxy_and_load_balancing"),
    "performance": ("cdn", "cache_rules", "image_optimization", "tiered_cache"),
    "application_delivery": ("workers", "pages", "durable_objects", "queues", "workflows"),
    "storage": ("r2_object_storage", "kv_storage", "d1_sql_database", "hyperdrive"),
    "networking": ("zero_trust_networking", "tunnels", "private_networking", "spectrum"),
    "security": ("web_application_firewall", "ddos_protection", "bot_management", "rate_limiting"),
    "identity_access": ("access_policies", "service_tokens", "identity_provider_integrations"),
    "observability": ("analytics", "logs", "health_checks", "alerts"),
    "email": ("email_routing",),
    "developer_platform": ("api_tokens", "account_and_zone_apis", "terraform_provider"),
}
_PRODUCTS: tuple[dict[str, Any], ...] = (
    {"id":"dns","name":"Cloudflare DNS","category":"connectivity","capabilities":("authoritative_dns",)},
    {"id":"cdn","name":"Cloudflare CDN","category":"performance","capabilities":("cdn","cache_rules")},
    {"id":"workers","name":"Cloudflare Workers","category":"application_delivery","capabilities":("workers","durable_objects","queues","workflows")},
    {"id":"pages","name":"Cloudflare Pages","category":"application_delivery","capabilities":("pages",)},
    {"id":"r2","name":"Cloudflare R2","category":"storage","capabilities":("r2_object_storage",)},
    {"id":"kv","name":"Workers KV","category":"storage","capabilities":("kv_storage",)},
    {"id":"d1","name":"Cloudflare D1","category":"storage","capabilities":("d1_sql_database",)},
    {"id":"zero_trust","name":"Cloudflare Zero Trust","category":"networking","capabilities":("zero_trust_networking","tunnels","access_policies")},
    {"id":"waf","name":"Web Application Firewall","category":"security","capabilities":("web_application_firewall","rate_limiting")},
    {"id":"api","name":"Cloudflare API","category":"developer_platform","capabilities":("account_and_zone_apis","api_tokens")},
)
def get_cloudflare_catalog() -> dict[str, Any]:
    """Return detached catalog metadata with explicit non-connected status."""
    return {"provider_id":"cloudflare","provider_name":"Cloudflare",
            "provider_type":"edge_network_and_cloud_platform",
            "integration_status":"catalog_only","live_connection_verified":False,
            "capabilities":deepcopy(CLOUDFLARE_CAPABILITIES),
            "products":deepcopy(_PRODUCTS),
            "credential_policy":"Never store API tokens in this package or source control.",
            "runtime_owner":"canonical API/CORE/ENGINE/DATABASE/SECURITY layers"}
def validate_cloudflare_catalog() -> tuple[str, ...]:
    """Validate IDs, category references, and capability references."""
    errors: list[str] = []
    ids=[item["id"] for item in _PRODUCTS]
    if len(ids)!=len(set(ids)): errors.append("duplicate Cloudflare product IDs")
    known={cap for values in CLOUDFLARE_CAPABILITIES.values() for cap in values}
    for item in _PRODUCTS:
        if item["category"] not in CLOUDFLARE_CAPABILITIES: errors.append(f"{item['id']} has unknown category")
        if not item["capabilities"] or not set(item["capabilities"]).issubset(known): errors.append(f"{item['id']} has unknown capabilities")
    return tuple(errors)
__all__=["CLOUDFLARE_CAPABILITIES","get_cloudflare_catalog","validate_cloudflare_catalog"]
