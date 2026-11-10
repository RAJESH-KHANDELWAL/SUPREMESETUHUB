"""Environment-backed configuration for Telegram; never logs credentials."""
from __future__ import annotations
from dataclasses import dataclass
import os

@dataclass(frozen=True, slots=True)
class ProviderConfig:
    credential: str | None = None

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        value = os.getenv("TELEGRAM_BOT_TOKEN")
        return cls(credential=value.strip() if value and value.strip() else None)

    @property
    def configured(self) -> bool:
        return bool(self.credential)

__all__ = ["ProviderConfig"]
