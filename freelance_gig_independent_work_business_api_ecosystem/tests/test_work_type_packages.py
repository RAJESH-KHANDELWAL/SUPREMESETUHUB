"""Validate that every canonical freelance work type has its own API package."""
import importlib
import unittest
from pkgutil import iter_modules

from .. import SUBCATEGORY_IDS


DOMAIN_PACKAGE = __package__.rsplit(".", 1)[0]


class IndependentWorkTypePackageTests(unittest.TestCase):
    def test_every_work_type_has_its_own_package_and_router(self):
        total = 0
        for specialization_id in SUBCATEGORY_IDS:
            specialization = importlib.import_module(
                f"{DOMAIN_PACKAGE}.{specialization_id}"
            )
            source = importlib.import_module(
                f"{DOMAIN_PACKAGE}.{specialization_id}.work_types"
            )
            expected_ids = {item["id"] for item in source.WORK_TYPES}
            child_ids = {
                child.name
                for child in iter_modules(specialization.__path__)
                if child.ispkg and child.name not in {"tests", "__pycache__"}
            }
            self.assertEqual(child_ids, expected_ids, specialization_id)

            for work_type_id in expected_ids:
                package = importlib.import_module(
                    f"{DOMAIN_PACKAGE}.{specialization_id}.{work_type_id}"
                )
                self.assertEqual(package.WORK_TYPE_ID, work_type_id)
                self.assertTrue(
                    package.get_work_type_status()["success"],
                    f"{specialization_id}/{work_type_id}",
                )
                child_router = importlib.import_module(
                    f"{DOMAIN_PACKAGE}.{specialization_id}.{work_type_id}.routes"
                ).router
                self.assertTrue(child_router.routes)
            total += len(expected_ids)

        self.assertEqual(total, 152)

    def test_work_type_packages_are_independently_mounted(self):
        for specialization_id in SUBCATEGORY_IDS:
            routes = importlib.import_module(
                f"{DOMAIN_PACKAGE}.{specialization_id}.routes"
            ).router
            source = importlib.import_module(
                f"{DOMAIN_PACKAGE}.{specialization_id}.work_types"
            )
            # The specialization router owns five top-level endpoints and
            # includes one independent child router per canonical work type.
            self.assertGreaterEqual(
                len(routes.routes),
                5 + len(source.WORK_TYPES),
                specialization_id,
            )


if __name__ == "__main__":
    unittest.main()
