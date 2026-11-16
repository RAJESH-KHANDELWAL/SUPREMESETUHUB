from ..catalog import validate_catalog
from ..service import ArtsCultureHeritageService


def test_catalog_integrity_and_detail():
    service = ArtsCultureHeritageService()
    items = service.list_categories()
    assert len(items) == 16
    assert len({item["id"] for item in items}) == len(items)
    assert validate_catalog()["valid"]
    assert service.get_category("cultural_heritage_sites")["id"] == "cultural_heritage_sites"


def test_search_and_channel_filters():
    service = ArtsCultureHeritageService()
    assert any(item["id"] == "handicrafts_traditional_crafts" for item in service.list_categories(query="handicrafts"))
    offline = service.list_categories(channel="offline")
    assert offline and all("offline" in item["channels"] for item in offline)


def test_unknown_category_and_status():
    service = ArtsCultureHeritageService()
    assert service.get_category("not_a_category") is None
    assert service.get_status()["domain_id"] == "arts_culture_heritage_creative_economy"
