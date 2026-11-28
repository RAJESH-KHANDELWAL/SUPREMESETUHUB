"""Provider-neutral metadata route handlers."""
from ..ecosystem_service import EcosystemService

def describe() -> dict:
    return EcosystemService().describe()
