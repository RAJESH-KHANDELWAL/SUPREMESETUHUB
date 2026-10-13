from __future__ import annotations

from backend.database.service import DatabaseService
from backend.digital_marketplace.service import DigitalMarketplaceService


def make_service(tmp_path):
    db = DatabaseService(db_path=str(tmp_path / "digital-marketplace-test.db"))
    return DigitalMarketplaceService(database=db)


def seed_design(service, *, status="PUBLISHED", market="IN", price_minor=49900):
    service.database.execute(
        """
        INSERT INTO digital_designs
            (design_id, slug, title, description, category, preview_url,
             private_storage_key, license_label, status, published_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("DSN-001", "blue-bharat-poster", "Blue Bharat Poster",
         "Original digital artwork preview", "POSTER", "/previews/blue-bharat.webp",
         "private/designs/original-001.zip", "Personal digital use",
         status, "2026-10-12T00:00:00Z"),
    )
    service.database.execute(
        """
        INSERT INTO digital_design_prices
            (price_id, design_id, market_code, currency_code, price_minor, is_active)
        VALUES (?, ?, ?, ?, ?, 1)
        """,
        ("PRICE-001", "DSN-001", market, "INR" if market == "IN" else "USD", price_minor),
    )


def test_catalog_returns_only_published_designs_and_never_private_storage_key(tmp_path):
    service = make_service(tmp_path)
    seed_design(service)
    result = service.catalog("IN")

    assert result["currency"] == "INR"
    assert result["product_model"] == "FLEXIBLE_DIGITAL_ASSETS_ONLY"
    assert result["count"] == 1
    assert result["designs"][0]["price"] == "499.00"
    assert "private_storage_key" not in result["designs"][0]
    assert "private/designs/original-001.zip" not in str(result)


def test_draft_design_is_not_public(tmp_path):
    service = make_service(tmp_path)
    seed_design(service, status="DRAFT")

    assert service.catalog("IN")["designs"] == []


def test_market_prices_are_separated(tmp_path):
    service = make_service(tmp_path)
    seed_design(service, market="GLOBAL", price_minor=599)

    assert service.catalog("IN")["designs"] == []
    result = service.catalog("GLOBAL")
    assert result["currency"] == "USD"
    assert result["designs"][0]["price"] == "5.99"


def test_invalid_market_and_pagination_are_rejected(tmp_path):
    service = make_service(tmp_path)
    for args, expected in [
        ({"market": "EU"}, "MARKET_MUST_BE_IN_OR_GLOBAL"),
        ({"limit": 0}, "LIMIT_MUST_BE_BETWEEN_1_AND_100"),
        ({"offset": -1}, "OFFSET_MUST_BE_NON_NEGATIVE"),
    ]:
        try:
            service.catalog(**args)
        except ValueError as exc:
            assert str(exc) == expected
        else:
            raise AssertionError(f"Expected {expected}")
