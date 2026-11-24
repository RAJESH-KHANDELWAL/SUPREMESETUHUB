import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from catalog import DOMAIN_CATALOG, FUNCTIONAL_AREAS  # noqa: E402


def test_catalog_ids_and_slugs_are_unique():
    assert len({item["id"] for item in DOMAIN_CATALOG}) == len(DOMAIN_CATALOG)
    assert len({item["slug"] for item in DOMAIN_CATALOG}) == len(DOMAIN_CATALOG)
    assert all(item["status"] == "proposed" for item in DOMAIN_CATALOG)


def test_domain_packages_have_readmes():
    package_root = PACKAGE_ROOT / "domains"
    for item in DOMAIN_CATALOG:
        assert (package_root / item["slug"] / "README.md").is_file()


def test_functional_areas_are_unique():
    assert len(FUNCTIONAL_AREAS) == len(set(FUNCTIONAL_AREAS))
