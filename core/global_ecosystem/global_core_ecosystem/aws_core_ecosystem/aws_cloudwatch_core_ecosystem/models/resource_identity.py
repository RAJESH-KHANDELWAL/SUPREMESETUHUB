"""Typed metadata identity for AWS CloudWatch; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-CLOUDWATCH-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS CloudWatch"
