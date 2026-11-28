"""Typed metadata identity for AWS Lightsail; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-LIGHTSAIL-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Lightsail"
