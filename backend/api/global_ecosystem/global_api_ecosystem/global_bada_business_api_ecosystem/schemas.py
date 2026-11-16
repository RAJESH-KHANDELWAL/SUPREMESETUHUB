from pydantic import BaseModel


class BusinessEcosystemStatus(BaseModel):
    success: bool
    ecosystem_id: str
    ecosystem_name: str
    version: str
    status: str
    module_count: int
    category_count: int
    adult_category_count: int
    global_world_domain_count: int
    domain_package_count: int
    domain_subcategory_count: int
    domain_registry_status: str
    timestamp: str
