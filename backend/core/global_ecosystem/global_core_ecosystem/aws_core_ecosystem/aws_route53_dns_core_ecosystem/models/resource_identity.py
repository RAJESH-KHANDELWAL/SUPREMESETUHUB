"""Typed metadata identity for AWS Route 53 DNS; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-ROUTE53-DNS-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Route 53 DNS"
