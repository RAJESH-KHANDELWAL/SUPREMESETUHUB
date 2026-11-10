"""Environment-backed Reddit configuration; credentials are never logged."""
from __future__ import annotations
from dataclasses import dataclass
import os

@dataclass(frozen=True, slots=True)
class ProviderConfig:
    credential: str | None = None

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        value = os.getenv("REDDIT_CLIENT_ID")
        return cls(credential=value.strip() if value and value.strip() else None)

    @property
    def configured(self) -> bool:
        return bool(self.credential)

__all__ = ["ProviderConfig"]
