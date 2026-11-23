"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMActivityTrackingAuditCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("ACTIVITY_TRACKING_AUDIT")
