"""Thread-safe in-memory domain profile registry."""
from __future__ import annotations
from threading import RLock
from .models import DomainProfile

class DomainRegistry:
    def __init__(self) -> None:
        self._profiles: dict[str, DomainProfile] = {}
        self._lock = RLock()

    def register(self, profile: DomainProfile) -> DomainProfile:
        key = profile.domain_id.strip().casefold()
        if not key:
            raise ValueError("domain_id is required")
        with self._lock:
            if key in self._profiles:
                raise ValueError(f"domain already registered: {key}")
            self._profiles[key] = profile
        return profile

    def get(self, domain_id: str) -> DomainProfile | None:
        with self._lock:
            return self._profiles.get(domain_id.strip().casefold())

    def list_profiles(self) -> tuple[DomainProfile, ...]:
        with self._lock:
            return tuple(self._profiles.values())

__all__ = ["DomainRegistry"]
