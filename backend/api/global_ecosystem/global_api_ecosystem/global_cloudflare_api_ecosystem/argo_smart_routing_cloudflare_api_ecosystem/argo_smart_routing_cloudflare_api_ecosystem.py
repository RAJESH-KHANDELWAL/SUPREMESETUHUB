"""Cloudflare Argo Smart Routing API catalog metadata; no live requests are made here."""

CLOUDFLARE_PRODUCT = {
    "provider_id": "cloudflare",
    "product_id": "argo_smart_routing",
    "name": "Argo Smart Routing",
    "scope": "Intelligent traffic routing",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_documentation": "https://developers.cloudflare.com/argo-smart-routing/",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "credentials": "Use least-privilege API tokens from environment variables or a managed secret store.",
}
