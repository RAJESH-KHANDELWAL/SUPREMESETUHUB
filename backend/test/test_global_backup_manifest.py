"""Tests for provider-neutral backup manifest integrity controls."""
import tempfile
import unittest
from pathlib import Path

from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.backup.global_ecosystem.global_backup_ecosystem.backup_manifest import (
    build_manifest,
    verify_manifest,
)


class BackupManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "alpha.txt").write_text("alpha", encoding="utf-8")
        (self.root / "nested").mkdir()
        (self.root / "nested" / "beta.bin").write_bytes(b"\\x00\\x01beta")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_builds_sorted_sha256_manifest(self):
        manifest = build_manifest(
            self.root, ["nested/beta.bin", "alpha.txt"], created_at="2026-11-24T00:00:00Z"
        )
        self.assertEqual([item["path"] for item in manifest["files"]], ["alpha.txt", "nested/beta.bin"])
        self.assertEqual(manifest["algorithm"], "sha256")
        self.assertTrue(verify_manifest(self.root, manifest)["valid"])

    def test_detects_modified_file(self):
        manifest = build_manifest(self.root, ["alpha.txt"])
        (self.root / "alpha.txt").write_text("changed", encoding="utf-8")
        result = verify_manifest(self.root, manifest)
        self.assertFalse(result["valid"])
        self.assertTrue(any("mismatch" in error for error in result["errors"]))

    def test_detects_missing_file(self):
        manifest = build_manifest(self.root, ["alpha.txt"])
        (self.root / "alpha.txt").unlink()
        result = verify_manifest(self.root, manifest)
        self.assertFalse(result["valid"])
        self.assertIn("alpha.txt: missing file", result["errors"])

    def test_rejects_path_traversal(self):
        with self.assertRaises(ValueError):
            build_manifest(self.root, ["../outside.txt"])

    def test_rejects_duplicate_paths(self):
        with self.assertRaises(ValueError):
            build_manifest(self.root, ["alpha.txt", "alpha.txt"])

    def test_rejects_corrupt_manifest_digest(self):
        manifest = build_manifest(self.root, ["alpha.txt"])
        manifest["files"][0]["sha256"] = "not-a-digest"
        result = verify_manifest(self.root, manifest)
        self.assertFalse(result["valid"])
        self.assertIn("alpha.txt: invalid SHA-256 digest", result["errors"])


if __name__ == "__main__":
    unittest.main()
