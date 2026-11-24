from __future__ import annotations
import unittest
from backend.global_ecosystem.anthropic_ecosystem import (
    ANTHROPIC_CAPABILITIES, AnthropicEcosystemService, get_capability,
)
from backend.global_ecosystem.anthropic_ecosystem.health import readiness_report

class AnthropicEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = AnthropicEcosystemService()

    def test_catalog_contains_expected_capabilities(self):
        self.assertEqual(set(ANTHROPIC_CAPABILITIES), {
            "messages", "message_batches", "models", "token_counting", "files",
            "admin_workspaces", "managed_agents", "tool_use", "auth_identity",
        })

    def test_catalog_does_not_claim_live_connection(self):
        report = readiness_report()
        self.assertEqual(report["status"], "CATALOG_ONLY")
        self.assertFalse(report["live_connection_verified"])

    def test_get_capability_is_case_insensitive(self):
        self.assertEqual(get_capability("MESSAGES").capability_id, "messages")

    def test_messages_plan_validates_payload(self):
        plan = self.service.plan("messages", "create", {
            "model": "claude-example", "max_tokens": 128,
            "messages": [{"role": "user", "content": "Hello"}],
        })
        self.assertEqual(plan.capability_id, "messages")
        self.assertTrue(plan.metadata["execution_required"])

    def test_messages_plan_rejects_missing_messages(self):
        with self.assertRaises(ValueError):
            self.service.plan("messages", "create", {"model": "x", "max_tokens": 10})

    def test_sensitive_capability_requires_permission(self):
        with self.assertRaises(PermissionError):
            self.service.plan("files", "list")
        plan = self.service.plan("files", "list", metadata={"permission_granted": True})
        self.assertEqual(plan.capability_id, "files")

    def test_inline_secret_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.plan("messages", "create", {
                "model": "x", "max_tokens": 10,
                "messages": [{"role": "user", "content": "hi"}],
                "api_key": "not-allowed",
            })

if __name__ == "__main__":
    unittest.main()
