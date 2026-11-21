"""Thin product metadata adapter; API and ENGINE work remain in their layers."""
from ..module_service import IBMProductCoreService
class IBMKubernetesContainersCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_kubernetes_containers"
