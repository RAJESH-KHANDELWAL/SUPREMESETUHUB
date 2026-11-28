from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import present_any, provider_health


class AWSProvider(IntegrationProvider):
    """AWS IAM / SDK integration readiness adapter."""

    name = "AWS"
    category = "CLOUD_PLATFORM"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": [
                "AWS_IAM_STS",
                "AWS_EC2",
                "AWS_LIGHTSAIL",
                "AWS_LAMBDA",
                "AWS_CONTAINERS",
                "AWS_S3",
                "AWS_RDS_DYNAMODB",
                "AWS_ROUTE53",
                "AWS_VPC",
                "AWS_CLOUDWATCH",
                "AWS_CLOUDTRAIL",
                "AWS_KMS_SECRETS_MANAGER",
                "AWS_BEDROCK_SAGEMAKER",
                "AWS_BILLING_COST_EXPLORER",
                "AWS_API_GATEWAY",
                "AWS_CLOUDFORMATION",
            ],
            "auth_method": "IAM role / web identity preferred; access keys only where required",
            "setup_guide": "docs/GOOGLE_MICROSOFT_AWS_APPLE_SETUP.md",
        }

    def health(self) -> Dict[str, Any]:
        import os

        configured = bool(os.getenv("AWS_REGION", "").strip()) and present_any(
            ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"),
            ("AWS_ROLE_ARN", "AWS_WEB_IDENTITY_TOKEN_FILE"),
        )
        credentials_present = present_any(
            ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"),
            ("AWS_ROLE_ARN", "AWS_WEB_IDENTITY_TOKEN_FILE"),
        )
        required = ["AWS_REGION"]
        if not credentials_present:
            required.append(
                "AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY or "
                "AWS_ROLE_ARN + AWS_WEB_IDENTITY_TOKEN_FILE"
            )
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="AWS IAM role/web identity preferred",
            required_configuration=required,
            capabilities=[
                "IAM_STS", "EC2", "LIGHTSAIL", "LAMBDA", "CONTAINERS",
                "S3", "RDS_DYNAMODB", "ROUTE53", "VPC", "CLOUDWATCH",
                "CLOUDTRAIL", "KMS_SECRETS", "BEDROCK_SAGEMAKER",
                "BILLING_COST", "API_GATEWAY", "CLOUDFORMATION",
            ],
        )
