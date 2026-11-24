"""Framework-neutral handlers for DEEPSEEK_TRAINING_DATA_STORAGE_ECOSYSTEM; no external operations are performed."""
from ..ecosystem_service import CategoryEcosystemService
def describe() -> dict:
    return CategoryEcosystemService().describe()
def health() -> dict:
    return CategoryEcosystemService().health()
