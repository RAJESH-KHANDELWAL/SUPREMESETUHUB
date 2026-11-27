"""Contract tests for the singular directory layout of Domain Core providers."""

from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[6]
PROVIDER_ROOT = (
    REPOSITORY_ROOT
    / "backend"
    / "core"
    / "global_ecosystem"
    / "global_core_ecosystem"
    / "global_domain_core_ecosystem"
)
PROVIDERS = (
    "abelohost_domain_core_ecosystem",
    "acme_domain_core_ecosystem",
    "afilias_domain_core_ecosystem",
    "afraid_domain_core_ecosystem",
)
REQUIRED_DIRECTORIES = ("event", "model", "schema", "service", "test")
OBSOLETE_DIRECTORIES = ("events", "models", "schemas", "services", "tests")


class GlobalDomainCoreDirectoryContractTests(unittest.TestCase):
    def test_all_provider_packages_exist(self):
        for provider in PROVIDERS:
            with self.subTest(provider=provider):
                self.assertTrue((PROVIDER_ROOT / provider).is_dir())

    def test_all_providers_use_required_singular_directories(self):
        for provider in PROVIDERS:
            provider_path = PROVIDER_ROOT / provider
            with self.subTest(provider=provider):
                for directory in REQUIRED_DIRECTORIES:
                    with self.subTest(directory=directory):
                        self.assertTrue(
                            (provider_path / directory).is_dir(),
                            f"Missing required directory: {provider}/{directory}",
                        )

    def test_no_provider_retains_obsolete_plural_directories(self):
        for provider in PROVIDERS:
            provider_path = PROVIDER_ROOT / provider
            with self.subTest(provider=provider):
                for directory in OBSOLETE_DIRECTORIES:
                    with self.subTest(directory=directory):
                        self.assertFalse(
                            (provider_path / directory).exists(),
                            f"Obsolete directory remains: {provider}/{directory}",
                        )


if __name__ == "__main__":
    unittest.main()
