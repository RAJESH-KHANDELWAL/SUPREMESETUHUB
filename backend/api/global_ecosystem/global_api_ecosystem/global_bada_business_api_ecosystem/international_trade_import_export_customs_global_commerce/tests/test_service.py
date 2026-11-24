from ..catalog import validate_catalog
from ..service import InternationalTradeService


def test_catalog_integrity_and_detail():
    service = InternationalTradeService()
    items = service.list_categories()
    assert len(items) == 19
    assert len({item["id"] for item in items}) == len(items)
    assert validate_catalog()["valid"]
    assert service.get_category("hs_codes_product_classification")["id"] == "hs_codes_product_classification"


def test_search_and_channel_filters():
    service = InternationalTradeService()
    assert any(item["id"] == "customs_clearance_brokers" for item in service.list_categories(query="customs broker"))
    online = service.list_categories(channel="online")
    assert online and all("online" in item["channels"] for item in online)


def test_unknown_category_and_status():
    service = InternationalTradeService()
    assert service.get_category("unknown") is None
    status = service.get_status()
    assert status["domain_id"] == "international_trade_import_export_customs_global_commerce"
    assert status["category_count"] == 19
