"""Canonical AWS provider-owned API ecosystem metadata.

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
        "IAM Identity Center", "AWS Developer Tools", "AWS CLI", "AWS SDKs",
    ],
    "api_families": [
        "iam_sts", "compute_ec2", "lightsail", "lambda", "containers",
        "s3_storage", "rds_dynamodb", "route53_dns_domains", "vpc_networking",
        "cloudwatch", "cloudtrail", "kms_secrets", "bedrock_sagemaker",
        "billing_cost", "api_gateway", "cloudformation",
    ],
    "children": [
        {"id": "iam_sts", "name": "AWS IAM AND STS API ECOSYSTEM", "folder": "aws_iam_sts_api_ecosystem", "status": "catalog_only"},
        {"id": "compute_ec2", "name": "AWS EC2 COMPUTE API ECOSYSTEM", "folder": "aws_ec2_compute_api_ecosystem", "status": "catalog_only"},
        {"id": "lightsail", "name": "AWS LIGHTSAIL API ECOSYSTEM", "folder": "aws_lightsail_api_ecosystem", "status": "catalog_only"},
        {"id": "lambda", "name": "AWS LAMBDA API ECOSYSTEM", "folder": "aws_lambda_api_ecosystem", "status": "catalog_only"},
        {"id": "containers", "name": "AWS CONTAINERS API ECOSYSTEM", "folder": "aws_containers_api_ecosystem", "status": "catalog_only"},
        {"id": "s3_storage", "name": "AWS S3 STORAGE API ECOSYSTEM", "folder": "aws_s3_storage_api_ecosystem", "status": "adapter_scaffold"},
        {"id": "rds_dynamodb", "name": "AWS DATABASE API ECOSYSTEM", "folder": "aws_database_api_ecosystem", "status": "catalog_only"},
        {"id": "route53_dns_domains", "name": "AWS ROUTE 53 DNS API ECOSYSTEM", "folder": "aws_route53_dns_api_ecosystem", "status": "catalog_only"},
        {"id": "vpc_networking", "name": "AWS VPC NETWORKING API ECOSYSTEM", "folder": "aws_vpc_networking_api_ecosystem", "status": "catalog_only"},
        {"id": "cloudwatch", "name": "AWS CLOUDWATCH API ECOSYSTEM", "folder": "aws_cloudwatch_api_ecosystem", "status": "adapter_scaffold"},
        {"id": "cloudtrail", "name": "AWS CLOUDTRAIL API ECOSYSTEM", "folder": "aws_cloudtrail_api_ecosystem", "status": "catalog_only"},
        {"id": "kms_secrets", "name": "AWS KMS AND SECRETS API ECOSYSTEM", "folder": "aws_kms_secrets_api_ecosystem", "status": "catalog_only"},
        {"id": "bedrock_sagemaker", "name": "AWS BEDROCK AND SAGEMAKER API ECOSYSTEM", "folder": "aws_bedrock_sagemaker_api_ecosystem", "status": "catalog_only"},
        {"id": "billing_cost", "name": "AWS BILLING AND COST API ECOSYSTEM", "folder": "aws_billing_cost_api_ecosystem", "status": "catalog_only"},
        {"id": "api_gateway", "name": "AWS API GATEWAY ECOSYSTEM", "folder": "aws_api_gateway_ecosystem", "status": "catalog_only"},
        {"id": "cloudformation", "name": "AWS CLOUDFORMATION API ECOSYSTEM", "folder": "aws_cloudformation_api_ecosystem", "status": "catalog_only"},
    ],
    "related_ecosystems": [
        "AI", "CLOUD", "DATABASE", "DEVELOPER", "DOMAIN", "HOSTING",
        "SECURITY", "SERVER", "STORAGE", "WEB", "WEBSITE",
    ],
    "adapter_path": "backend/integrations/providers/aws.py",
    "credential_source": "iam_role_or_web_identity_or_managed_secret_store",
}


def list_aws_api_ecosystems() -> dict[str, object]:
    """List AWS API family catalogs; this does not assert live connectivity."""
    children = [dict(item) for item in AWS_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider": AWS_API_ECOSYSTEM["name"],
        "status": AWS_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


__all__ = ["AWS_API_ECOSYSTEM", "list_aws_api_ecosystems"]
