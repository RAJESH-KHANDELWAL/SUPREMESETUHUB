"""Business-facing catalogue adapter to the canonical Cultural CORE taxonomy."""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.catalog import ECOSYSTEM_ID as SOURCE_ECOSYSTEM_ID, PARENT_ECOSYSTEM_ID as CULTURAL_CORE_ID, list_capabilities as list_source_capabilities, get_capability
ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-BHARAT-WORLD-CULTURE-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
SOURCE_CORE_ID = CULTURAL_CORE_ID
SOURCE_PACKAGE = "backend/core/global_ecosystem/global_core_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem/"
def list_capabilities(domain: str | None = None) -> list[dict[str, Any]]:
 return list_source_capabilities(domain)
def get_business_capability(capability_id: str) -> dict[str, Any] | None:
 return get_capability(capability_id)
