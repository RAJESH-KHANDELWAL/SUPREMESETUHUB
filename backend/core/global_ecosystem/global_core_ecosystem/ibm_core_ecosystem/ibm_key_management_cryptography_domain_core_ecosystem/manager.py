"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMKeyManagementCryptographyCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("KEY_MANAGEMENT_CRYPTOGRAPHY")
