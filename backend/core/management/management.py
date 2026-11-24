"""
CORE Management

Central management layer for organizing people, roles,
responsibilities, resources and approved work.

Management coordinates work.
It does not replace the ENGINE execution layer.
"""

from typing import Any, Dict, List


class Management:
    """
    Central CORE management controller.
    """

    def __init__(self) -> None:
        self.roles: Dict[str, Dict[str, Any]] = {}
        self.teams: Dict[str, Dict[str, Any]] = {}
        self.responsibilities: Dict[str, List[str]] = {}
        self.active_work: Dict[str, Dict[str, Any]] = {}

    def register_role(
        self,
        role_name: str,
        description: str = "",
        authority: List[str] | None = None,
    ) -> None:
        """Register a management or leadership role."""

        key = role_name.strip().upper()

        if not key:
            raise ValueError("role_name cannot be empty")

        self.roles[key] = {
            "role_name": key,
            "description": description,
            "authority": list(authority or []),
        }

    def get_role(self, role_name: str) -> Dict[str, Any] | None:
        """Return a registered role."""

        return self.roles.get(role_name.strip().upper())

    def register_team(
        self,
        team_name: str,
        leader: str | None = None,
        members: List[str] | None = None,
    ) -> None:
        """Register a team and its leadership."""

        key = team_name.strip().upper()

        if not key:
            raise ValueError("team_name cannot be empty")

        self.teams[key] = {
            "team_name": key,
            "leader": leader,
            "members": list(members or []),
        }

    def get_team(self, team_name: str) -> Dict[str, Any] | None:
        """Return a registered team."""

        return self.teams.get(team_name.strip().upper())

    def assign_responsibility(
        self,
        identity: str,
        responsibility: str,
    ) -> None:
        """Assign a responsibility to an identity."""

        identity_key = identity.strip()

        if not identity_key:
            raise ValueError("identity cannot be empty")

        if not responsibility.strip():
            raise ValueError("responsibility cannot be empty")

        self.responsibilities.setdefault(identity_key, [])

        if responsibility not in self.responsibilities[identity_key]:
            self.responsibilities[identity_key].append(responsibility)

    def get_responsibilities(
        self,
        identity: str,
    ) -> List[str]:
        """Return responsibilities assigned to an identity."""

        return list(
            self.responsibilities.get(identity.strip(), [])
        )

    def register_work(
        self,
        work_id: str,
        work_name: str,
        assigned_to: str | None = None,
        status: str = "PENDING",
    ) -> None:
        """Register work before execution."""

        key = work_id.strip()

        if not key:
            raise ValueError("work_id cannot be empty")

        self.active_work[key] = {
            "work_id": key,
            "work_name": work_name.strip(),
            "assigned_to": assigned_to,
            "status": status.upper(),
        }

    def update_work_status(
        self,
        work_id: str,
        status: str,
    ) -> bool:
        """Update the status of registered work."""

        key = work_id.strip()

        if key not in self.active_work:
            return False

        self.active_work[key]["status"] = status.strip().upper()
        return True

    def get_work(
        self,
        work_id: str,
    ) -> Dict[str, Any] | None:
        """Return registered work information."""

        return self.active_work.get(work_id.strip())

    def list_work(self) -> List[Dict[str, Any]]:
        """Return all registered work."""

        return list(self.active_work.values())

    def summary(self) -> Dict[str, int]:
        """Return a management-layer summary."""

        return {
            "roles": len(self.roles),
            "teams": len(self.teams),
            "identities_with_responsibilities": len(
                self.responsibilities
            ),
            "active_work_items": len(self.active_work),
        }
