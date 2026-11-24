from ..service import MarketingMediaEntertainmentService


def test_catalog_and_detail():
    service = MarketingMediaEntertainmentService()
    items = service.list_categories()
    assert len(items) == 16
    assert len({item["id"] for item in items}) == len(items)
    assert service.get_category(items[0]["id"])["id"] == items[0]["id"]


def test_online_offline_and_hybrid_channel_filters():
    service = MarketingMediaEntertainmentService()
    online = service.list_categories(channel="online")
    offline = service.list_categories(channel="offline")
    hybrid = service.list_categories(channel="hybrid")
    assert online and offline and hybrid
    assert all("online" in item["channels"] for item in online)
    assert all("offline" in item["channels"] for item in offline)
    assert all("hybrid" in item["channels"] for item in hybrid)


def test_digital_marketing_is_searchable():
    service = MarketingMediaEntertainmentService()
    assert any(item["id"] == "digital_marketing" for item in service.list_categories(query="SEO"))


def test_status():
    status = MarketingMediaEntertainmentService().get_status()
    assert status["status"] == "taxonomy_scaffold"
    assert status["domain_id"] == "marketing_media_entertainment"
