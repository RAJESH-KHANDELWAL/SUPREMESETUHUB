"""Typed metadata identity for AWS Lambda; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-LAMBDA-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Lambda"
