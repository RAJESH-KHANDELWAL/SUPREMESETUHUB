"""Home services, property maintenance and facility management API ecosystem."""
INDUSTRY_ID = "home_services_property_maintenance_facility_management"
INDUSTRY_NAME = "Home Services, Property Maintenance & Facility Management API Ecosystem"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import HomeServicesFacilityService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "HomeServicesFacilityService"]
