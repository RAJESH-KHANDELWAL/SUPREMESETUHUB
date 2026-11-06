from ..catalog import validate_catalog
from ..service import HomeServicesFacilityService

def test_catalog_integrity_and_detail():
 service=HomeServicesFacilityService(); items=service.list_categories()
 assert len(items)==18
 assert len({x["id"] for x in items})==len(items)
 assert validate_catalog()["valid"]
 assert service.get_category("commercial_facility_management")["id"]=="commercial_facility_management"

def test_search_and_channel_filters():
 service=HomeServicesFacilityService()
 assert any(x["id"]=="cleaning_and_housekeeping" for x in service.list_categories(query="housekeeping"))
 offline=service.list_categories(channel="offline")
 assert offline and all("offline" in x["channels"] for x in offline)

def test_cross_ecosystem_links():
 links=HomeServicesFacilityService().get_cross_ecosystem_links()
 assert "spa_and_massage_services" in links["healthcare_wellness_fitness"]["canonical_categories"]
 assert "gym_and_fitness_centres" in links["healthcare_wellness_fitness"]["canonical_categories"]

def test_unknown_category_and_status():
 service=HomeServicesFacilityService()
 assert service.get_category("unknown") is None
 assert service.get_status()["category_count"]==18
