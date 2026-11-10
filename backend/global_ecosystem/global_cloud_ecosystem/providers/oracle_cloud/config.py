"""OCI configuration; SDK-specific signer construction remains an injected concern."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class OracleCloudConfig:
    config_file: str | None = None
    profile: str = "DEFAULT"
    region: str | None = None
    tenancy: str | None = None
    user: str | None = None
    fingerprint: str | None = None
    key_file: str | None = None

    @classmethod
    def from_env(cls) -> "OracleCloudConfig":
        return cls(os.getenv("OCI_CONFIG_FILE"), os.getenv("OCI_PROFILE", "DEFAULT"),
                   os.getenv("OCI_REGION"), os.getenv("OCI_TENANCY"), os.getenv("OCI_USER"),
                   os.getenv("OCI_FINGERPRINT"), os.getenv("OCI_KEY_FILE"))
