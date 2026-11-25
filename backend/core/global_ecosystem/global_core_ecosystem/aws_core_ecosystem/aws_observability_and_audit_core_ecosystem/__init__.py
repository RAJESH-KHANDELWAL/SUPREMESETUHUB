"""Observability and Audit AWS Core domain package."""
from .manager import ObservabilityAndAuditDomainManager,get_manager
DOMAIN_ID="OBSERVABILITY_AND_AUDIT"
__all__=["DOMAIN_ID","ObservabilityAndAuditDomainManager","get_manager"]
