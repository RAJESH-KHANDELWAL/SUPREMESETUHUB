"""Catalog entry: Cloudflare integrations with Amazon Web Services (AWS)."""
AWS_CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "aws",
    "provider_name": "Amazon Web Services",
    "ecosystem_name": "AWS CLOUDFLARE API ECOSYSTEM",
    "integration_owner": "Cloudflare exposes the integration; AWS remains the cloud provider",
    "integration_areas": [
        {"name": "Cloudflare Multi-Cloud Networking", "status": "CLOSED_BETA_PER_OFFICIAL_DOCS", "purpose": "Discover/connect AWS VPC and cloud network resources"},
        {"name": "Cloud Connector", "status": "DOCUMENTED", "purpose": "Cloudflare rules can target supported Amazon S3 origins"},
        {"name": "Cloudflare Logpush", "status": "DOCUMENTED", "purpose": "Send supported Cloudflare logs to Amazon S3"},
        {"name": "AI Gateway", "status": "DOCUMENTED", "purpose": "Use AWS Bedrock as a supported AI provider endpoint"},
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