"""Typed record for a workforce classification."""
from dataclasses import dataclass, field
@dataclass(frozen=True)
class WorkRole:
    category_id: str
    title: str
    aliases: tuple[str, ...] = ()
    responsibilities: tuple[str, ...] = ()
    dimensions: dict = field(default_factory=dict)
