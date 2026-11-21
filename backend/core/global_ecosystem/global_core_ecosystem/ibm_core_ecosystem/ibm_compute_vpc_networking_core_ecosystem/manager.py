"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMComputeVpcNetworkingCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("COMPUTE_VPC_NETWORKING")
