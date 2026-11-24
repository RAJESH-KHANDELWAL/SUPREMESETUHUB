"""Azure service-principal configuration; secrets are never logged."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class AzureConfig:
    tenant_id: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    subscription_id: str | None = None

    @classmethod
    def from_env(cls) -> "AzureConfig":
        return cls(os.getenv("AZURE_TENANT_ID"), os.getenv("AZURE_CLIENT_ID"),
                   os.getenv("AZURE_CLIENT_SECRET"), os.getenv("AZURE_SUBSCRIPTION_ID"))

    def credentials_configured(self) -> bool:
        return bool(self.tenant_id and self.client_id and self.client_secret and self.subscription_id)
