"""Thin product metadata adapter; API and ENGINE work remain in their layers."""
from ..module_service import IBMProductCoreService
class IBMBillingUsageCostCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_billing_usage_cost"
