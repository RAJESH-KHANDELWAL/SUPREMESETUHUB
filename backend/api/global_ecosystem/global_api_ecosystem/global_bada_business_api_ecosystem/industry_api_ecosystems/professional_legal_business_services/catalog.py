"""Category catalog for Professional, Legal & Business Services."""
from __future__ import annotations

CATEGORIES = (
    {"id": "legal_services", "name": "Legal Services", "subcategories": ["civil_law","criminal_law","corporate_law","commercial_law","litigation"]},
    {"id": "accounting_taxation", "name": "Accounting & Taxation", "subcategories": ["bookkeeping","audit","tax_filing","gst_compliance","payroll"]},
    {"id": "business_consulting", "name": "Business Consulting", "subcategories": ["strategy_consulting","operations_consulting","management_consulting","growth_advisory"]},
    {"id": "company_secretarial", "name": "Company Secretarial & Compliance", "subcategories": ["company_incorporation","roc_filings","corporate_governance","regulatory_compliance"]},
    {"id": "human_resources", "name": "Human Resources Services", "subcategories": ["recruitment","hr_advisory","staffing","payroll_services"]},
    {"id": "marketing_agencies", "name": "Marketing & Advertising Agencies", "subcategories": ["digital_marketing","branding","public_relations","market_research"]},
    {"id": "design_architecture", "name": "Design & Architecture", "subcategories": ["architecture","interior_design","graphic_design","industrial_design"]},
    {"id": "engineering_consultancy", "name": "Engineering Consultancy", "subcategories": ["civil_engineering","mechanical_engineering","electrical_engineering","project_management"]},
    {"id": "it_professional_services", "name": "IT Professional Services", "subcategories": ["software_consulting","managed_it","cybersecurity_services","cloud_consulting"]},
    {"id": "translation_localization", "name": "Translation & Localization", "subcategories": ["translation","interpretation","localization","transcription"]},
    {"id": "procurement_advisory", "name": "Procurement & Sourcing", "subcategories": ["vendor_management","sourcing","tender_support","supply_advisory"]},
    {"id": "testing_certification", "name": "Testing & Certification Services", "subcategories": ["product_testing","quality_inspection","management_systems","technical_certification"]},
)

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None
