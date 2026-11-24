"""Manager for the MAPS_GEOSPATIAL_AND_TRAVEL Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class MapsGeospatialDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "MAPS_GEOSPATIAL_AND_TRAVEL"


def get_manager() -> MapsGeospatialDomainManager:
    return MapsGeospatialDomainManager()


__all__ = ["MapsGeospatialDomainManager", "get_manager"]
