"""Framework-neutral handlers for DEEPSEEK_INFORMATION_RETRIEVAL_STORAGE_ECOSYSTEM; no external operations are performed."""
from ..ecosystem_service import CategoryEcosystemService
def describe() -> dict:
    return CategoryEcosystemService().describe()
def health() -> dict:
    return CategoryEcosystemService().health()
