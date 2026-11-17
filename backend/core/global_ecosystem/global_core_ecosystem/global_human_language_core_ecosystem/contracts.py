"""Contracts for human-language taxonomy metadata; no provider execution."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class HumanLanguageDomain:
    domain_id: str
    name: str
    folder: str
    scope: str
    age_restricted: bool = False
    consent_required: bool = False
    status: str = "CORE_CATALOG_ONLY"

    def __post_init__(self):
        if not all(
            isinstance(value, str) and value.strip()
            for value in (self.domain_id, self.name, self.folder, self.scope)
        ):
            raise ValueError("human-language domain identity and scope fields must be non-empty strings")
        if self.age_restricted and not self.consent_required:
            raise ValueError("age-restricted domains must require consent metadata")


@dataclass(frozen=True)
class HumanLanguageServiceTier:
    tier_id: str
    name: str
    rank: int
    description: str
    capabilities: tuple[str, ...] = field(default_factory=tuple)
