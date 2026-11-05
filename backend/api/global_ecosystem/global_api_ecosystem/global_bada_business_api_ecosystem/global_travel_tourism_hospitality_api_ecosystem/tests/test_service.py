from global_travel_tourism_hospitality_api_ecosystem.service import TravelService
def test_catalog_and_detail():
    service=TravelService(); items=service.list_categories()
    assert len(items)>=10
    assert len({item["id"] for item in items})==len(items)
    assert service.get_category(items[0]["id"])["id"]==items[0]["id"]
def test_status():
    assert TravelService().get_status()["status"]=="taxonomy_scaffold"
