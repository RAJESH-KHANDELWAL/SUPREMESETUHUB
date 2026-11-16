from typing import Any, Dict

from ..base import IntegrationProvider


class ESAProvider(IntegrationProvider):
    """European Space Agency public-data integration metadata.

    This provider advertises intended data families only. It does not claim a
    live connection or imply that every ESA dataset has a public API.
    """

    name = "ESA"
    category = "SPACE_AND_EARTH_OBSERVATION"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "ESA Open Access / Copernicus Data Space APIs (dataset-specific)",
            "official_url": "https://www.esa.int/",
            "capabilities": [
                "EARTH_OBSERVATION_CATALOGS",
                "SATELLITE_MISSION_METADATA",
                "COPERNICUS_DATA_DISCOVERY",
                "SPACE_RESEARCH_DATA",
            ],
            "authentication": "PUBLIC_ACCESS_OR_PROVIDER_ACCOUNT_DEPENDING_ON_DATASET",
            "connection": "NOT_CONNECTED",
            "integration_mode": "CATALOG_ONLY",
        }

    def health(self) -> Dict[str, Any]:
        return {
            "provider": self.name,
            "category": self.category,
            "status": "READY",
            "authentication": "NOT_CONFIGURED",
            "connection": "NOT_CONNECTED",
            "integration_mode": "CATALOG_ONLY",
        }
