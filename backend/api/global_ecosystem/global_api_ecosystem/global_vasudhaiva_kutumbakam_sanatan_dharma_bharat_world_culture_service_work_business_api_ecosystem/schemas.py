"""Validated API contracts for cultural service, work and business records."""
from __future__ import annotations
from pydantic import BaseModel,Field
class CultureServiceWorkBusinessRecordRequest(BaseModel):
    record_id:str=Field(min_length=3,max_length=160)
    capability_id:str=Field(min_length=2,max_length=100)
    record_type:str=Field(min_length=2,max_length=40)
    title:str=Field(min_length=1,max_length=300)
    description:str=Field(min_length=1,max_length=10000)
    organization_name:str|None=Field(default=None,max_length=250)
    location:str|None=Field(default=None,max_length=250)
    website_url:str|None=Field(default=None,max_length=2000)
    source_url:str|None=Field(default=None,max_length=2000)
    status:str=Field(default="DRAFT",max_length=30)
    metadata:dict=Field(default_factory=dict)
class CultureServiceWorkBusinessAIRequest(BaseModel):
    question:str=Field(min_length=1,max_length=500)
    domain:str|None=Field(default=None,max_length=20)
