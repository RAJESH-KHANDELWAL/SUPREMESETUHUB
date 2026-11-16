"""Typed record for independent-work and business categories."""
from dataclasses import dataclass, field
@dataclass(frozen=True)
class IndependentWorkProfile:
    category_id: str
    title: str
    aliases: tuple[str, ...] = ()
    responsibilities: tuple[str, ...] = ()
    business_dimensions: dict = field(default_factory=dict)
