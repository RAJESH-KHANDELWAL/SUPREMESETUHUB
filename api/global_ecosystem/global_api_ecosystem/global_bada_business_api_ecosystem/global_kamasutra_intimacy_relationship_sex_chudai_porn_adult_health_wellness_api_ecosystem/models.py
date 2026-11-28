"""Typed models for the adult wellness taxonomy; not clinical records."""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class EcosystemCategory:
    id: str
    name: str
    folder: str
    subdomains: tuple[str, ...] = field(default_factory=tuple)
    coverage: tuple[str, ...] = ("india", "global")
    channels: tuple[str, ...] = ("online", "offline", "hybrid")
    age_restriction: str = "18+"
    status: str = "taxonomy_scaffold"
