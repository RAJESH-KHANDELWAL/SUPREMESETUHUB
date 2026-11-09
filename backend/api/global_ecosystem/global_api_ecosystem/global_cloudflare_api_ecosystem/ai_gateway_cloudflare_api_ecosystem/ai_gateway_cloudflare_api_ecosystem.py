"""Cloudflare AI Gateway and Workers AI API catalog metadata; not a live connector."""

CLOUDFLARE_AI_GATEWAY_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "product_area": "AI Gateway and Workers AI",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "scope": "Cloudflare AI Gateway resources and Workers AI inference endpoints.",
    "official_documentation": "https://developers.cloudflare.com/api/resources/ai_gateway/",
    "api_boundary": "/accounts/{account_id}/ai/run/{model_name}",
    "api_base_url": "https://api.cloudflare.com/client/v4",
    "credential_source": "environment_or_managed_secret_store",
}
