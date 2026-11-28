"""Shared read-only service for individual Oracle product packages."""
from .product_catalog import get_product

class OracleProductCoreService:
    def __init__(self, product_id: str) -> None:
        self.product = get_product(product_id)
        if self.product is None:
            raise KeyError(f"Unknown Oracle product: {product_id}")

    def describe(self) -> dict:
        return dict(self.product)

    def status(self) -> dict:
        return {"product": self.describe(), "status": "CATALOG_ONLY", "live_connection_verified": False}

    def capabilities(self) -> list[str]:
        return ["PRODUCT_DISCOVERY", "CAPABILITY_METADATA", "DOMAIN_CLASSIFICATION", "READINESS_METADATA"]
