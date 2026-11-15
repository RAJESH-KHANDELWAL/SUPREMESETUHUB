"""Local metadata/readiness service; no Adobe API calls."""
from .models import StorageObjectRecord
from .registry import StorageMetadataRegistry
ECOSYSTEM_ID="lightroom"
ECOSYSTEM_NAME="Adobe Lightroom Storage"
RELATED_API_FAMILY="Requires validation of currently supported Lightroom API"
class StorageEcosystemService:
    def __init__(self,*,enabled:bool=True,registry:StorageMetadataRegistry|None=None):self.enabled=bool(enabled);self.registry=registry or StorageMetadataRegistry()
    def describe(self)->dict:
        return {"provider_id":"adobe","ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"enabled":self.enabled,"implementation_state":"FOUNDATION_INITIALIZED","connection_state":"NOT_CONFIGURED","external_connections_verified":False,"related_api_family":RELATED_API_FAMILY,"capabilities":["IDENTITY","METADATA_MODEL","IN_MEMORY_METADATA_REGISTRY"]}
    def health(self)->dict:
        return {"success":self.enabled,"ecosystem_id":ECOSYSTEM_ID,"status":"FOUNDATION_READY" if self.enabled else "DISABLED","connection_state":"NOT_CONFIGURED","external_connections_verified":False,"metadata_records":self.registry.count()}
    def register_metadata(self,record:StorageObjectRecord)->dict:
        if record.provider_id!="adobe" or record.ecosystem_id!=ECOSYSTEM_ID:raise ValueError("RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH")
        return self.registry.register(record)
