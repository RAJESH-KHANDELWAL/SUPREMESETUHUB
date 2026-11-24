"""Typed metadata identity for AWS Containers (ECS, EKS and ECR); no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-CONTAINERS-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS Containers (ECS, EKS and ECR)"
