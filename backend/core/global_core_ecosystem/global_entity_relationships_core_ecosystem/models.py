"""Typed metadata contracts for entity relationship records."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class RelationshipRecord:
    relationship_id: str
    source_entity_id: str
    target_entity_id: str
    relationship_type: str
    verification_status: str = "UNVERIFIED"
    jurisdiction: str | None = None
    effective_from: str | None = None
    effective_to: str | None = None
    source_urls: tuple[str,...] = ()
    metadata: dict[str,Any] = field(default_factory=dict)
