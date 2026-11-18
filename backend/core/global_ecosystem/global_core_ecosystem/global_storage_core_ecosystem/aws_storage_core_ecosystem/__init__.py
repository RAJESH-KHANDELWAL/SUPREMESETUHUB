"""AWS Storage Core provider package."""
PROVIDER = "aws"
ECOSYSTEM_ID = "AWS-STORAGE-CORE-ECOSYSTEM"

from .service import AwsStorageCoreService

__all__ = ["PROVIDER", "ECOSYSTEM_ID", "AwsStorageCoreService"]
