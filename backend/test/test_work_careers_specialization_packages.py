import importlib
import pkgutil
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.categories import CATEGORY_DEFINITIONS
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.specialization_routes import router

PACKAGE = "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem"

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


class WorkCareerSpecializationTests(unittest.TestCase):
    def test_every_direct_specialization_folder_is_registered(self):
        mounted_paths = _registered_paths(router)
        total = 0
        for category in CATEGORY_DEFINITIONS:
            category_id = category["id"]
            package = importlib.import_module(f"{PACKAGE}.{category_id}")
            folder_ids = {item.name for item in pkgutil.iter_modules(package.__path__) if item.ispkg and item.name not in {"tests", "__pycache__"}}
            catalogue = importlib.import_module(f"{PACKAGE}.{category_id}.categories")
            registered_ids = {item["id"] for item in catalogue.list_tracks()}
            self.assertEqual(folder_ids, registered_ids, category_id)
            for specialization_id in folder_ids:
                category_slug = category_id.replace("_", "-")
                path_prefix = f"/work-careers/{category_slug}/{specialization_id}"
                self.assertTrue(any(path.startswith(path_prefix) for path in mounted_paths), path_prefix)
                total += 1
        self.assertGreater(total, 80)

if __name__ == "__main__":
    unittest.main()
