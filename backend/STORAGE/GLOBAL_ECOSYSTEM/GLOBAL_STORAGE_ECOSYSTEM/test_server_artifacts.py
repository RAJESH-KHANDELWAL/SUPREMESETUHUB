"""Offline tests for STORAGE-owned server artifact metadata."""
import unittest
from .models import ServerArtifact
from .server_artifact_repository import ServerArtifactRepository
from .service import EcosystemService

def artifact(artifact_id="backup-1"):
    return ServerArtifact(artifact_id,"server-1","backup","s3","bucket/server-1/backup.tar",size_bytes=100)

class StorageServerArtifactTests(unittest.TestCase):
    def test_artifact_metadata_lifecycle(self):
        service=EcosystemService()
        result=service.register_server_artifact(artifact())
        self.assertTrue(result["success"])
        self.assertEqual(service.list_server_artifacts("server-1")["count"],1)
        self.assertEqual(service.update_server_artifact_status("backup-1","READY")["artifact"]["status"],"READY")

    def test_duplicate_invalid_and_copy_isolation(self):
        repo=ServerArtifactRepository()
        created=repo.create(artifact())
        created["metadata"]["changed"]=True
        self.assertNotIn("changed",repo.get("backup-1")["metadata"])
        with self.assertRaises(ValueError): repo.create(artifact())
        with self.assertRaises(ValueError):
            repo.create(ServerArtifact("bad","","","","",size_bytes=-1))

if __name__=="__main__": unittest.main()
