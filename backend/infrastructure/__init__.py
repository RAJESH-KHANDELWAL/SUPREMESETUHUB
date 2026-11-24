"""Infrastructure control plane with domain implementations owned by GLOBAL INFRASTRUCTURE ECOSYSTEM."""

from pathlib import Path

_PACKAGE_DIR = Path(__file__).resolve().parent
_ECOSYSTEM_DOMAIN_DIR = (
    _PACKAGE_DIR / "global_ecosystem" / "global_infrastructure_ecosystem"
)

# Keep legacy imports (backend.infrastructure.<domain>) working while the
# implementation packages physically live under GLOBAL INFRASTRUCTURE ECOSYSTEM.
# The package directory remains second so global_ecosystem and root modules
# continue to resolve normally.
__path__ = [str(_ECOSYSTEM_DOMAIN_DIR), str(_PACKAGE_DIR)]

from .model import (
    InfrastructureCategory,
    InfrastructureOwnershipType,
    InfrastructureRegistry,
    InfrastructureRelationship,
    InfrastructureRelationshipType,
    InfrastructureResource,
    InfrastructureResourceStatus,
    InfrastructureResourceType,
)

__all__ = [
    "InfrastructureCategory",
    "InfrastructureOwnershipType",
    "InfrastructureRegistry",
    "InfrastructureRelationship",
    "InfrastructureRelationshipType",
    "InfrastructureResource",
    "InfrastructureResourceStatus",
    "InfrastructureResourceType",
]
