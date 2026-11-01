"""Unit tests for source-aware global company registry behavior."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from .. import service


class CompanyRegistryTests(unittest.TestCase):
    def _registry(self, records):
        temporary = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".json", delete=False)
        json.dump({"records": records}, temporary)
        temporary.close()
        self.addCleanup(Path(temporary.name).unlink, missing_ok=True)
        return Path(temporary.name)

    def test_search_is_alphabetical_and_letter_filtered(self):
        path = self._registry([
            {"company_id": "b", "name": "Zebra Labs", "entity_type": "registered_company"},
            {"company_id": "a", "name": "Apple Works", "entity_type": "registered_company"},
        ])
        with patch.object(service, "REGISTRY_PATH", path):
            result = service.search_companies(letter="a")
        self.assertEqual([item["company_id"] for item in result["items"]], ["a"])

    def test_alphabet_counts(self):
        path = self._registry([
            {"company_id": "a", "name": "Apple", "entity_type": "registered_company"},
            {"company_id": "b", "name": "Amazon", "entity_type": "registered_company"},
            {"company_id": "z", "name": "Zebra", "entity_type": "registered_company"},
        ])
        with patch.object(service, "REGISTRY_PATH", path):
            result = service.get_company_alphabet()
        self.assertEqual(result["total"], 3)
        self.assertEqual(result["letters"]["A"], 2)
        self.assertEqual(result["letters"]["Z"], 1)

    def test_verified_record_requires_source_url(self):
        path = self._registry([
            {
                "company_id": "verified-1",
                "name": "Example Corp",
                "entity_type": "registered_company",
                "verification_status": "registry_verified",
            }
        ])
        with patch.object(service, "REGISTRY_PATH", path):
            with self.assertRaisesRegex(ValueError, "must include source_urls"):
                service.load_company_registry()


    def test_country_source_directory_and_country_filter(self):
        with patch.object(service, "PACKAGE_DIR", Path(__file__).resolve().parents[1]):
            result = service.list_country_sources("IN")
        self.assertEqual(result["registry_status"], "source_directory_only")
        self.assertTrue(result["items"])
        self.assertTrue(all(item["country_code"] == "IN" for item in result["items"]))

    def test_country_source_ids_are_unique(self):
        source_path = Path(__file__).resolve().parents[1] / "data" / "country_sources.json"
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        payload["sources"].append(dict(payload["sources"][0]))
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir = Path(temp_dir)
            data_dir = package_dir / "data"
            data_dir.mkdir()
            (data_dir / "country_sources.json").write_text(json.dumps(payload), encoding="utf-8")
            with patch.object(service, "PACKAGE_DIR", package_dir):
                with self.assertRaisesRegex(ValueError, "Duplicate source_id"):
                    service.load_country_sources()

    def test_duplicate_company_ids_are_rejected(self):
        path = self._registry([
            {"company_id": "duplicate", "name": "One", "entity_type": "registered_company"},
            {"company_id": "duplicate", "name": "Two", "entity_type": "registered_company"},
        ])
        with patch.object(service, "REGISTRY_PATH", path):
            with self.assertRaisesRegex(ValueError, "Duplicate company_id"):
                service.load_company_registry()


if __name__ == "__main__":
    unittest.main()
