"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMMonitoringActivityTrackerCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_monitoring_activity_tracker"
