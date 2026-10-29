"""Catalog entry: Cloudflare integrations with Google Cloud Platform (GCP)."""
GOOGLE_CLOUD_CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "google_cloud",
    "provider_name": "Google Cloud Platform",
    "ecosystem_name": "GOOGLE CLOUD CLOUDFLARE API ECOSYSTEM",
    "integration_owner": "Cloudflare exposes the integration; Google Cloud remains the cloud provider",
    "integration_areas": [
        {"name": "Cloudflare Multi-Cloud Networking", "status": "CLOSED_BETA_PER_OFFICIAL_DOCS", "purpose": "Discover/connect Google Cloud VPC and network resources"},
        {"name": "Cloud Connector", "status": "DOCUMENTED", "purpose": "Cloudflare rules can target supported Google Cloud Storage origins"},
        {"name": "Cloudflare Logpush", "status": "DOCUMENTED", "purpose": "Send supported Cloudflare logs to Google Cloud Storage or BigQuery"},
        {"name": "Cloudflare WAN", "status": "DOCUMENTED", "purpose": "Network connectivity integration with Google Cloud VPN"},
        {"name": "AI Gateway", "status": "DOCUMENTED", "purpose": "Use Google AI Studio/Gemini as a supported AI provider endpoint"},
    ],
    "official_documentation": [
        "https://developers.cloudflare.com/multi-cloud-networking/get-started/",
        "https://developers.cloudflare.com/rules/cloud-connector/providers/",
        "https://developers.cloudflare.com/fundamentals/reference/partners/",
        "https://developers.cloudflare.com/ai-gateway/get-started/",
    ],
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
}