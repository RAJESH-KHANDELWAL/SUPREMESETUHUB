"""Thin family adapter; supply official base URL and a secure token provider."""
from __future__ import annotations
from ..shared.auth import AccessTokenProvider
from ..shared.client import AdobeApiClient

class CreativeCloudAssetsClient(AdobeApiClient):
    """Transport wrapper only; product operations must be added from official docs."""
    def __init__(self, *, base_url: str, token_provider: AccessTokenProvider, timeout: float = 20.0) -> None:
        super().__init__(base_url=base_url, token_provider=token_provider, timeout=timeout)
