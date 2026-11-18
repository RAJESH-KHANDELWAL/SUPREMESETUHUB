"""Typed metadata identity for AWS KMS and Secrets Manager; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-KMS-SECRETS-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS KMS and Secrets Manager"
