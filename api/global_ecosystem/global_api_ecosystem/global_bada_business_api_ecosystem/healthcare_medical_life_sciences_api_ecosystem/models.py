"""Lightweight taxonomy models; these are not clinical records."""
from dataclasses import dataclass

@dataclass(frozen=True)
class HealthcareDomain:
    id: str
    name: str
    folder: str
    description: str
    status: str = "taxonomy_scaffold"

@dataclass(frozen=True)
class EcosystemStatus:
    ecosystem_id: str = "healthcare_medical_life_sciences"
    version: str = "0.1.0"
    status: str = "scaffold"
    domain_count: int = 34
