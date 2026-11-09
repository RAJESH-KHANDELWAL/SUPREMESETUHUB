"""APP engine: lifecycle adapter for the APP-owned ecosystem.

The engine controls APP lifecycle through BaseEngine and delegates
component metadata operations to the APP layer. It does not implement
API transport, CORE orchestration, or ENGINE provider execution.
"""
from __future__ import annotations

from typing import Any

from backend.engine.base import BaseEngine
from backend.app.global_ecosystem.global_app_ecosystem import (
    GlobalAppEcosystemManager,
)


class AppEngine(BaseEngine):
    """Manage the GLOBAL APP ecosystem as a first-class engine."""

    NAME = "GLOBAL APP ENGINE"

    def __init__(
        self,
        app_manager: GlobalAppEcosystemManager | None = None,
    ) -> None:
        super().__init__(self.NAME)
        self.app_manager = app_manager or GlobalAppEcosystemManager()

    def start(self) -> dict[str, Any]:
        """Start APP lifecycle metadata; does not execute components."""
        lifecycle = self.app_manager.health()["lifecycle"]["state"]

        if lifecycle == "NEW":
            self.app_manager.transition("CONFIGURED")
            lifecycle = "CONFIGURED"
        elif lifecycle == "FAILED":
            self.app_manager.transition("CONFIGURED")
            lifecycle = "CONFIGURED"
        elif lifecycle == "STOPPED":
            self.app_manager.transition("STARTING")
            self.app_manager.transition("RUNNING")
            self.state = "RUNNING"
            return self.status()

        if lifecycle == "CONFIGURED":
            self.app_manager.transition("STARTING")
            self.app_manager.transition("RUNNING")
        elif lifecycle != "RUNNING":
            raise RuntimeError(f"APP cannot start from lifecycle state: {lifecycle}")

        super().start()
        return self.status()

    def stop(self) -> dict[str, Any]:
        """Stop APP lifecycle metadata without stopping the host process."""
        lifecycle = self.app_manager.health()["lifecycle"]["state"]

        if lifecycle == "RUNNING":
            self.app_manager.transition("STOPPING")
            self.app_manager.transition("STOPPED")
        elif lifecycle in {"NEW", "CONFIGURED", "FAILED"}:
            self.app_manager.transition("STOPPED")
        elif lifecycle == "STOPPING":
            self.app_manager.transition("STOPPED")

        super().stop()
        return self.status()

    def register_component(self, component: Any, *, replace: bool = False) -> Any:
        return self.app_manager.register_component(component, replace=replace)

    def get_component(self, component_id: str) -> Any:
        return self.app_manager.get_component(component_id)

    def list_components(self, **kwargs: Any) -> Any:
        return self.app_manager.list_components(**kwargs)

    def register_adapter(
        self,
        component_id: str,
        adapter: Any,
        *,
        replace: bool = False,
    ) -> Any:
        return self.app_manager.register_adapter(
            component_id,
            adapter,
            replace=replace,
        )

    def invoke_adapter(self, component_id: str, *args: Any, **kwargs: Any) -> Any:
        return self.app_manager.invoke_adapter(component_id, *args, **kwargs)

    def health(self) -> dict[str, Any]:
        return self.app_manager.health()

    def status(self) -> dict[str, Any]:
        return {
            **super().status(),
            "ecosystem": "GLOBAL_APP_ECOSYSTEM",
            "app_lifecycle": self.app_manager.health()["lifecycle"],
            "component_count": self.app_manager.health()["components"][
                "registered_components"
            ],
            "execution": "EXPLICIT_ONLY",
        }


__all__ = ["AppEngine"]
