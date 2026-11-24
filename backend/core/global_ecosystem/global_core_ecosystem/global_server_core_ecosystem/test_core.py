"""Offline tests for SERVER CORE domain contracts."""
import unittest
from .models import ServerIdentity
from .registry import ServerCoreRegistry
from .service import ServerCoreService
from .policy import ServerPolicy

class ServerCoreTests(unittest.TestCase):
    def payload(self, server_id="node-1"):
        return {"server_id":server_id,"provider_id":"AWS","server_type":"VPS",
                "server_role":"application","country":"in","region":"ap-south-1",
                "environment":"test","metadata":{"zone":"a"}}

    def test_identity_registration_normalizes_and_copies(self):
        service=ServerCoreService()
        result=service.register_identity(self.payload())
        self.assertTrue(result["success"])
        result["identity"]["metadata"]["zone"]="mutated"
        stored=service.get_identity("node-1")["identity"]
        self.assertEqual(stored["provider_id"],"aws")
        self.assertEqual(stored["metadata"]["zone"],"a")

    def test_missing_and_duplicate_identity_rejected(self):
        registry=ServerCoreRegistry()
        with self.assertRaises(ValueError): registry.register(ServerIdentity("", "aws","vps","app","IN","west","test"))
        item=ServerIdentity("one","aws","vps","app","IN","west","test")
        registry.register(item)
        with self.assertRaises(ValueError): registry.register(item)

    def test_policy_requires_approval_by_default(self):
        policy=ServerPolicy()
        with self.assertRaises(PermissionError): policy.validate(environment="production")
        policy.validate(environment="production",authorized=True)
        with self.assertRaises(ValueError): policy.validate(environment="sandbox",authorized=True)

    def test_service_reports_core_boundary(self):
        info=ServerCoreService().describe()
        self.assertEqual(info["layer"],"CORE")
        self.assertFalse(info["remote_operations_enabled"])
        self.assertIn("aws",info["provider_domains"])

if __name__=="__main__": unittest.main()
