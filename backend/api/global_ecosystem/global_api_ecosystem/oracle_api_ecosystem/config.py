"""Environment-backed OCI configuration with secret-safe validation."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class OCIConfig:
    tenancy_ocid: str
    user_ocid: str
    fingerprint: str
    region: str
    private_key_file: str | None = None
    private_key_pem: str | None = None
    passphrase: str | None = None
    base_url: str | None = None

    @classmethod
    def from_env(cls) -> "OCIConfig":
        return cls(
            tenancy_ocid=os.getenv("OCI_TENANCY_OCID", "").strip(),
            user_ocid=os.getenv("OCI_USER_OCID", "").strip(),
            fingerprint=os.getenv("OCI_FINGERPRINT", "").strip(),
            region=os.getenv("OCI_REGION", "").strip(),
            private_key_file=os.getenv("OCI_PRIVATE_KEY_FILE") or None,
            private_key_pem=os.getenv("OCI_PRIVATE_KEY_PEM") or None,
            passphrase=os.getenv("OCI_PRIVATE_KEY_PASSPHRASE") or None,
            base_url=os.getenv("OCI_BASE_URL") or None,
        )

    def validate(self) -> list[str]:
        missing = [
            name for name, value in (
                ("OCI_TENANCY_OCID", self.tenancy_ocid),
                ("OCI_USER_OCID", self.user_ocid),
                ("OCI_FINGERPRINT", self.fingerprint),
                ("OCI_REGION", self.region),
            ) if not value
        ]
        if not self.private_key_file and not self.private_key_pem:
            missing.append("OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM")
        if self.private_key_file and self.private_key_pem:
            missing.append("Set only one of OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM")
        return missing

    @property
    def key_id(self) -> str:
        return f"{self.tenancy_ocid}/{self.user_ocid}/{self.fingerprint}"

    def load_private_key_pem(self) -> bytes:
        if self.private_key_pem:
            return self.private_key_pem.encode("utf-8")
        if self.private_key_file:
            with open(self.private_key_file, "rb") as key_file:
                return key_file.read()
        raise ValueError("OCI private key is not configured")
