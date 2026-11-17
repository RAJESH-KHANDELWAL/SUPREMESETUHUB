"""Cloudflare GraphQL Analytics API API catalog metadata; no live requests are made here."""

CLOUDFLARE_PRODUCT = {
    "provider_id": "cloudflare",
    "product_id": "graph_ql_analytics",
    "name": "GraphQL Analytics API",
    "scope": "Analytics queries for Cloudflare traffic and products",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "official_documentation": "https://developers.cloudflare.com/analytics/graphql-api/",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "credentials": "Use least-privilege API tokens from environment variables or a managed secret store.",
}
