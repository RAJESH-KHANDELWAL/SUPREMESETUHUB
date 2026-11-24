"""Typed domain models."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class EcosystemDomain:
    id: str
    name: str
    description: str
    folder: str
    status: str = "taxonomy_scaffold"

@dataclass(frozen=True)
class EcosystemStatus:
    ecosystem_id: str = "agriculture_food_natural_resources"
    version: str = "0.1.0"
    status: str = "scaffold"
    domain_count: int = 16
