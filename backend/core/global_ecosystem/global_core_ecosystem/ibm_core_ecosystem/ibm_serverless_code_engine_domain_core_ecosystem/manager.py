"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMServerlessCodeEngineCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("SERVERLESS_CODE_ENGINE")
