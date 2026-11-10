"""Aggregate discovery service across canonical work/business catalogues."""
from __future__ import annotations
from ..global_universal_work_business_taxonomy_api_ecosystem.service import UniversalWorkBusinessTaxonomyService
from ..global_freelancer_gig_independent_work_business_api_ecosystem import list_subcategories as list_freelance_specializations
from ..global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.service import DomainService as JobsCareersService
from .catalog import list_sources

class GlobalWorkBusinessAPIService:
    ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-WORK-BUSINESS-API"
    VERSION = "1.0.0"

    def __init__(self):
        self.taxonomy = UniversalWorkBusinessTaxonomyService()
        self.jobs = JobsCareersService()

    def status(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID,
                "ecosystem_name": "GLOBAL WORK & BUSINESS API ECOSYSTEM",
                "version": self.VERSION, "status": "AGGREGATE_FACADE_READY",
                "canonical_sources": list_sources(),
                "universal_taxonomy": self.taxonomy.get_status(),
                "freelance_specialization_count": len(list_freelance_specializations()),
                "jobs_careers": self.jobs.get_status(),
                "live_jobs_or_gigs": False}

    def list_sectors(self, include_adult=False):
        return self.taxonomy.list_sectors(include_adult)

    def search_sectors(self, query, include_adult=False):
        return self.taxonomy.search(query, include_adult)

    def get_sector(self, sector_id, include_adult=False):
        return self.taxonomy.get_sector(sector_id, include_adult)

    def facets(self):
        return self.taxonomy.get_facets()

    def freelance_specializations(self):
        items = list_freelance_specializations()
        return {"count": len(items), "specializations": items, "classification": "taxonomy_only"}

    def jobs_careers_status(self):
        return self.jobs.get_status()
