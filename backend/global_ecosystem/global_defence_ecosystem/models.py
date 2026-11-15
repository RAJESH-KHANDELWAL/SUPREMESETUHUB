"""Typed records for defence and civil-protection domain metadata."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class DefenceUseCase:
    use_case_id: str
    title: str
    capability_group: str
    geography: str = "india"
    maturity: str = "standard"
    stakeholders: tuple[str, ...] = ()
    safeguards: tuple[str, ...] = ("human_oversight", "audit_logging", "legal_review")
    metadata: dict[str, Any] = field(default_factory=dict)
