"""Token configuration for Cloudflare; never expose token values in logs."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class CloudflareConfig:
    api_token: str | None = None
    @classmethod
    def from_env(cls) -> "CloudflareConfig":
        return cls(os.getenv("CLOUDFLARE_API_TOKEN"))
    def credentials_configured(self) -> bool:
        return bool(self.api_token)
