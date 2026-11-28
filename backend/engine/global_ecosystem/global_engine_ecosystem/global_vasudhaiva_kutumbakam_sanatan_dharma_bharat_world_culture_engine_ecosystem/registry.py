"""Independent registry for cultural ENGINE domain metadata."""
from __future__ import annotations
from .models import CulturalEngineDomain

class CulturalEngineRegistry:
    def __init__(self) -> None:
        self._domains: dict[str, CulturalEngineDomain] = {}

    def register(self, domain: CulturalEngineDomain) -> None:
        if domain.domain_id in self._domains:
            raise ValueError(f"Duplicate cultural ENGINE domain: {domain.domain_id}")
        self._domains[domain.domain_id] = domain

    def get(self, domain_id: str) -> CulturalEngineDomain | None:
        return self._domains.get(domain_id)

    def list(self) -> tuple[CulturalEngineDomain, ...]:
        return tuple(self._domains.values())
