"""Service layer for GLOBAL APP API ECOSYSTEM."""

from datetime import datetime, timezone


class EcosystemService:
    ECOSYSTEM_ID = "global-app"
    ECOSYSTEM_NAME = "GLOBAL APP API ECOSYSTEM"
    VERSION = "1.0.0"
    PROVIDERS = (
        {"provider_id": "aws", "provider_name": "AWS", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "adobe", "provider_name": "Adobe", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "apple", "provider_name": "Apple", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "google", "provider_name": "Google", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "shopify", "provider_name": "Shopify", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "microsoft", "provider_name": "Microsoft", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
        {"provider_id": "cloudflare", "provider_name": "Cloudflare", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    )

    def get_status(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "ecosystem_name": self.ECOSYSTEM_NAME, "version": self.VERSION, "status": "catalog_available", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False, "provider_count": len(self.PROVIDERS), "timestamp": datetime.now(timezone.utc).isoformat()}

    def list_providers(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(self.PROVIDERS), "providers": list(self.PROVIDERS)}

    def get_provider(self, provider_id: str):
        key = provider_id.strip().casefold()
        return next((item for item in self.PROVIDERS if item["provider_id"] == key), None)

    def search_providers(self, query: str):
        term = query.strip().casefold()
        return [item for item in self.PROVIDERS if term in item["provider_id"] or term in item["provider_name"].casefold()]
