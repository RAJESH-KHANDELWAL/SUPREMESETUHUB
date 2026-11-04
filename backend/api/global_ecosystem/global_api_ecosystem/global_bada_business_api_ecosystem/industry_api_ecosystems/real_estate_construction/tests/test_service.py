from .service import RealEstateService
def test_catalog_and_search():
    s = RealEstateService(); items = s.list_categories()
    assert len(items) >= 10
    assert len({x["id"] for x in items}) == len(items)
    assert s.list_categories(items[0]["id"])
    assert s.get_category(items[0]["id"])["id"] == items[0]["id"]
def test_status():
    assert RealEstateService().get_status()["status"] == "taxonomy_scaffold"
