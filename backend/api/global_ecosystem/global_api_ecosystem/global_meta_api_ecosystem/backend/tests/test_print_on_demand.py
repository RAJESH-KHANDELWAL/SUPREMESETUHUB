from __future__ import annotations

from backend.database.service import DatabaseService
from backend.print_on_demand.service import PrintOnDemandService


def make_service(tmp_path):
    db = DatabaseService(db_path=str(tmp_path / "pod-test.db"))
    return PrintOnDemandService(database=db)


def test_catalog_has_india_and_global_market_prices(tmp_path):
    service = make_service(tmp_path)
    india = service.catalog("IN")
    global_market = service.catalog("GLOBAL")

    assert india["currency"] == "INR"
    assert global_market["currency"] == "USD"
    assert len(india["products"]) >= 5
    assert india["trend_data_status"] == "EDITORIAL_STARTERS_NOT_LIVE_TREND_DATA"


def test_premium_tier_costs_more_and_quantity_total_is_correct(tmp_path):
    service = make_service(tmp_path)
    standard = service.quote("POD-TEE", "IN", "STANDARD", 3, 1)
    premium = service.quote("POD-TEE", "IN", "PREMIUM", 3, 1)
    bulk = service.quote("POD-TEE", "IN", "STANDARD", 3, 100)

    assert premium["unit_price"] > standard["unit_price"]
    assert bulk["total_price"] == bulk["unit_price"] * 100
    assert bulk["currency"] == "INR"


def test_demand_score_increases_price_without_exceeding_product_cap(tmp_path):
    service = make_service(tmp_path)
    low = service.quote("POD-MUG", "GLOBAL", "STANDARD", 1, 1)
    high = service.quote("POD-MUG", "GLOBAL", "STANDARD", 5, 1)

    assert high["unit_price"] >= low["unit_price"]
    assert high["unit_price"] <= 39


def test_design_brief_is_persisted_and_scoped_to_owner(tmp_path):
    service = make_service(tmp_path)
    created = service.create_brief(
        user_id="user-a", product_sku="POD-TEE", market="IN", tier="STANDARD",
        quantity=2, demand_score=3, design_prompt="Original blue Bharat-inspired geometric art",
    )

    own = service.list_briefs("user-a")
    other = service.list_briefs("user-b")
    assert created["status"] == "DRAFT"
    assert created["quote"]["total_price"] == created["quote"]["unit_price"] * 2
    assert len(own) == 1
    assert own[0]["brief_id"] == created["brief_id"]
    assert other == []


def test_invalid_product_and_quantity_are_rejected(tmp_path):
    service = make_service(tmp_path)
    try:
        service.quote("UNKNOWN", "IN")
    except ValueError as exc:
        assert str(exc) == "UNKNOWN_PRODUCT_SKU"
    else:
        raise AssertionError("Unknown products must be rejected")

    try:
        service.quote("POD-TEE", "IN", quantity=101)
    except ValueError as exc:
        assert str(exc) == "QUANTITY_MUST_BE_BETWEEN_1_AND_100"
    else:
        raise AssertionError("Out-of-range quantities must be rejected")
