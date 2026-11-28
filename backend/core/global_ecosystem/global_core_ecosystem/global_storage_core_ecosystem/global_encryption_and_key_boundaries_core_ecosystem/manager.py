"""Read-only domain manager for Encryption and Key Boundaries."""
from ..domain_runtime import StorageCoreDomainManager
class EncryptionAndKeyBoundariesManager(StorageCoreDomainManager):
 DOMAIN_ID="ENCRYPTION_AND_KEY_BOUNDARIES"
def get_manager()->EncryptionAndKeyBoundariesManager: return EncryptionAndKeyBoundariesManager()
