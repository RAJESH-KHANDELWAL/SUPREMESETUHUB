"""FastAPI routes for Industry API Ecosystems."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import IndustryEcosystemDetailResponse, IndustryEcosystemListResponse
from .service import IndustryEcosystemService

router = APIRouter(prefix="/industries", tags=["GLOBAL BADA BUSINESS - INDUSTRY API ECOSYSTEMS"])
service = IndustryEcosystemService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("", response_model=IndustryEcosystemListResponse)
def list_industries(
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
    coverage: str | None = Query(default=None, pattern="^(india|global)$"),
    q: str | None = Query(default=None, min_length=1, max_length=100),
    include_adult: bool = Query(default=False, description="Show separately classified 18+ taxonomy; this flag is not age verification."),
):
    items = service.list_industries(channel=channel, coverage=coverage, query=q, include_adult=include_adult)
    return {"success": True, "count": len(items), "industries": items}

@router.get("/{industry_id}", response_model=IndustryEcosystemDetailResponse)
def get_industry(
    industry_id: str,
    include_adult: bool = Query(default=False, description="Show separately classified 18+ taxonomy; this flag is not age verification."),
):
    item = service.get_industry(industry_id, include_adult=include_adult)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "INDUSTRY_ECOSYSTEM_NOT_FOUND", "industry_id": industry_id})
    return {"success": True, "industry": item}


# Domain-specific industry APIs
from .agriculture_food_natural_resources.routes import router as agriculture_food_router
from .education_learning_training.routes import router as education_learning_router
from .jobs_careers_employment.routes import router as jobs_careers_router
from .healthcare_life_sciences.routes import router as healthcare_router
from .finance_banking_insurance.routes import router as finance_banking_router
from .real_estate_construction.routes import router as real_estate_router
from .retail_ecommerce_consumer_goods.routes import router as retail_ecommerce_router

router.include_router(agriculture_food_router)
router.include_router(education_learning_router)
router.include_router(jobs_careers_router)
router.include_router(healthcare_router)
router.include_router(finance_banking_router)
router.include_router(real_estate_router)
router.include_router(retail_ecommerce_router)

from .technology_it_telecommunications.routes import router as technology_telecom_router
from .manufacturing_industrial_services.routes import router as manufacturing_router
from .transport_logistics_supply_chain.routes import router as transport_logistics_router
from .travel_tourism_hospitality.routes import router as travel_hospitality_router
from .media_entertainment_creative_industries.routes import router as media_creative_router

router.include_router(technology_telecom_router)
router.include_router(manufacturing_router)
router.include_router(transport_logistics_router)
router.include_router(travel_hospitality_router)
router.include_router(media_creative_router)

from .energy_utilities_environment.routes import router as energy_environment_router
from .professional_legal_business_services.routes import router as professional_services_router
from .government_public_services_social_impact.routes import router as public_impact_router
from .automotive_mobility.routes import router as automotive_mobility_router
from .personal_lifestyle_wellness.routes import router as personal_wellness_router

router.include_router(energy_environment_router)
router.include_router(professional_services_router)
router.include_router(public_impact_router)
router.include_router(automotive_mobility_router)
router.include_router(personal_wellness_router)

from .sports_recreation_community.routes import router as sports_community_router
router.include_router(sports_community_router)

from .food_hospitality_restaurants.routes import router as food_hospitality_router
from .security_defence_safety_services.routes import router as security_defence_router
from .science_research_innovation.routes import router as science_research_router
from .mining_metals_minerals.routes import router as mining_metals_router
router.include_router(food_hospitality_router)
router.include_router(security_defence_router)
router.include_router(science_research_router)
router.include_router(mining_metals_router)

from .digital_infrastructure_telecommunications.routes import router as digital_infrastructure_router
from .aviation_aerospace_space_technology.routes import router as aviation_aerospace_router
from .water_resources_marine_industries.routes import router as water_marine_router
from .fashion_textiles_apparel.routes import router as fashion_textiles_router
from .supply_chain_warehousing_distribution.routes import router as supply_chain_distribution_router
router.include_router(digital_infrastructure_router)
router.include_router(aviation_aerospace_router)
router.include_router(water_marine_router)
router.include_router(fashion_textiles_router)
router.include_router(supply_chain_distribution_router)
