"""Manager for the Observability and Audit AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class ObservabilityAndAuditDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="OBSERVABILITY_AND_AUDIT"
def get_manager()->ObservabilityAndAuditDomainManager:return ObservabilityAndAuditDomainManager()
__all__=["ObservabilityAndAuditDomainManager","get_manager"]
