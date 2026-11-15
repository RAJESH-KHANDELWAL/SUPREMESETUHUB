"""Cloudflare TURN Service API catalog metadata; no live requests are made here."""

CLOUDFLARE_PRODUCT = {
    "provider_id": "cloudflare",
    "product_id": "turn_service",
    "name": "TURN Service",
    "scope": "Connectivity relay for real-time communication",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_documentation": "https://developers.cloudflare.com/calls/turn/",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "credentials": "Use least-privilege API tokens from environment variables or a managed secret store.",
}
