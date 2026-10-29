"""Index of documented third-party cloud/provider integration areas for Cloudflare.

This catalog does not create connections or imply that credentials are configured.
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
        "apple": "apple_cloudflare_api_ecosystem.py",
    },
    "verified_documentation_scope": [
        "Cloudflare Multi-Cloud Networking docs list AWS, Google Cloud, and Azure integrations; feature is currently described as closed beta.",
        "Cloud Connector docs list Cloudflare R2, AWS S3, Google Cloud Storage, Azure Blob Storage, and Oracle Cloud Object Storage.",
        "Cloudflare partner docs list additional network/logging integrations including Alibaba Cloud VPN Gateway, Google Cloud VPN, Microsoft Azure, and Oracle Cloud.",
        "Cloudflare AI Gateway docs list AWS Bedrock, Google AI Studio, and Azure OpenAI among supported provider endpoints.",
    ],
    "security_note": "Keep provider credentials in environment variables or a managed secret store; never commit credentials.",
}