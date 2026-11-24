from __future__ import annotations
import unittest
from .. import get_catalog, get_manager, list_language_records, get_language_record, list_programming_language_domains
class ProgrammingLanguageCoreTests(unittest.TestCase):
 def test_manager_status_health_metadata_only(self):
  manager=get_manager();status=manager.status();health=manager.health()
  self.assertTrue(status["success"]);self.assertFalse(status["runtime_execution_verified"])
  self.assertFalse(health["runtime_execution_verified"]);self.assertEqual(health["api_calls_performed"],0)
 def test_catalog_has_26_domains_and_seven_tiers(self):
  catalog=get_catalog();self.assertEqual(catalog["domain_count"],26);self.assertEqual(len(catalog["service_tiers"]),7)
  self.assertEqual([x["name"] for x in catalog["service_tiers"]],["Normal","Basic","Standard","Premium","Professional","Enterprise","Supreme"])
 def test_curated_language_search_lookup(self):
  records=list_language_records();self.assertGreater(len(records),100)
  self.assertIsNotNone(get_language_record("Python"));self.assertIsNotNone(get_language_record("Solidity"))
  self.assertTrue(list_language_records(search="GPU"))
 def test_domains_unique_and_scoped(self):
  domains=list_programming_language_domains();ids=[x["id"] for x in domains]
  self.assertEqual(len(ids),len(set(ids)));self.assertTrue(all(x["scope"].strip() for x in domains))
 def test_returned_catalog_is_copy(self):
  catalog=get_catalog();catalog["languages"].clear();self.assertGreater(len(get_catalog()["languages"]),100)
if __name__=="__main__":unittest.main()
