"""
CORE Decision Management

Defines the structure and lifecycle of management decisions.

This layer records and manages decisions.
It does not execute technical work.
"""

from typing import Any, Dict, List


class DecisionManager:
    """
    Central decision-management controller.
    """

    def __init__(self) -> None:
        self.decisions: Dict[str, Dict[str, Any]] = {}

    def create_decision(
        self,
        decision_id: str,
        title: str,
        description: str = "",
        created_by: str = "SYSTEM",
        priority: str = "NORMAL",
    ) -> None:
        """Create a new decision record."""

        key = decision_id.strip()

        if not key:
            raise ValueError("decision_id cannot be empty")

        if not title.strip():
            raise ValueError("title cannot be empty")

        self.decisions[key] = {
            "decision_id": key,
            "title": title.strip(),
            "description": description.strip(),
            "created_by": created_by.strip(),
            "priority": priority.strip().upper(),
            "status": "PENDING",
            "decision": None,
            "approved_by": None,
        }

    def get_decision(
        self,
        decision_id: str,
    ) -> Dict[str, Any] | None:
        """Return a decision record."""

        return self.decisions.get(decision_id.strip())

    def approve(
        self,
        decision_id: str,
        approved_by: str,
        decision: str,
    ) -> bool:
        """Approve a pending decision."""

        key = decision_id.strip()

        if key not in self.decisions:
            return False

        if not approved_by.strip():
            raise ValueError("approved_by cannot be empty")

        if not decision.strip():
            raise ValueError("decision cannot be empty")

        self.decisions[key]["status"] = "APPROVED"
        self.decisions[key]["decision"] = decision.strip()
        self.decisions[key]["approved_by"] = approved_by.strip()

        return True

    def reject(
        self,
        decision_id: str,
        rejected_by: str,
        reason: str = "",
    ) -> bool:
        """Reject a pending decision."""

        key = decision_id.strip()

        if key not in self.decisions:
            return False

        if not rejected_by.strip():
            raise ValueError("rejected_by cannot be empty")

        self.decisions[key]["status"] = "REJECTED"
        self.decisions[key]["approved_by"] = rejected_by.strip()
        self.decisions[key]["decision"] = reason.strip()

        return True

    def cancel(
        self,
        decision_id: str,
        cancelled_by: str,
    ) -> bool:
        """Cancel a decision."""

        key = decision_id.strip()

        if key not in self.decisions:
            return False

        self.decisions[key]["status"] = "CANCELLED"
        self.decisions[key]["approved_by"] = cancelled_by.strip()

        return True

    def list_decisions(self) -> List[Dict[str, Any]]:
        """Return all decision records."""

        return list(self.decisions.values())

    def list_pending(self) -> List[Dict[str, Any]]:
        """Return decisions awaiting a decision."""

        return [
            decision
            for decision in self.decisions.values()
            if decision["status"] == "PENDING"
        ]

    def count(self) -> int:
        """Return total number of decisions."""

        return len(self.decisions)
