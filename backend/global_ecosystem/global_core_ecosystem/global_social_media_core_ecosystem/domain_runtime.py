"""Shared read-only runtime for Social Media Core domain packages."""
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS
from .product_catalog import list_social_media_platforms
class SocialMediaCoreDomainManager:
    DOMAIN_ID=""
    def __init__(self,domain_id:str|None=None)->None:
        if domain_id is not None:self.DOMAIN_ID=domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:raise ValueError(f"UNKNOWN_SOCIAL_MEDIA_DOMAIN: {self.DOMAIN_ID}")
        self.definition=DOMAIN_DEFINITIONS[self.DOMAIN_ID]
    def list_platforms(self)->dict[str,Any]:
        items=list_social_media_platforms(domain_id=self.DOMAIN_ID);return {"success":True,"domain_id":self.DOMAIN_ID,"count":len(items),"platforms":items}
    def status(self)->dict[str,Any]:
        items=self.list_platforms()["platforms"];return {"success":True,"domain_id":self.DOMAIN_ID,"name":self.definition["name"],"purpose":self.definition["purpose"],"status":"CORE_DOMAIN_AVAILABLE","platform_count":len(items),"live_connections_verified":False,"api_calls_performed":0}
    def get_platform(self,platform_id:str)->dict[str,Any]|None:
        key=platform_id.strip().casefold();return next((x for x in list_social_media_platforms(domain_id=self.DOMAIN_ID) if x["platform_id"].casefold()==key),None)
