from __future__ import annotations

from typing import Any

from .identity import SupremeIdentity
from .memory import SupremeMemory
from .orchestrator import SupremeOrchestrator
from .permissions import SupremePermissions


class SupremePersonalAI:
    """
    Central SUPREME PERSONAL AI core.

    Connects identity, permissions, memory and request
    orchestration into one owner-controlled AI layer.
    """

    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.identity = SupremeIdentity()
        self.permissions = SupremePermissions()
        self.memory = SupremeMemory()
        self.orchestrator = SupremeOrchestrator()

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "name": "SUPREME",
            "version": self.VERSION,
            "type": "PERSONAL_AI",
            "mode": "OWNER_PERSONAL_AI",
            "status": "READY",
            "identity": self.identity.context(),
            "capabilities": self.orchestrator.capabilities(),
            "memory_records": self.memory.count(),
        }

    def plan(
        self,
        request: str,
        actor_role: str = "OWNER",
    ) -> dict[str, Any]:
        plan = self.orchestrator.plan(request)

        capability = plan["capability"]

        permission = self.permissions.check(
            actor_role=actor_role,
            capability=f"{capability}.read",
        )

        return {
            **plan,
            "permission": permission,
        }

    def remember(
        self,
        content: str,
        category: str = "general",
        actor_role: str = "OWNER",
    ) -> dict[str, Any]:
        self.permissions.require_owner(actor_role)

        return self.memory.remember(
            content=content,
            category=category,
        )

    def capabilities(self) -> list[str]:
        return self.orchestrator.capabilities()
