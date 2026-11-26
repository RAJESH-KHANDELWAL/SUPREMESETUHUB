"""GitHub family discovery and dependency orchestration; no provider calls."""
from .catalog import get_github_core_catalog, list_github_families
from .policy import GitHubCorePolicy
from .product_catalog import github_offerings_summary, get_github_offering


class GitHubCoreOrchestrator:
    """Coordinate GitHub family metadata without provider API calls."""

    def catalog(self):
        return get_github_core_catalog()

    def list_families(self, enabled_only=False):
        items = list_github_families()
        if enabled_only:
            items = [item for item in items if item.get("enabled", True)]
        safe = [GitHubCorePolicy.safe_summary(item) for item in items]
        return {"success": True, "count": len(safe), "families": safe}

    def get_family(self, family):
        needle = str(family).strip().casefold()
        if not needle:
            return None
        return next(
            (
                GitHubCorePolicy.safe_summary(item)
                for item in list_github_families()
                if item["family"].casefold() == needle
                or item["name"].casefold() == needle
                or item["ecosystem_id"].casefold() == needle
            ),
            None,
        )

    def health(self):
        catalog = self.catalog()
        items = catalog["children"]
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "family_count": len(items),
            "enabled_family_count": sum(bool(item.get("enabled", True)) for item in items),
            "families_with_existing_api_routes": sum(
                bool(item.get("family_api_routes_implemented")) for item in items
            ),
            "live_connections_verified_by_core": 0,
            "api_calls_performed_by_core": 0,
            "warning": (
                "Catalog registration and shared transport do not prove complete "
                "family endpoint coverage, caller authorization or live authentication."
            ),
        }

    def offerings(self):
        return github_offerings_summary()

    def get_offering(self, family):
        return get_github_offering(family)

    def dependency_map(self):
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["core_module"],
                    "api_catalog_ref": item.get("api_catalog_ref"),
                    "api_transport_ref": item.get("shared_api_transport_ref"),
                    "relationship": "DELEGATES_TO_API_INTEGRATION_LAYER",
                }
                for item in list_github_families()
            ],
        }


__all__ = ["GitHubCoreOrchestrator"]
