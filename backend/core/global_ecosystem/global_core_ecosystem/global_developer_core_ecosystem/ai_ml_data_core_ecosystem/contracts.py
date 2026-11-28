"""Provider-specific metadata contract for AI ML DATA Core."""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ProviderMetadata:
    provider_id: str = "ai_ml_data"
    ecosystem_id: str = "GLOBAL-DEVELOPER-AI-ML-DATA-CORE-ECOSYSTEM"
    api_catalog_ref: str = "backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem/ai_ml_data_api_ecosystem"
    status: str = "CORE_CATALOG_ONLY"
    live_connection_verified: bool = False

@dataclass(frozen=True)
class ProviderResult:
    success: bool
    status: str = "CORE_CATALOG_ONLY"
    data: dict[str, Any] | None = None
