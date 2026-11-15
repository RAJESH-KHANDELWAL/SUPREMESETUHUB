"""Registry of company-specific packages already present in this ecosystem.

The registry intentionally records package presence only. It does not assert that
company profile data is complete, verified, or connected to the shared JSON registry.
"""
from .models import CompanyModule

_COMPANY_MODULES = (
    ("adobe", "Adobe"),
    ("alibaba", "Alibaba"),
    ("amazon", "Amazon"),
    ("apple", "Apple"),
    ("atlassian", "Atlassian"),
    ("aws", "AWS"),
    ("bytedance", "ByteDance"),
    ("cisco", "Cisco"),
    ("cloudflare", "Cloudflare"),
    ("github", "GitHub"),
    ("google", "Google"),
    ("ibm", "IBM"),
    ("intel", "Intel"),
    ("meta", "Meta"),
    ("microsoft", "Microsoft"),
    ("netflix", "Netflix"),
    ("nvidia", "NVIDIA"),
    ("openai", "OpenAI"),
    ("oracle", "Oracle"),
    ("paypal", "PayPal"),
    ("salesforce", "Salesforce"),
    ("samsung", "Samsung"),
    ("shopify", "Shopify"),
    ("stripe", "Stripe"),
    ("tencent", "Tencent"),
    ("zoom", "Zoom"),
)

COMPANY_MODULES = tuple(
    CompanyModule(
        company_id=company_id,
        name=name,
        package_path=f"global_companies_ecosystem/{company_id}",
    )
    for company_id, name in _COMPANY_MODULES
)


def list_company_modules() -> list[CompanyModule]:
    return list(COMPANY_MODULES)


def get_company_module(company_id: str) -> CompanyModule | None:
    key = (company_id or "").strip().casefold()
    return next((item for item in COMPANY_MODULES if item.company_id == key), None)


def search_company_modules(query: str) -> list[CompanyModule]:
    needle = (query or "").strip().casefold()
    if not needle:
        return []
    return [
        item for item in COMPANY_MODULES
        if needle in item.company_id.casefold() or needle in item.name.casefold()
    ]


def validate_company_module_registry() -> dict[str, object]:
    ids = [item.company_id for item in COMPANY_MODULES]
    paths = [item.package_path for item in COMPANY_MODULES]
    return {
        "structurally_valid": (
            bool(ids)
            and len(ids) == len(set(ids))
            and len(paths) == len(set(paths))
            and all(item.name.strip() and item.package_path.startswith("global_companies_ecosystem/")
                    for item in COMPANY_MODULES)
        ),
        "module_count": len(COMPANY_MODULES),
        "duplicate_company_ids": sorted({value for value in ids if ids.count(value) > 1}),
        "duplicate_package_paths": sorted({value for value in paths if paths.count(value) > 1}),
        "registry_status": "module_index_only",
    }
