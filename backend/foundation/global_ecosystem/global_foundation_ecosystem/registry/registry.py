from __future__ import annotations

from typing import Any


class FoundationRegistry:
    """
    CENTRAL FOUNDATION REGISTRY

    Maintains registered Foundation components
    for MAIN BASE FOUNDATION.
    """

    def __init__(self):
        self._components: dict[str, dict[str, Any]] = {}

    def register_component(
        self,
        name: str,
        component: Any,
        category: str = "FOUNDATION",
    ) -> dict[str, Any]:
        component_name = name.strip().lower()

        if not component_name:
            raise ValueError("COMPONENT_NAME_REQUIRED")

        self._components[component_name] = {
            "name": component_name,
            "category": category,
            "component": component,
            "status": "REGISTERED",
        }

        return self.component_info(component_name)

    def unregister_component(self, name: str) -> dict[str, Any]:
        component_name = name.strip().lower()

        if component_name not in self._components:
            raise ValueError("COMPONENT_NOT_FOUND")

        del self._components[component_name]

        return {
            "success": True,
            "component": component_name,
            "status": "UNREGISTERED",
        }

    def component_info(self, name: str) -> dict[str, Any]:
        component_name = name.strip().lower()

        component = self._components.get(component_name)

        if component is None:
            raise ValueError("COMPONENT_NOT_FOUND")

        return {
            "name": component["name"],
            "category": component["category"],
            "status": component["status"],
        }

    def list_components(self) -> list[dict[str, Any]]:
        return [
            self.component_info(name)
            for name in sorted(self._components)
        ]

    def has_component(self, name: str) -> bool:
        return name.strip().lower() in self._components

    def count(self) -> int:
        return len(self._components)

    def clear(self) -> None:
        self._components.clear()

    def status(self) -> dict[str, Any]:
        return {
            "component_count": self.count(),
            "components": self.list_components(),
            "status": "READY",
        }


__all__ = [
    "FoundationRegistry",
]
