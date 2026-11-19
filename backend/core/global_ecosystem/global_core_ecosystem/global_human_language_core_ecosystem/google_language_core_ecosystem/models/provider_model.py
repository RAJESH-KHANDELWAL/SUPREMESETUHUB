"""Provider descriptor model for GOOGLE LANGUAGE."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id: str
    provider_key: str
    name: str
    ecosystem_id: str
    status: str = "CORE_CATALOG_ONLY"
    live_connection: bool = False
