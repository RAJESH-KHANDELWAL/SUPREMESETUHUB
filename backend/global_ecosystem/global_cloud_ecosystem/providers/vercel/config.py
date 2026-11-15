"""Token configuration for Vercel; token values are never logged."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class VercelConfig:
    api_token: str | None = None
    @classmethod
    def from_env(cls) -> "VercelConfig":
        return cls(os.getenv("VERCEL_TOKEN"))
    def credentials_configured(self) -> bool:
        return bool(self.api_token)
