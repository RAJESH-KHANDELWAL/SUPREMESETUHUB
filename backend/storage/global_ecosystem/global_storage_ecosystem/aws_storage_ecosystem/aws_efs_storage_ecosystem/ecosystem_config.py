"""Runtime configuration boundary; secrets belong in a secret manager."""
import os

PACKAGE_ID = "aws_efs_storage_ecosystem"
ENV_PREFIX = "AWS_EFS_STORAGE_ECOSYSTEM"

def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "false").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "credentials_configured": False,
        "connection_state": "NOT_CONFIGURED",
        "storage_operations_enabled": False,
    }
