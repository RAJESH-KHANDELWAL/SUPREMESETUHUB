"""Framework-neutral API handlers; mount in an authorized application router."""
from ..ecosystem_service import EcosystemService
_service = EcosystemService()
def describe() -> dict:
    return _service.describe()
def health() -> dict:
    return _service.health()
