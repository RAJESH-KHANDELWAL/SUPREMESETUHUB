"""Small in-memory registry for approved defence-domain metadata."""
from __future__ import annotations

from threading import RLock
from .models import DefenceUseCase

class DefenceUseCaseRegistry:
    """Thread-safe metadata registry; persistence belongs to DATABASE layer."""
    def __init__(self) -> None:
        self._items: dict[str, DefenceUseCase] = {}
        self._lock = RLock()

    def register(self, item: DefenceUseCase) -> None:
        if not item.use_case_id.strip():
            raise ValueError("use_case_id is required")
        with self._lock:
            if item.use_case_id in self._items:
                raise ValueError(f"Use case already registered: {item.use_case_id}")
            self._items[item.use_case_id] = item

    def get(self, use_case_id: str) -> DefenceUseCase | None:
        with self._lock:
            return self._items.get(use_case_id)

    def list(self) -> tuple[DefenceUseCase, ...]:
        with self._lock:
            return tuple(self._items[key] for key in sorted(self._items))

    def remove(self, use_case_id: str) -> bool:
        with self._lock:
            return self._items.pop(use_case_id, None) is not None
