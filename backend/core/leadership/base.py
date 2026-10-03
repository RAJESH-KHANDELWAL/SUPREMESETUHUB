"""
CORE Leadership Base

Common foundation for all leadership roles.

This layer defines WHAT a leadership role is.
It does not perform technical execution.
Technical execution belongs to backend/engines.
"""

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class LeadershipRole:
    """
    Common representation of a leadership/management role.
    """

    role_name: str
    level: str = "leadership"
    responsibilities: list[str] = field(default_factory=list)
    authority: list[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def describe(self) -> Dict[str, Any]:
        """
        Return a structured description of the leadership role.
        """
        return {
            "role_name": self.role_name,
            "level": self.level,
            "responsibilities": self.responsibilities,
            "authority": self.authority,
            "metadata": self.metadata,
        }

    def can_decide(self, decision: str) -> bool:
        """
        Basic decision-authority check.

        Detailed authorization rules should be implemented
        by the CORE management/authorization layer.
        """
        return decision in self.authority

    def add_responsibility(self, responsibility: str) -> None:
        """Add a responsibility if it is not already registered."""
        if responsibility not in self.responsibilities:
            self.responsibilities.append(responsibility)

    def add_authority(self, authority: str) -> None:
        """Add an authority if it is not already registered."""
        if authority not in self.authority:
            self.authority.append(authority)
