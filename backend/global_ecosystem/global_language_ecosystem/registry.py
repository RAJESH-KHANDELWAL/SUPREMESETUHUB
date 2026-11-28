"""Small in-memory registry for language metadata.

This is a development utility, not a persistent database or a production
distributed registry.
"""
from threading import RLock
from .models import LanguageProfile


class LanguageRegistry:
    def __init__(self) -> None:
        self._items: dict[str, LanguageProfile] = {}
        self._lock = RLock()

    def register(self, profile: LanguageProfile, *, replace: bool = False) -> None:
        key = profile.language_code.lower()
        with self._lock:
            if key in self._items and not replace:
                raise ValueError(f"language already registered: {key}")
            self._items[key] = profile

    def get(self, language_code: str) -> LanguageProfile | None:
        with self._lock:
            return self._items.get(language_code.lower())

    def list_all(self) -> tuple[LanguageProfile, ...]:
        with self._lock:
            return tuple(self._items[key] for key in sorted(self._items))
