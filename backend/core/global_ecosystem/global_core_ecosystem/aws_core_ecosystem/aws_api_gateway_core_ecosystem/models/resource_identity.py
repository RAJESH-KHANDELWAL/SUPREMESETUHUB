"""Typed metadata identity for AWS API Gateway; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-API-GATEWAY-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS API Gateway"
