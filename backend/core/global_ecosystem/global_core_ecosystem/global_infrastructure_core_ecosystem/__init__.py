"""CORE contracts for provider-neutral infrastructure identity."""
from .service import GlobalInfrastructureCoreService

LAYER = "CORE"
ECOSYSTEM_ID = "global-infrastructure-core-ecosystem"

__all__ = ["LAYER", "ECOSYSTEM_ID", "GlobalInfrastructureCoreService"]
