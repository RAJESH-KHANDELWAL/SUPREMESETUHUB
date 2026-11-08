"""Google provider core ecosystem metadata and integration boundaries."""
from .catalog import GOOGLE_CORE_ECOSYSTEM, get_google_core_catalog
from .service import GoogleCoreEcosystemService

__all__ = ["GOOGLE_CORE_ECOSYSTEM", "get_google_core_catalog", "GoogleCoreEcosystemService"]
