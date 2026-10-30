from ..service import MediaService
def test_catalog_and_detail():
    service=MediaServiceService(); items=service.list_categories()
    assert len(items)>=10
    assert len({item["id"] for item in items})==len(items)
    assert service.get_category(items[0]["id"])["id"]==items[0]["id"]
def test_status():
    assert MediaServiceService().get_status()["status"]=="taxonomy_scaffold"
