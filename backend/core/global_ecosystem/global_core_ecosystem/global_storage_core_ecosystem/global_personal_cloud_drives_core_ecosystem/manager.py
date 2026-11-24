"""Read-only domain manager for Personal Cloud Drives."""
from ..domain_runtime import StorageCoreDomainManager
class PersonalCloudDrivesManager(StorageCoreDomainManager):
 DOMAIN_ID="PERSONAL_CLOUD_DRIVES"
def get_manager()->PersonalCloudDrivesManager: return PersonalCloudDrivesManager()
