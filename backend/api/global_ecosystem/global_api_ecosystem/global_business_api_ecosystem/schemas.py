from pydantic import BaseModel


class BusinessEcosystemStatus(BaseModel):
    success: bool
    ecosystem_id: str
    ecosystem_name: str
    version: str
    status: str
    module_count: int
    timestamp: str
