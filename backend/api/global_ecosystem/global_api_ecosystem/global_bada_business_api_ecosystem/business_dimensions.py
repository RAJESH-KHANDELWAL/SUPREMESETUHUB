"""Cross-cutting dimensions for classifying businesses without duplicating sector taxonomy.

These controlled vocabularies describe how an organisation operates. They are
not registrations, legal opinions, provider verifications, or live integrations.
"""

BUSINESS_DIMENSIONS = (
    {
        "id": "entity_types",
        "name": "Business and organisation types",
        "values": [
            "sole_proprietorship", "individual_business", "self_employed",
            "home_based_business", "family_business", "partnership",
            "limited_liability_partnership", "private_limited_company",
            "public_limited_company", "one_person_company", "cooperative",
            "producer_company", "nonprofit", "charity", "social_enterprise",
            "startup", "scaleup", "franchisee", "franchisor", "joint_venture",
            "public_sector_enterprise", "multinational_corporation",
            "holding_company", "conglomerate", "marketplace_operator",
            "platform_operator", "independent_professional", "creator_business",
        ],
    },
    {
        "id": "business_sizes",
        "name": "Business size and scale",
        "values": [
            "pre_revenue", "individual", "home_based", "micro", "small",
            "medium", "large", "enterprise", "multinational", "conglomerate",
        ],
        "note": "Size thresholds are jurisdiction-specific; use local legal definitions where applicable.",
    },
    {
        "id": "operating_models",
        "name": "Operating and delivery models",
        "values": [
            "offline", "online", "hybrid", "mobile_or_field_based",
            "remote_first", "physical_store", "branch_network", "marketplace",
            "direct_to_consumer", "business_to_business", "business_to_consumer",
            "business_to_government", "peer_to_peer", "subscription",
            "on_demand", "platform_enabled", "franchise_network",
        ],
    },
    {
        "id": "ownership_models",
        "name": "Ownership and control models",
        "values": [
            "founder_owned", "family_owned", "employee_owned", "partner_owned",
            "member_owned", "cooperative_owned", "investor_backed",
            "venture_capital_backed", "private_equity_backed", "publicly_listed",
            "state_owned", "nonprofit_governed", "community_owned",
        ],
    },
    {
        "id": "business_lifecycle",
        "name": "Business lifecycle and maturity",
        "values": [
            "idea", "validation", "pre_launch", "launch", "early_stage",
            "growth", "scaling", "mature", "restructuring", "acquisition",
            "merger", "succession", "closure",
        ],
    },
    {
        "id": "commerce_models",
        "name": "Revenue and commerce models",
        "values": [
            "one_time_sales", "recurring_subscription", "usage_based",
            "commission", "marketplace_fees", "advertising_supported",
            "licensing", "royalties", "franchise_fees", "rental_or_leasing",
            "freemium", "donations_or_grants", "service_contract",
            "project_based", "transaction_fees", "hybrid_revenue",
        ],
    },
    {
        "id": "customer_segments",
        "name": "Customer and market segments",
        "values": [
            "b2b", "b2c", "b2g", "b2b2c", "d2c", "c2c", "c2b",
            "individual_consumers", "families", "small_businesses",
            "msmes", "startups", "enterprises", "government",
            "nonprofits", "institutions", "global_customers",
        ],
    },
    {
        "id": "market_scope",
        "name": "Geographic and trade scope",
        "values": [
            "neighbourhood", "local", "city", "district", "state_or_province",
            "national", "cross_border", "regional", "international", "global",
            "export", "import", "domestic_trade", "free_trade_zone",
        ],
    },
    {
        "id": "business_capabilities",
        "name": "Business capabilities and operational functions",
        "values": [
            "strategy_and_planning", "company_formation", "licensing_and_permits",
            "finance_and_accounting", "banking_and_payments", "sales_and_crm",
            "marketing_and_advertising", "customer_support", "human_resources",
            "recruitment_and_payroll", "procurement", "inventory_and_warehouse",
            "manufacturing_and_quality", "supply_chain_and_logistics",
            "ecommerce_and_order_management", "contracts_and_legal",
            "tax_and_compliance", "risk_and_insurance", "data_and_analytics",
            "technology_and_cybersecurity", "research_and_development",
            "intellectual_property", "partnerships_and_networking",
            "funding_and_investment", "franchising_and_licensing",
            "sustainability_and_esg", "business_continuity",
            "mergers_and_acquisitions", "export_and_import_operations",
        ],
    },
    {
        "id": "verification_states",
        "name": "Business record and verification states",
        "values": [
            "unverified", "contact_details_verified", "identity_checked",
            "registration_claimed", "registration_verified",
            "license_verified", "address_verified", "ownership_verified",
            "provider_documentation_reviewed", "integration_tested",
            "suspended", "under_review",
        ],
        "note": "A catalog entry is not proof of registration, licence, identity, or trustworthiness.",
    },
)

def list_business_dimensions():
    """Return all supported cross-cutting business classification dimensions."""
    return {"count": len(BUSINESS_DIMENSIONS), "dimensions": list(BUSINESS_DIMENSIONS)}


def get_business_dimension(dimension_id: str):
    """Return one dimension by stable ID, or None when it is unknown."""
    return next((item for item in BUSINESS_DIMENSIONS if item["id"] == dimension_id), None)
