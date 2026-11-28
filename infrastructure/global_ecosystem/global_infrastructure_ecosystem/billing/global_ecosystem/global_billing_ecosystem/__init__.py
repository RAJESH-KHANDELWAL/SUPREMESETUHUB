"""Billing Global Ecosystem package."""
from .manager import BillingEcosystemManager, get_manager
ECOSYSTEM_ID = "global-billing-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "BillingEcosystemManager", "get_manager"]
