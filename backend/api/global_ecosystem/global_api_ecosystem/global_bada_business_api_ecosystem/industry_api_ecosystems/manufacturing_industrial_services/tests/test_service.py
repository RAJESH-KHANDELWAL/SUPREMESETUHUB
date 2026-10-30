from .service import ManufacturingService
def test_catalog():
    s=ManufacturingService(); items=s.list_categories()
    assert len(items)>=10 and len({x["id"] for x in items})==len(items)
    assert s.get_category(items[0]["id"])["id"]==items[0]["id"]
def test_status(): assert ManufacturingService().get_status()["status"]=="taxonomy_scaffold"
