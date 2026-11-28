"""Typed metadata identity for AWS CloudFormation; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-CLOUDFORMATION-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS CloudFormation"
