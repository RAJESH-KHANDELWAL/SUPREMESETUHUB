"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMMonitoringObservabilityCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("MONITORING_OBSERVABILITY")
