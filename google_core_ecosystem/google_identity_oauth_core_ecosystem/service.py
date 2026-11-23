"""GOOGLE-IDENTITY-OAUTH-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleIdentityOAuthCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-IDENTITY-OAUTH-CORE-ECOSYSTEM"


__all__ = ["GoogleIdentityOAuthCoreService"]
