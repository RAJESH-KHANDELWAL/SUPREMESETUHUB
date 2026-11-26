"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMIamIdentityAccessCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("IAM_IDENTITY_ACCESS")
