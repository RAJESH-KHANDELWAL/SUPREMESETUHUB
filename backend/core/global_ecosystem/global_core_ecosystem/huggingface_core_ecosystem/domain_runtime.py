"""Shared read-only runtime for Hugging Face CORE domain metadata."""
from .domain_catalog import get_domain

class HuggingFaceCoreDomainManager:
    def __init__(self, domain_id: str):
        self.domain_id = str(domain_id).strip().upper()
        if not self.domain_id:
            raise ValueError("HUGGINGFACE_CORE_DOMAIN_ID_REQUIRED")
        if get_domain(self.domain_id) is None:
            raise ValueError(f"UNKNOWN_HUGGINGFACE_CORE_DOMAIN: {self.domain_id}")
    def describe(self) -> dict:
        return {"success": True, "provider_id": "huggingface", "layer": "CORE",
                "domain": get_domain(self.domain_id), "implementation_mode": "SHARED_METADATA_TAXONOMY",
                "remote_operations_enabled": False}
