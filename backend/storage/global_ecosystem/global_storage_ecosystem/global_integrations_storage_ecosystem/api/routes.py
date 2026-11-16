"""Framework-neutral status and health handlers; no provider I/O."""
from ..ecosystem_service import EcosystemService


def get_ecosystem_status() -> dict:
    return EcosystemService().describe()


def get_health() -> dict:
    return EcosystemService().health()
