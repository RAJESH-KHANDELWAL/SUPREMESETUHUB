"""Monitoring Global Ecosystem package."""
from .manager import MonitoringEcosystemManager, get_manager
ECOSYSTEM_ID = "global-monitoring-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "MonitoringEcosystemManager", "get_manager"]
