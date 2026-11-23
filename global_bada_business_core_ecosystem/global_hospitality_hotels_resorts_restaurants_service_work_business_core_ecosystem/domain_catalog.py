"""Hospitality service-work business capability taxonomy."""
DOMAINS = {
  "business_strategy": [
    "Business model design",
    "Feasibility studies",
    "Market research",
    "Business planning",
    "Business setup coordination",
    "Operating model",
    "Business continuity"
  ],
  "operations": [
    "Standard operating procedures",
    "Service quality systems",
    "Process improvement",
    "Capacity planning",
    "Cost controls",
    "Performance management"
  ],
  "revenue_marketing": [
    "Revenue management",
    "Pricing strategy",
    "Brand positioning",
    "Digital marketing",
    "Sales enablement",
    "Customer retention",
    "Reputation management"
  ],
  "distribution_technology": [
    "Direct booking strategy",
    "Online travel agency channel strategy",
    "Channel management",
    "Property management systems",
    "Point of sale systems",
    "CRM",
    "Analytics"
  ],
  "procurement_supply": [
    "Supplier discovery",
    "Vendor qualification",
    "Food and beverage sourcing",
    "Linen and amenities",
    "Equipment procurement",
    "Contract management",
    "Inventory systems"
  ],
  "staffing_training": [
    "Recruitment support",
    "Staffing partners",
    "Hospitality training",
    "Leadership development",
    "Workforce planning",
    "Service standards"
  ],
  "finance_compliance": [
    "Budgeting",
    "Unit economics",
    "Cash flow planning",
    "Tax coordination",
    "Licensing checklist",
    "Insurance coordination",
    "Audit readiness"
  ],
  "property_assets": [
    "Site selection",
    "Property feasibility",
    "Asset management",
    "Renovation planning",
    "Facilities management",
    "Lease review"
  ],
  "franchise_investment": [
    "Franchise models",
    "Franchisor readiness",
    "Franchisee support",
    "Investor readiness",
    "Partnership models",
    "Expansion planning"
  ],
  "india_global_market": [
    "India market mapping",
    "State and city market mapping",
    "Tourism circuits",
    "International market entry",
    "Localization",
    "Cross-border partnerships"
  ]
}
def list_domains():
    return [{"id": key, "capabilities": list(values)} for key, values in DOMAINS.items()]
def get_domain(domain_id):
    values = DOMAINS.get(str(domain_id or "").strip().lower())
    return {"id": str(domain_id).strip().lower(), "capabilities": list(values)} if values is not None else None
