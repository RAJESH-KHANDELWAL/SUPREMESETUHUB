"""Infrastructure control plane with domain implementations owned by GLOBAL INFRASTRUCTURE ECOSYSTEM."""

from pathlib import Path

_PACKAGE_DIR = Path(__file__).resolve().parent
_ECOSYSTEM_DOMAIN_DIR = (
    _PACKAGE_DIR / "global_ecosystem" / "global_infrastructure_ecosystem"
)

# Resolve root compatibility shims first (backend.infrastructure.<module>).
# The ecosystem directory remains available for modules not defined at the
# package root, while canonical implementations are imported by full path.
__path__ = [str(_PACKAGE_DIR), str(_ECOSYSTEM_DOMAIN_DIR)]

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
