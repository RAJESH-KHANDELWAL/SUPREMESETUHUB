"""Structural and service tests for the Global Organizations API ecosystem."""
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_organizations_api_ecosystem.catalog import (
    LEGAL_FORM_DIMENSIONS, GOVERNANCE_MODELS, GEOGRAPHIC_SCOPES, VERIFICATION_STATES,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_organizations_api_ecosystem.organization_domain_api_ecosystems.registry import ORGANIZATION_DOMAINS
from backend.api.global_ecosystem.global_api_ecosystem.global_organizations_api_ecosystem.organization_type_api_ecosystems.registry import ORGANIZATION_TYPES
from backend.api.global_ecosystem.global_api_ecosystem.global_organizations_api_ecosystem.routes import router
from backend.api.global_ecosystem.global_api_ecosystem.global_organizations_api_ecosystem.service import (
    get_ecosystem_status, load_organization_registry, search_organizations,
)

class GlobalOrganizationsEcosystemTests(unittest.TestCase):
    def test_taxonomies_are_nonempty_and_unique(self):
        self.assertTrue(ORGANIZATION_DOMAINS)
        self.assertTrue(ORGANIZATION_TYPES)
        self.assertEqual(len({x["domain_id"] for x in ORGANIZATION_DOMAINS}), len(ORGANIZATION_DOMAINS))
        self.assertEqual(len({x["type_id"] for x in ORGANIZATION_TYPES}), len(ORGANIZATION_TYPES))

    def test_classification_dimensions_are_nonempty(self):
        self.assertTrue(LEGAL_FORM_DIMENSIONS)
        self.assertTrue(GOVERNANCE_MODELS)
        self.assertTrue(GEOGRAPHIC_SCOPES)
        self.assertTrue(VERIFICATION_STATES)

    def test_registry_is_valid_and_initially_empty(self):
        self.assertEqual(load_organization_registry(), [])
        status = get_ecosystem_status()
        self.assertEqual(status["organization_count"], 0)
        self.assertFalse(status["live_external_connections"])

    def test_search_returns_paginated_empty_directory(self):
        result = search_organizations(limit=10, offset=0)
        self.assertEqual(result["total"], 0)
        self.assertEqual(result["items"], [])

    def test_routes_are_defined(self):
        paths = {route.path for route in router.routes}
        self.assertIn("/global/organizations/status", paths)
        self.assertIn("/global/organizations/search", paths)
        self.assertIn("/global/organizations/integrations", paths)
        self.assertIn("/global/organizations/{organization_id}", paths)

if __name__ == "__main__":
    unittest.main()
