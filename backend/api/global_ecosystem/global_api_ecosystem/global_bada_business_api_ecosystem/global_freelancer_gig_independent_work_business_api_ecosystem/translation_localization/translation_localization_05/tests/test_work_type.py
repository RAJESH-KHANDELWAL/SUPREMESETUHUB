import unittest

from ..categories import (
    SPECIALIZATION_ID,
    WORK_TYPE_ID,
    get_work_type_definition,
    validate_work_type_definition,
)
from ..catalog import get_work_type, serialize_work_type
from ..services import get_work_type_resource, get_work_type_status


class IndependentWorkTypeTests(unittest.TestCase):
    def test_folder_id_resolves_to_parent_canonical_record(self):
        definition = get_work_type_definition()
        self.assertEqual(definition["id"], WORK_TYPE_ID)
        self.assertTrue(definition["name"])
        self.assertTrue(definition["description"])

    def test_catalogue_model_and_serialization(self):
        record = get_work_type()
        payload = serialize_work_type()
        self.assertEqual(record.id, WORK_TYPE_ID)
        self.assertEqual(record.specialization_id, SPECIALIZATION_ID)
        self.assertEqual(payload["id"], WORK_TYPE_ID)
        self.assertEqual(payload["taxonomy_status"], "taxonomy_only")

    def test_service_and_integrity_contracts(self):
        resource = get_work_type_resource()
        status = get_work_type_status()
        self.assertTrue(resource["success"])
        self.assertTrue(status["success"])
        self.assertTrue(validate_work_type_definition()["structurally_valid"])
        self.assertFalse(status["live_gig_available"])


if __name__ == "__main__":
    unittest.main()
