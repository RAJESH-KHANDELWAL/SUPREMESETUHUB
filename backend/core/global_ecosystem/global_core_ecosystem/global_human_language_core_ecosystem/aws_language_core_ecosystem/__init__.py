"""Public metadata-only interface for AWS LANGUAGE."""
from .ecosystem_config import ECOSYSTEM_ID, PROVIDER_ID, PROVIDER_NAME
from .service import capabilities, describe, readiness, service

__all__ = ["ECOSYSTEM_ID", "PROVIDER_ID", "PROVIDER_NAME", "service", "describe", "readiness", "capabilities"]
