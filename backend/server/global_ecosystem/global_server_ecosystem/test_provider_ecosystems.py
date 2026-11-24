"""Tests for canonical provider-wise SERVER ecosystem namespaces."""
import importlib
import unittest

from .catalog import get_provider_catalog, list_providers, list_service_types

BASE = "backend.server.global_ecosystem.global_server_ecosystem"
PROVIDER_IDS = (
    "abelohost", "aws", "azure", "cloudflare", "digitalocean",
    "google", "hostinger", "microsoft", "vicetemple",
)
SERVICE_SUFFIXES = (
    "vpn", "vps", "cloud", "web", "cloud_web", "dedicated",
    "edge", "application", "database",
)


class ProviderEcosystemStructureTests(unittest.TestCase):
    def test_catalog_points_to_canonical_provider_packages(self):
        rows = {row.provider_id: row for row in get_provider_catalog()}
        self.assertEqual(set(PROVIDER_IDS), set(rows))
        for provider_id in PROVIDER_IDS:
            self.assertEqual(
                rows[provider_id].package,
                f"{provider_id}_server_server_ecosystem",
            )

    def test_every_provider_package_imports_and_declares_identity(self):
        for provider_id in PROVIDER_IDS:
            with self.subTest(provider=provider_id):
                module = importlib.import_module(
                    f"{BASE}.{provider_id}_server_ecosystem"
                )
                self.assertEqual(module.PROVIDER_ID, provider_id)
                self.assertEqual(module.OWNING_DOMAIN, "SERVER")
                self.assertTrue(module.DISPLAY_NAME)

    def test_server_layer_packages_follow_sibling_layer_convention(self):
        for provider_id in PROVIDER_IDS:
            with self.subTest(provider=provider_id):
                module = importlib.import_module(
                    f"{BASE}.{provider_id}_server_server_ecosystem"
                )
                self.assertEqual(module.PROVIDER_ID, provider_id)
                self.assertEqual(module.OWNING_DOMAIN, "SERVER")
                self.assertTrue(module.DISPLAY_NAME)
                self.assertTrue(callable(module.ADAPTER_CLASS))
                self.assertEqual(module.LAYER, "SERVER")
                self.assertEqual(module.PACKAGE_KIND, "PROVIDER_SERVER_ECOSYSTEM")
                description = module.describe_server_provider()
                self.assertEqual(description["provider_id"], provider_id)
                self.assertEqual(description["connection_status"], "NOT_PROBED")

    def test_every_provider_has_all_service_family_namespaces(self):
        expected_types = {item["service_type_id"] for item in list_service_types()}
        self.assertEqual(len(expected_types), len(SERVICE_SUFFIXES))
        for provider_id in PROVIDER_IDS:
            for suffix in SERVICE_SUFFIXES:
                with self.subTest(provider=provider_id, service=suffix):
                    module = importlib.import_module(
                        f"{BASE}.{provider_id}_server_ecosystem."
                        f"{provider_id}_{suffix}_server_ecosystem"
                    )
                    self.assertEqual(module.PROVIDER_ID, provider_id)
                    self.assertEqual(module.OWNING_DOMAIN, "SERVER")
                    self.assertEqual(module.EXECUTION_MODE, "EXPLICIT_ADAPTER_REQUIRED")
                    self.assertIn(module.SERVICE_TYPE_ID, expected_types)


    def test_canonical_provider_classes_are_exported_from_public_package(self):
        public = importlib.import_module(BASE)
        expected_exports = (
            "AbelohostServerProvider", "AWSServerEcosystem",
            "AzureAdditionalServerEcosystem", "CloudflareServerProvider",
            "DigitalOceanServerEcosystem", "GoogleServerEcosystem",
            "HostingerServerEcosystem", "MicrosoftServerProvider",
            "ViceTempleServerProvider",
        )
        for export in expected_exports:
            with self.subTest(export=export):
                self.assertTrue(hasattr(public, export), export)

    def test_catalog_exposes_canonical_package_names(self):
        packages = {row["provider_id"]: row["package"] for row in list_providers()}
        for provider_id in PROVIDER_IDS:
            self.assertEqual(packages[provider_id], f"{provider_id}_server_server_ecosystem")


if __name__ == "__main__":
    unittest.main()
