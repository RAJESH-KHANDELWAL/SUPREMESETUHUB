from .service import TechnologyService
def test_catalog_and_search():
    s = TechnologyService(); items = s.list_categories()
    assert len(items) >= 10 and len({x["id"] for x in items}) == len(items)
    assert s.list_categories(items[0]["id"])
    assert s.get_category(items[0]["id"])["id"] == items[0]["id"]
def test_status(): assert TechnologyService().get_status()["status"] == "taxonomy_scaffold"
