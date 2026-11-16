from backend.database.service import DatabaseService
from backend.digital_marketplace.service import DigitalMarketplaceService


def make_service(tmp_path):
    return DigitalMarketplaceService(DatabaseService(str(tmp_path / "digital-marketplace.db")))


def test_digital_catalog_is_flexible_and_does_not_expose_private_key(tmp_path):
    service = make_service(tmp_path)
    saved = service.save_design({
        "title": "Bharat Cosmic Art Pack",
        "category": "digital-art",
        "asset_type": "BUNDLE",
        "file_format": "ZIP",
        "preview_url": "https://assets.example.test/previews/cosmic.webp",
        "private_storage_key": "private/digital/cosmic.zip",
        "tags": ["space", "bharat", "abstract"],
        "prices": {"IN": 19900, "GLOBAL": 499},
        "status": "PUBLISHED",
    })

    india = service.catalog("IN", category="digital-art", search="bharat")
    global_catalog = service.catalog("GLOBAL", search="cosmic")

    assert saved["status"] == "PUBLISHED"
    assert india["currency"] == "INR"
    assert india["count"] == 1
    assert india["designs"][0]["asset_type"] == "BUNDLE"
    assert india["designs"][0]["tags"] == ["space", "bharat", "abstract"]
    assert "private_storage_key" not in india["designs"][0]
    assert global_catalog["currency"] == "USD"
    assert global_catalog["designs"][0]["price"] == "4.99"
    assert global_catalog["product_model"] == "FLEXIBLE_DIGITAL_ASSETS_ONLY"


def test_draft_is_not_public_and_market_prices_are_required(tmp_path):
    service = make_service(tmp_path)
    service.save_design({
        "title": "Draft Wallpaper",
        "category": "wallpaper",
        "private_storage_key": "private/wallpaper.png",
        "prices": {"IN": 9900},
        "status": "DRAFT",
    })
    assert service.catalog("IN")["count"] == 0


def test_rejects_non_https_preview_and_invalid_market_price(tmp_path):
    service = make_service(tmp_path)
    base = {
        "title": "Test Asset",
        "category": "art",
        "private_storage_key": "private/test.png",
        "prices": {"IN": 100},
    }
    try:
        service.save_design({**base, "preview_url": "http://unsafe.example.test/image.png"})
        assert False, "expected preview URL validation"
    except ValueError as exc:
        assert "HTTPS" in str(exc)

    try:
        service.save_design({**base, "prices": {"IN": 0}})
        assert False, "expected positive price validation"
    except ValueError as exc:
        assert "POSITIVE" in str(exc)
