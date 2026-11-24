"""Cloudflare SSL Certificates and Certificate Manager API catalog metadata; no live requests are made here."""

CLOUDFLARE_PRODUCT = {
    "provider_id": "cloudflare",
    "product_id": "ssl_certificates",
    "name": "SSL Certificates and Certificate Manager",
    "scope": "TLS certificate lifecycle management",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_documentation": "https://developers.cloudflare.com/ssl/",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "credentials": "Use least-privilege API tokens from environment variables or a managed secret store.",
}
