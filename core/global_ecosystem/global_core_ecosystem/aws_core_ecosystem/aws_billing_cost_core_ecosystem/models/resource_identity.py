"""Typed metadata identity for AWS Billing and Cost Management; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-BILLING-COST-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Billing and Cost Management"
