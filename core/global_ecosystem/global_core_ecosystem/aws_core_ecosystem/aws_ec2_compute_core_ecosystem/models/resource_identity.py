"""Typed metadata identity for AWS EC2 Compute; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-EC2-COMPUTE-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS EC2 Compute"
