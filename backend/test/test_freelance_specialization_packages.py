import importlib
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_freelancer_gig_independent_work_business_api_ecosystem import SUBCATEGORY_IDS

PACKAGE = "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_freelancer_gig_independent_work_business_api_ecosystem"

def _registered_paths(router):
    paths = set()
    for route in router.routes:
        path = getattr(route, "path", None)
        if path:
            paths.add(path)
        included_router = getattr(route, "original_router", None)
        include_context = getattr(route, "include_context", None)
        prefix = getattr(include_context, "prefix", "")
        for child in getattr(included_router, "routes", ()):
            child_path = getattr(child, "path", None)
            if child_path:
                paths.add(f"{prefix}{child_path}")
    return paths


class FreelanceSpecializationPackageTests(unittest.TestCase):
    def test_each_specialization_has_independent_layers(self):
        self.assertEqual(len(SUBCATEGORY_IDS), 25)
        self.assertEqual(len(SUBCATEGORY_IDS), len(set(SUBCATEGORY_IDS)))
        for specialization_id in SUBCATEGORY_IDS:
            package = f"{PACKAGE}.{specialization_id}"
            definition = importlib.import_module(package)
            work_types = importlib.import_module(f"{package}.work_types").WORK_TYPES
            catalog = importlib.import_module(f"{package}.catalog")
            services = importlib.import_module(f"{package}.services")
            routes = importlib.import_module(f"{package}.routes").router
            validators = importlib.import_module(f"{package}.validators")
            self.assertEqual(definition.SPECIALIZATION_ID, specialization_id)
            self.assertTrue(work_types, specialization_id)
            self.assertEqual(len(work_types), len({item["id"] for item in work_types}), specialization_id)
            self.assertEqual(len(catalog.list_work_types()), len(work_types), specialization_id)
            self.assertEqual(services.get_status()["work_type_count"], len(work_types), specialization_id)
            self.assertTrue(routes.routes, specialization_id)
            self.assertTrue(validators.validate_work_types()["structurally_valid"], specialization_id)

    def test_aggregate_router_mounts_all_specializations(self):
        router = importlib.import_module(f"{PACKAGE}.specializations").router
        paths = _registered_paths(router)
        for specialization_id in SUBCATEGORY_IDS:
            self.assertIn(f"/freelance/specializations/{specialization_id}", paths)

if __name__ == "__main__":
    unittest.main()
