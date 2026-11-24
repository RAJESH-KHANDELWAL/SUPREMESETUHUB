"""Runtime configuration for DEEPSEEK_RETRIEVAL_AUGMENTED_GENERATION_STORAGE_ECOSYSTEM; never store secrets in source."""
import os
ECOSYSTEM_ID = "DEEPSEEK_RETRIEVAL_AUGMENTED_GENERATION_STORAGE_ECOSYSTEM"
ENV_PREFIX = "DEEPSEEK_RETRIEVAL_AUGMENTED_GENERATION_STORAGE_ECOSYSTEM"
def get_config() -> dict:
    return {"enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "true").lower() == "true", "environment": os.getenv("APP_ENV", "development"), "connection_state": "NOT_CONFIGURED", "credentials_configured": False}
