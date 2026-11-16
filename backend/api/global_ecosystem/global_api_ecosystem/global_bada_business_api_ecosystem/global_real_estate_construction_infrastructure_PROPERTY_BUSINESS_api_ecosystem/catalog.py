"""Real Estate & Construction category taxonomy."""
from __future__ import annotations
CATEGORIES = [
  {
    "id": "residential_property",
    "name": "Residential Property",
    "subcategories": [
      "apartments",
      "independent_houses",
      "plots",
      "gated_communities"
    ]
  },
  {
    "id": "commercial_property",
    "name": "Commercial Property",
    "subcategories": [
      "offices",
      "retail_spaces",
      "warehouses",
      "industrial_property"
    ]
  },
  {
    "id": "property_brokerage",
    "name": "Property Sales & Brokerage",
    "subcategories": [
      "residential_brokers",
      "commercial_brokers",
      "channel_partners",
      "transaction_advisory"
    ]
  },
  {
    "id": "rental_management",
    "name": "Rental & Property Management",
    "subcategories": [
      "residential_rentals",
      "commercial_leasing",
      "tenant_management",
      "facility_management"
    ]
  },
  {
    "id": "real_estate_development",
    "name": "Real Estate Development",
    "subcategories": [
      "residential_developers",
      "commercial_developers",
      "townships",
      "mixed_use_projects"
    ]
  },
  {
    "id": "construction_civil_works",
    "name": "Construction & Civil Works",
    "subcategories": [
      "general_contractors",
      "civil_engineering",
      "infrastructure",
      "renovation"
    ]
  },
  {
    "id": "architecture_design",
    "name": "Architecture & Design",
    "subcategories": [
      "architects",
      "interior_design",
      "landscape_design",
      "space_planning"
    ]
  },
  {
    "id": "building_materials",
    "name": "Building Materials & Products",
    "subcategories": [
      "cement",
      "steel",
      "tiles",
      "doors_windows"
    ]
  },
  {
    "id": "engineering_project_management",
    "name": "Engineering & Project Management",
    "subcategories": [
      "structural_engineering",
      "mep_services",
      "project_management",
      "quantity_surveying"
    ]
  },
  {
    "id": "property_legal_valuation",
    "name": "Property Legal, Valuation & Inspection",
    "subcategories": [
      "title_due_diligence",
      "registration_support",
      "property_valuation",
      "building_inspection"
    ]
  },
  {
    "id": "home_finance",
    "name": "Mortgage & Home Finance",
    "subcategories": [
      "home_loans",
      "loan_against_property",
      "mortgage_broking",
      "construction_finance"
    ]
  },
  {
    "id": "proptech_smart_buildings",
    "name": "PropTech & Smart Buildings",
    "subcategories": [
      "property_listing_technology",
      "building_automation",
      "real_estate_analytics",
      "digital_management"
    ]
  }
]
def list_categories():
    return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
