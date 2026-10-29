"""Catalog entry: Cloudflare integrations with Microsoft Azure."""
MICROSOFT_AZURE_CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "microsoft_azure",
    "provider_name": "Microsoft Azure",
    "ecosystem_name": "MICROSOFT AZURE CLOUDFLARE API ECOSYSTEM",
    "integration_owner": "Cloudflare exposes the integration; Microsoft Azure remains the cloud provider",
    "integration_areas": [
        {"name": "Cloudflare Multi-Cloud Networking", "status": "CLOSED_BETA_PER_OFFICIAL_DOCS", "purpose": "Discover/connect Azure virtual networks and cloud resources"},
        {"name": "Cloud Connector", "status": "DOCUMENTED", "purpose": "Cloudflare rules can target supported Azure Blob Storage origins"},
        {"name": "Cloudflare Logpush", "status": "DOCUMENTED", "purpose": "Send supported Cloudflare logs to Microsoft Azure"},
        {"name": "Cloudflare WAN", "status": "DOCUMENTED", "purpose": "Network connectivity integration with Microsoft Azure"},
        {"name": "AI Gateway", "status": "DOCUMENTED", "purpose": "Use Azure OpenAI as a supported AI provider endpoint"},
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