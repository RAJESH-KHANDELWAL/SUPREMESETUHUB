"""Typed metadata identity for AWS IAM and STS; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-IAM-STS-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS IAM and STS"
