"""Typed metadata identity for AWS CloudTrail; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-CLOUDTRAIL-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS CloudTrail"
