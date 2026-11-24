"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMSecretsManagementCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("SECRETS_MANAGEMENT")
