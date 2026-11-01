"""Mounted company-specific profile adapters."""
from importlib import import_module
from fastapi import APIRouter

COMPANY_ADAPTER_IDS = (
    "adobe", "alibaba", "amazon", "apple", "atlassian", "aws",
    "bytedance", "cisco", "cloudflare", "github", "google", "ibm",
    "intel", "meta", "microsoft", "netflix", "nvidia", "openai",
    "oracle", "paypal", "salesforce", "samsung", "shopify", "stripe",
    "tencent", "zoom",
)

router = APIRouter(tags=["GLOBAL COMPANY PROFILE ADAPTERS"])
for company_id in COMPANY_ADAPTER_IDS:
    module = import_module(f".{company_id}.routes", package=__package__)
    router.include_router(module.router)
