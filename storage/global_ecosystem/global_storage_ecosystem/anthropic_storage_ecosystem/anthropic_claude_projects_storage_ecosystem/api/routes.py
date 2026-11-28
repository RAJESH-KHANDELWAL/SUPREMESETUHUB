"""Framework-neutral API handlers for ANTHROPIC_CLAUDE_PROJECTS_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService
def get_ecosystem_status() -> dict:
    return CategoryEcosystemService().describe()
def get_health() -> dict:
    return CategoryEcosystemService().health()
