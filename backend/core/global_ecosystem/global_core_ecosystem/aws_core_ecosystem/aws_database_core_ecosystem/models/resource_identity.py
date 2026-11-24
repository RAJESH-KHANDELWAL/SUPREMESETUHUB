"""Typed metadata identity for AWS Database (RDS, Aurora and DynamoDB); no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-DATABASE-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Database (RDS, Aurora and DynamoDB)"
