"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaLoginOauthIdentityCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("LOGIN_OAUTH_IDENTITY")
