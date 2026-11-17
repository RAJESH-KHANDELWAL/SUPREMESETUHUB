"""Contracts for language taxonomy metadata; no provider execution."""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class LanguageDomain:
    domain_id: str
    name: str
    division: str
    folder: str
    scope: str
    age_restricted: bool = False
    consent_required: bool = False
    status: str = "CORE_CATALOG_ONLY"
    def __post_init__(self):
        if not all(isinstance(x, str) and x.strip() for x in (self.domain_id,self.name,self.division,self.folder,self.scope)):
            raise ValueError("language domain identity and scope fields must be non-empty strings")
        if self.division not in {"HUMAN","PROGRAMMING","PROVIDER","SHARED"}:
            raise ValueError("unsupported language domain division")
        if self.age_restricted and not self.consent_required:
            raise ValueError("age-restricted domains must require consent metadata")

@dataclass(frozen=True)
class LanguageServiceTier:
    tier_id: str
    name: str
    rank: int
    description: str
    capabilities: tuple[str, ...] = field(default_factory=tuple)
