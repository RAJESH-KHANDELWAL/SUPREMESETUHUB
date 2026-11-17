"""Deterministic storage provider registry; no provider calls."""
from .contracts import StorageProvider
ROOT="backend/core/global_ecosystem/global_core_ecosystem/global_storage_core_ecosystem"
_PROVIDERS=(
 StorageProvider("apple","Apple",f"{ROOT}/apple_storage_core_ecosystem",("DEVICE_BACKUP","FILE_SYNC","APP_DATA_STORAGE"),("ICLOUD_DRIVE_METADATA","DEVICE_BACKUP_METADATA","APP_DATA_STORAGE_METADATA")),
 StorageProvider("aws","Amazon Web Services",f"{ROOT}/aws_storage_core_ecosystem",("OBJECT_STORAGE","ARCHIVE","FILE_STORAGE","BLOCK_STORAGE"),("S3_OBJECT_STORAGE","GLACIER_ARCHIVE","EFS_FILE_STORAGE","EBS_BLOCK_STORAGE")),
 StorageProvider("digitalocean","DigitalOcean",f"{ROOT}/digitalocean_storage_core_ecosystem",("OBJECT_STORAGE","BLOCK_STORAGE","BACKUP"),("SPACES_OBJECT_STORAGE","VOLUMES_BLOCK_STORAGE","SNAPSHOT_METADATA")),
 StorageProvider("google","Google",f"{ROOT}/google_storage_core_ecosystem",("OBJECT_STORAGE","FILE_STORAGE","USER_FILE_STORAGE","BACKUP"),("CLOUD_STORAGE_OBJECTS","DRIVE_FILE_METADATA","BACKUP_METADATA","BUCKET_POLICY_METADATA")),
 StorageProvider("microsoft","Microsoft",f"{ROOT}/microsoft_storage_core_ecosystem",("OBJECT_STORAGE","USER_FILE_STORAGE","FILE_SHARES","BACKUP"),("AZURE_BLOB_STORAGE","AZURE_FILES_METADATA","ONEDRIVE_FILE_METADATA","BACKUP_METADATA")),
)
_INDEX={p.provider_id:p for p in _PROVIDERS}
def list_providers(*,include_disabled=False):
 return [p.to_dict() for p in sorted(_PROVIDERS,key=lambda x:x.provider_id) if include_disabled or p.status!="DISABLED"]
def get_provider(provider_id):
 if not isinstance(provider_id,str): return None
 p=_INDEX.get(provider_id.strip().lower())
 return p.to_dict() if p else None
