"""Source-aware directory for the 26 company-specific adapter packages.

Names and official-site URLs are discovery metadata only. No legal identity,
jurisdiction, ownership, filings, or live provider connection is asserted.
"""
from fastapi import APIRouter, HTTPException, Query

COMPANIES = {
    "adobe": ("Adobe", "https://www.adobe.com/"),
    "alibaba": ("Alibaba", "https://www.alibaba.com/"),
    "amazon": ("Amazon", "https://www.amazon.com/"),
    "apple": ("Apple", "https://www.apple.com/"),
    "atlassian": ("Atlassian", "https://www.atlassian.com/"),
    "aws": ("Amazon Web Services", "https://aws.amazon.com/"),
    "bytedance": ("ByteDance", "https://www.bytedance.com/"),
    "cisco": ("Cisco", "https://www.cisco.com/"),
    "cloudflare": ("Cloudflare", "https://www.cloudflare.com/"),
    "github": ("GitHub", "https://github.com/"),
    "google": ("Google", "https://about.google/"),
    "ibm": ("IBM", "https://www.ibm.com/"),
    "intel": ("Intel", "https://www.intel.com/"),
    "meta": ("Meta", "https://about.meta.com/"),
    "microsoft": ("Microsoft", "https://www.microsoft.com/"),
    "netflix": ("Netflix", "https://about.netflix.com/"),
    "nvidia": ("NVIDIA", "https://www.nvidia.com/"),
    "openai": ("OpenAI", "https://openai.com/"),
    "oracle": ("Oracle", "https://www.oracle.com/"),
    "paypal": ("PayPal", "https://www.paypal.com/"),
    "salesforce": ("Salesforce", "https://www.salesforce.com/"),
    "samsung": ("Samsung", "https://www.samsung.com/"),
    "shopify": ("Shopify", "https://www.shopify.com/"),
    "stripe": ("Stripe", "https://stripe.com/"),
    "tencent": ("Tencent", "https://www.tencent.com/"),
    "zoom": ("Zoom", "https://www.zoom.com/"),
}

def _profile(company_id: str) -> dict:
    item = COMPANIES.get(company_id)
    if item is None:
        raise KeyError(company_id)
    name, url = item
    return {
        "company_id": company_id,
        "display_name": name,
        "record_type": "company",
        "profile_status": "source_registered_unverified",
        "data_status": "no_verified_profile_record",
        "sources": [{
            "source_id": f"{company_id}_official_website",
            "source_type": "official_website",
            "url": url,
            "authority": "company_published_source",
            "live_connection": False,
        }],
        "limitations": [
            "This is a company-brand discovery entry, not a verified legal-entity record.",
            "No live registry, filings, ownership, or provider integration is connected.",
            "The official website is a discovery source and does not establish jurisdiction or legal status.",
        ],
    }

router = APIRouter(prefix="/global/company-directory/company-profiles", tags=["Company Profile Directory"])

@router.get("")
def list_company_profiles(q: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=100), offset: int = Query(default=0, ge=0)):
    entries = [_profile(company_id) for company_id in COMPANIES]
    if q:
        term = q.casefold()
        entries = [entry for entry in entries if term in entry["company_id"] or term in entry["display_name"].casefold()]
    return {"success": True, "count": len(entries), "total": len(entries), "limit": limit, "offset": offset, "items": entries[offset:offset + limit]}

@router.get("/{company_id}")
def get_company_profile(company_id: str):
    try:
        return {"success": True, **_profile(company_id.casefold())}
    except KeyError as exc:
        raise HTTPException(status_code=404, detail={"error": "COMPANY_PROFILE_NOT_FOUND", "company_id": company_id}) from exc
