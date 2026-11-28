"""Typed metadata identity for AWS VPC Networking; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-VPC-NETWORKING-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS VPC Networking"
