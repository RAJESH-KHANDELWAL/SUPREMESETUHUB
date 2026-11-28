"""Typed metadata identity for AWS Bedrock and SageMaker AI; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-BEDROCK-SAGEMAKER-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Bedrock and SageMaker AI"
