"""Machine-readable catalog entry for AWS Bedrock."""

PROVIDER = {
    "id": "aws_bedrock",
    "name": "AWS Bedrock",
    "vendor": "Amazon Web Services",
    "category": "ai_provider",
    "api_endpoint": None,
    "credential_env": "AWS_REGION",
    "models_or_services": ["amazon.nova","anthropic.claude","meta.llama"],
    "integration_status": "scaffold",
    "notes": "Use AWS SDK credential chain and SigV4; do not send AWS credentials as bearer tokens.",
}
