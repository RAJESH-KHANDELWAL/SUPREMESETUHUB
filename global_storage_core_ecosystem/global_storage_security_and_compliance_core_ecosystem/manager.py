"""Read-only domain manager for Storage Security and Compliance."""
from ..domain_runtime import StorageCoreDomainManager
class StorageSecurityAndComplianceManager(StorageCoreDomainManager):
 DOMAIN_ID="STORAGE_SECURITY_AND_COMPLIANCE"
def get_manager()->StorageSecurityAndComplianceManager: return StorageSecurityAndComplianceManager()
