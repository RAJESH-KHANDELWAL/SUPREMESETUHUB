"""Typed metadata identity for AWS S3 Storage; no AWS resource is queried."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AwsResourceFamilyIdentity:
    ecosystem_id: str = "AWS-S3-STORAGE-CORE-ECOSYSTEM"
    provider: str = "aws"
    display_name: str = "AWS S3 Storage"
