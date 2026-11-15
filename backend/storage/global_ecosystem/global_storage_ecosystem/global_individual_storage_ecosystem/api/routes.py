"""Framework-neutral API contract for individual storage metadata.

HTTP framework bindings and authentication middleware belong in the API layer.
"""
from .ecosystem_service import EcosystemService


def describe_individual_storage() -> dict:
    """Return package capabilities without disclosing personal information."""
    return EcosystemService().describe()


def individual_storage_health() -> dict:
    """Return local foundation health; never implies provider connectivity."""
    return EcosystemService().health()
