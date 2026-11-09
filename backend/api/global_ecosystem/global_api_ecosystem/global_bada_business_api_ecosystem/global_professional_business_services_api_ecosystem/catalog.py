"""Category catalog for Professional Services API Ecosystem."""
from __future__ import annotations

CATEGORIES = (
    {"id": "accounting_bookkeeping", "name": "Accounting & Bookkeeping Services", "subcategories": ["bookkeeping", "financial_record_keeping", "accounts_payable_receivable", "management_accounts"]},
    {"id": "taxation_advisory", "name": "Taxation & Tax Advisory Services", "subcategories": ["income_tax_return_preparation", "gst_return_support", "tax_planning_information", "tax_compliance_support"]},
    {"id": "audit_assurance", "name": "Audit & Assurance Services", "subcategories": ["internal_audit", "statutory_audit_by_qualified_firms", "financial_audit", "process_audit", "assurance_services"]},
    {"id": "business_management_consulting", "name": "Business & Management Consulting", "subcategories": ["business_strategy", "management_consulting", "business_process_improvement", "growth_advisory", "organizational_development"]},
    {"id": "human_resources_talent", "name": "Human Resources & Talent Services", "subcategories": ["recruitment", "staffing", "talent_acquisition", "hr_operations", "people_advisory"]},
    {"id": "architecture_interior_design", "name": "Architecture & Interior Design Consultancy", "subcategories": ["architectural_design", "interior_space_planning", "building_design_consultancy", "design_documentation"]},
    {"id": "engineering_project_consultancy", "name": "Engineering & Project Consultancy", "subcategories": ["civil_engineering_consultancy", "mechanical_engineering_consultancy", "electrical_engineering_consultancy", "project_management_consultancy", "technical_feasibility"]},
    {"id": "translation_interpretation", "name": "Translation, Interpretation & Localization", "subcategories": ["document_translation", "business_interpretation", "website_localization", "multilingual_content_adaptation"]},
    {"id": "business_process_outsourcing", "name": "Business Process Outsourcing (BPO)", "subcategories": ["back_office_operations", "data_processing", "document_processing", "customer_operations_support"]},
    {"id": "virtual_admin_support", "name": "Virtual Assistance & Administrative Support", "subcategories": ["virtual_assistance", "administrative_support", "calendar_and_inbox_support", "business_document_preparation"]},
    {"id": "professional_writing_documentation", "name": "Professional Writing & Documentation", "subcategories": ["technical_writing", "business_writing", "editing_and_proofreading", "policy_and_process_documentation"]},
    {"id": "research_business_analytics", "name": "Research & Business Analytics Services", "subcategories": ["business_research", "market_intelligence", "data_analysis", "industry_research", "reporting_and_insights"]},
)

def list_categories():
    return [dict(item, subcategories=list(item["subcategories"])) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
