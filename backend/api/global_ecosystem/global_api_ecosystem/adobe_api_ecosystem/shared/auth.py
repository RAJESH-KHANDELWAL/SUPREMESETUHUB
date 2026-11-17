"""Authentication boundary. Implement a grant only after product entitlement is known."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
import os

class AccessTokenProvider(Protocol):
    def get_access_token(self) -> str:
        """Return a short-lived access token from a secure token store."""

@dataclass(frozen=True)
class AdobeOAuthReadiness:
    client_id_present: bool
    client_secret_present: bool

    @property
    def configured(self) -> bool:
        return self.client_id_present and self.client_secret_present

def oauth_readiness(environ: dict[str, str] | None = None) -> AdobeOAuthReadiness:
    """Report secret presence only; this does not validate OAuth or API access."""
    values = os.environ if environ is None else environ
    return AdobeOAuthReadiness(
        client_id_present=bool(values.get("ADOBE_CLIENT_ID")),
        client_secret_present=bool(values.get("ADOBE_CLIENT_SECRET")),
    )
