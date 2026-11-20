"""Load Balancer Global Ecosystem package."""
from .manager import LoadBalancerEcosystemManager, get_manager
ECOSYSTEM_ID = "global-load-balancer-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "LoadBalancerEcosystemManager", "get_manager"]
