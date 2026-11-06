"""AWS provider-owned API ecosystem metadata.

Catalog metadata only. This module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_API_ECOSYSTEM = {
    "provider_id": "aws",
    "name": "AWS API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "AWS Management Console", "AWS Marketplace", "AWS Organizations",
        "IAM Identity Center", "AWS Developer Tools"
    ],
    "api_families": [
        "iam_sts", "compute_ec2", "lightsail", "lambda", "containers",
        "s3_storage", "rds_dynamodb", "route53_dns_domains", "vpc_networking",
        "cloudwatch", "cloudtrail", "kms_secrets", "bedrock_sagemaker",
        "billing_cost", "api_gateway", "cloudformation"
    ],
    "related_ecosystems": [
        "AI", "CLOUD", "DATABASE", "DEVELOPER", "DOMAIN", "HOSTING",
        "SECURITY", "SERVER", "STORAGE", "WEB", "WEBSITE"
    ],
    "adapter_path": "backend/integrations/providers/aws.py",
    "credential_source": "iam_role_or_managed_secret_store",
}
