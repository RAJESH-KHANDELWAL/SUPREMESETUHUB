"""Token configuration for Netlify; token values are never logged."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class NetlifyConfig:
    api_token: str | None = None
    @classmethod
    def from_env(cls) -> "NetlifyConfig":
        return cls(os.getenv("NETLIFY_AUTH_TOKEN"))
    def credentials_configured(self) -> bool:
        return bool(self.api_token)
