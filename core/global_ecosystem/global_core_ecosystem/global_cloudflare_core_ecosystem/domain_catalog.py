"""Cloudflare domain taxonomy derived from the provider product inventory."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .product_catalog import list_products

DOMAIN_DEFINITIONS = {
    "GOVERNANCE_IDENTITY": {"name": "Governance, Accounts and Identity", "scope": "Account structure, auditability, data location and provider governance."},
    "DNS_DOMAIN_REGISTRY": {"name": "DNS and Domain Registry", "scope": "Zones, DNS records, registrar and domain lifecycle."},
    "NETWORK_EDGE": {"name": "Network, Connectivity and Edge Delivery", "scope": "Routing, connectivity, load balancing, network edge and traffic services."},
    "APPLICATION_SECURITY": {"name": "Application and Network Security", "scope": "Application protection, API security, TLS, bot controls and abuse prevention."},
    "ZERO_TRUST_ACCESS": {"name": "Zero Trust, Access and Secure Connectivity", "scope": "Gateway, WARP, Tunnel, browser isolation and data controls."},
    "DEVELOPER_COMPUTE": {"name": "Developer Platform, Compute and Serverless", "scope": "Workers, Pages, containers, browser rendering and workflows."},
    "DATA_STORAGE_MESSAGING": {"name": "Data, Storage, Databases and Messaging", "scope": "R2, D1, KV, Durable Objects, Queues, Hyperdrive and event streams."},
    "AI_DEVELOPER_PLATFORM": {"name": "AI and Developer Intelligence", "scope": "Workers AI, AI Gateway, AI Search, Vectorize and agent tooling."},
    "OBSERVABILITY_ANALYTICS": {"name": "Observability, Logs and Analytics", "scope": "Health checks, logs, analytics and operational visibility."},
    "MEDIA_DELIVERY": {"name": "Media, Images and Streaming", "scope": "Image transformation, video streaming and media delivery."},
    "EMAIL_SERVICES": {"name": "Email Routing and Security", "scope": "Email routing, sending and email threat protection."},
}
def list_domain_inventory() -> list[dict[str, Any]]:
    counts = Counter(item["domain_id"] for item in list_products())
    return [{"domain_id": key, **value, "product_count": counts.get(key, 0)}
            for key, value in DOMAIN_DEFINITIONS.items()]
def domain_summary() -> dict[str, Any]:
    domains = list_domain_inventory()
    return {"success": True, "domain_count": len(domains),
            "product_count": sum(x["product_count"] for x in domains),
            "domains": domains}
