"""In-memory, APP-layer component registry."""
from __future__ import annotations
from threading import RLock
from .components import BadaBusinessAppComponent

class BadaBusinessAppRegistry:
    def __init__(self) -> None:
        self._items: dict[str, BadaBusinessAppComponent] = {}
        self._lock = RLock()

    def register(self, component: BadaBusinessAppComponent) -> None:
        if not component.component_id.strip():
            raise ValueError("APP_COMPONENT_ID_REQUIRED")
        with self._lock:
            if component.component_id in self._items:
                raise ValueError(f"APP_COMPONENT_ALREADY_REGISTERED:{component.component_id}")
            self._items[component.component_id] = component

    def get(self, component_id: str) -> BadaBusinessAppComponent:
        with self._lock:
            try:
                return self._items[component_id]
            except KeyError as exc:
                raise KeyError(f"APP_COMPONENT_NOT_FOUND:{component_id}") from exc

    def list(self) -> tuple[BadaBusinessAppComponent, ...]:
        with self._lock:
            return tuple(self._items.values())

    def register_defaults(self) -> int:
        added = 0
        for component in build_default_components():
            try:
                self.register(component)
                added += 1
            except ValueError as exc:
                if "ALREADY_REGISTERED" not in str(exc):
                    raise
        return added

from .components import build_default_components
