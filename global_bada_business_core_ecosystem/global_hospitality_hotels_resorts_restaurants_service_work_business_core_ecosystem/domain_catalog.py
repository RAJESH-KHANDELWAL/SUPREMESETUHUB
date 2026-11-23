"""Canonical hospitality service, work and business taxonomy."""
from copy import deepcopy
DOMAINS = {
  "business_strategy": [
    "Business model design",
    "Feasibility studies",
    "Market research",
    "Business plans",
    "Operating model design",
    "Continuity planning",
    "Growth strategy"
  ],
  "setup_licensing": [
    "Business setup guidance",
    "Registration coordination",
    "Local licensing checklists",
    "Food business license coordination",
    "Fire safety approval checklists",
    "Tourism registration guidance",
    "Permit renewal tracking",
    "Professional referrals"
  ],
  "operations": [
    "Standard operating procedures",
    "Service quality systems",
    "Process mapping",
    "Capacity planning",
    "Cost optimization",
    "Performance dashboards",
    "Customer experience improvement"
  ],
  "revenue_sales": [
    "Revenue management advisory",
    "Pricing strategy",
    "Occupancy improvement",
    "Sales pipeline design",
    "Corporate sales",
    "Group sales",
    "Upselling",
    "Customer retention"
  ],
  "marketing_branding": [
    "Brand positioning",
    "Digital marketing",
    "Search visibility",
    "Local business profiles",
    "Content strategy",
    "Social media",
    "Reputation management",
    "Campaign analytics"
  ],
  "technology_distribution": [
    "Direct booking strategy",
    "OTA channel strategy",
    "Channel management advisory",
    "PMS selection",
    "POS selection",
    "CRM selection",
    "Booking engine selection",
    "Integration planning"
  ],
  "finance_commercial": [
    "Budgeting support",
    "Unit economics",
    "Cash flow planning",
    "Financial modelling",
    "Cost controls",
    "Tax professional coordination",
    "Insurance coordination",
    "Audit readiness"
  ],
  "procurement_supply": [
    "Supplier discovery",
    "Vendor due diligence coordination",
    "Food sourcing",
    "Linen and amenities sourcing",
    "Equipment procurement",
    "Contract administration support",
    "Inventory systems"
  ],
  "staffing_training": [
    "Recruitment support",
    "Staffing partner discovery",
    "Workforce planning",
    "Role design",
    "Hospitality training",
    "Leadership development",
    "Service standards",
    "Workplace wellbeing"
  ],
  "property_assets": [
    "Site selection support",
    "Property feasibility",
    "Lease comparison support",
    "Asset management planning",
    "Renovation planning",
    "Facilities management advisory"
  ],
  "franchise_investment": [
    "Franchise model design",
    "Franchisor readiness",
    "Franchisee support",
    "Investor readiness",
    "Partnership models",
    "Expansion planning",
    "Due diligence coordination"
  ],
  "tourism_destination": [
    "Destination research",
    "Tourism circuit development",
    "Local experience design",
    "Tour operator partnerships",
    "Destination marketing",
    "Community tourism"
  ],
  "digital_services": [
    "Website planning",
    "Booking funnel design",
    "CRM implementation planning",
    "Data analytics",
    "Automation discovery",
    "Cybersecurity assessment referrals"
  ],
  "india_global_market": [
    "India market mapping",
    "State and city opportunity mapping",
    "International market entry",
    "Localization",
    "Cross-border partnerships",
    "Regional expansion"
  ],
  "professional_advisory": [
    "Business consulting",
    "Management advisory",
    "Hospitality coaching",
    "Operations consulting",
    "Marketing advisory",
    "Technology advisory"
  ],
  "service_work": [
    "Hospitality service providers",
    "Independent consultants",
    "Freelance specialists",
    "Maintenance services",
    "Cleaning services",
    "Catering services",
    "Event service providers",
    "Training providers"
  ]
}
def list_domains():
    return [{"id": k, "capabilities": list(v)} for k, v in DOMAINS.items()]
def get_domain(domain_id):
    key = str(domain_id or "").strip().lower(); values = DOMAINS.get(key)
    return {"id": key, "capabilities": list(values)} if values is not None else None
def search_domains(query=""):
    term = str(query or "").strip().casefold()
    return [item for item in list_domains() if not term or term in item["id"].casefold() or any(term in x.casefold() for x in item["capabilities"])]
def catalog_snapshot():
    return {"domains": deepcopy(DOMAINS), "domain_count": len(DOMAINS), "capability_count": sum(len(v) for v in DOMAINS.values())}
