"""Index of documented third-party provider integrations involving Cloudflare.

This is a catalog, not a connector: no credentials are loaded and no connection
is made. Keep only provider integrations supported by a specific official source.
"""
CLOUDFLARE_PROVIDER_INTEGRATIONS = {
    "provider_id": "cloudflare",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "provider_modules": {
        "aws": "aws_cloudflare_api_ecosystem.py",
        "google_cloud": "google_cloud_cloudflare_api_ecosystem.py",
        "microsoft_azure": "microsoft_azure_cloudflare_api_ecosystem.py",
        "oracle_cloud": "oracle_cloud_cloudflare_api_ecosystem.py",
        "alibaba_cloud": "alibaba_cloud_cloudflare_api_ecosystem.py",
    },
    "documented_integration_areas": [
        {
            "name": "Cloudflare Multi-Cloud Networking",
            "providers": ["AWS", "Google Cloud", "Microsoft Azure"],
            "official_documentation": "https://developers.cloudflare.com/multi-cloud-networking/get-started/",
            "status": "CLOSED_BETA_PER_OFFICIAL_DOCS",
        },
        {
            "name": "Cloud Connector",
            "providers": ["AWS S3", "Google Cloud Storage", "Azure Blob Storage", "Oracle Cloud Object Storage"],
            "official_documentation": "https://developers.cloudflare.com/rules/cloud-connector/providers/",
            "status": "DOCUMENTED",
        },
        {
            "name": "Cloudflare partner integrations",
            "providers": ["Alibaba Cloud", "Google Cloud", "Microsoft Azure", "Oracle Cloud"],
            "official_documentation": "https://developers.cloudflare.com/fundamentals/reference/partners/",
            "status": "DOCUMENTED_PARTNER_REFERENCE",
        },
        {
            "name": "Cloudflare AI Gateway provider endpoints",
            "providers": ["AWS Bedrock", "Google AI Studio", "Azure OpenAI"],
            "official_documentation": "https://developers.cloudflare.com/ai-gateway/get-started/",
            "status": "DOCUMENTED",
        },
    ],
    "security_note": "Use least-privilege credentials in environment variables or a managed secret store; never commit credentials.",
}
