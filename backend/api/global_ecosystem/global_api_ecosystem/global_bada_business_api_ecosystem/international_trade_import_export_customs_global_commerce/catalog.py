"""International trade, customs and cross-border commerce taxonomy."""

CATEGORIES = [
    {"id": "import_export_businesses", "name": "Import & Export Businesses", "channels": ["online", "offline", "hybrid"], "subcategories": ["exporters", "importers", "merchant_exporters", "manufacturer_exporters", "export_trading_companies", "import_distributors", "cross_border_smes"]},
    {"id": "international_trade_markets", "name": "International Trade & Global Markets", "channels": ["online", "offline", "hybrid"], "subcategories": ["bilateral_trade", "multilateral_trade", "regional_trade_blocs", "global_market_entry", "country_market_profiles", "trade_flows", "market_access_opportunities"]},
    {"id": "customs_clearance_brokers", "name": "Customs Clearance & Customs Brokers", "channels": ["offline", "hybrid"], "subcategories": ["customs_brokerage", "import_clearance", "export_clearance", "customs_document_review", "port_clearance_coordination", "customs_queries"]},
    {"id": "trade_documentation_certificates", "name": "Import-Export Documentation & Certificates", "channels": ["online", "offline", "hybrid"], "subcategories": ["commercial_invoice", "packing_list", "bill_of_lading_documentation", "certificate_of_origin", "inspection_certificates", "export_declarations", "import_declarations", "document_digitisation"]},
    {"id": "hs_codes_product_classification", "name": "HS Codes & Product Classification", "channels": ["online", "hybrid"], "subcategories": ["harmonized_system_codes", "national_tariff_lines", "product_classification_research", "classification_rulings", "hs_code_crosswalks", "classification_reviews"]},
    {"id": "customs_duties_tariffs_taxes", "name": "Customs Duties, Tariffs & Border Taxes", "channels": ["online", "hybrid"], "subcategories": ["customs_duty_information", "preferential_tariffs", "anti_dumping_duties", "countervailing_duties", "safeguard_measures", "landed_cost_components"]},
    {"id": "trade_compliance_regulatory", "name": "Trade Compliance & Regulatory Requirements", "channels": ["online", "offline", "hybrid"], "subcategories": ["import_export_licensing", "restricted_goods_controls", "export_controls", "sanctions_screening", "product_regulatory_requirements", "trade_compliance_advisory"]},
    {"id": "rules_of_origin_trade_remedies", "name": "Rules of Origin & Trade Remedies", "channels": ["online", "hybrid"], "subcategories": ["preferential_rules_of_origin", "non_preferential_origin", "origin_certification", "trade_remedy_cases", "anti_dumping_proceedings", "safeguard_investigations"]},
    {"id": "trade_agreements_market_access", "name": "Trade Agreements & Market Access", "channels": ["online", "hybrid"], "subcategories": ["free_trade_agreements", "comprehensive_economic_partnerships", "bilateral_trade_agreements", "tariff_concessions", "market_access_conditions", "agreement_utilisation"]},
    {"id": "export_promotion_trade_bodies", "name": "Export Promotion Councils & Trade Bodies", "channels": ["offline", "hybrid", "online"], "subcategories": ["export_promotion_councils", "chambers_of_commerce", "trade_associations", "industry_export_bodies", "trade_delegations", "exporter_membership_services"]},
    {"id": "export_incentives_government_schemes", "name": "Export Incentives & Government Schemes", "channels": ["online", "offline", "hybrid"], "subcategories": ["export_incentive_programmes", "duty_remission_schemes", "export_credit_support_referrals", "government_export_grants", "scheme_eligibility_information", "incentive_claim_support"]},
    {"id": "global_sourcing_procurement", "name": "Global Sourcing & International Procurement", "channels": ["online", "offline", "hybrid"], "subcategories": ["international_supplier_sourcing", "global_vendor_discovery", "sourcing_agents", "international_tender_sourcing", "supplier_due_diligence", "procurement_marketplaces"]},
    {"id": "international_buyer_seller_networks", "name": "International Buyer-Seller Networks", "channels": ["online", "offline", "hybrid"], "subcategories": ["buyer_discovery", "exporter_directories", "b2b_trade_matching", "trade_lead_generation", "buyer_seller_meetings", "verified_trade_enquiries"]},
    {"id": "trade_fairs_exhibitions_missions", "name": "International Trade Fairs, Exhibitions & Missions", "channels": ["offline", "hybrid"], "subcategories": ["international_trade_fairs", "buyer_seller_meets", "export_exhibitions", "trade_missions", "country_pavilions", "business_delegations"]},
    {"id": "cross_border_ecommerce", "name": "Cross-Border E-commerce & Digital Trade", "channels": ["online", "hybrid"], "subcategories": ["cross_border_marketplaces", "international_d2c", "digital_trade_services", "cross_border_seller_enablement", "international_order_compliance", "digital_services_exports"]},
    {"id": "trade_intelligence_statistics", "name": "Trade Intelligence, Statistics & Research", "channels": ["online", "hybrid"], "subcategories": ["import_export_statistics", "commodity_trade_data", "country_trade_profiles", "competitor_trade_research", "trade_forecasting", "market_intelligence_reports"]},
    {"id": "trade_facilitation_single_window", "name": "Trade Facilitation & Single-Window Systems", "channels": ["online", "hybrid"], "subcategories": ["national_single_windows", "customs_e_filing", "trade_document_exchange", "border_agency_coordination", "trade_process_automation", "paperless_trade"]},
    {"id": "trade_quality_inspection_standards", "name": "Trade Quality, Inspection & Standards", "channels": ["offline", "hybrid"], "subcategories": ["pre_shipment_inspection", "commodity_testing_referrals", "product_conformity_assessment", "quality_certification", "export_packaging_standards", "technical_barriers_to_trade"]},
    {"id": "trade_consulting_capacity_building", "name": "Export Consulting & Trade Capacity Building", "channels": ["online", "offline", "hybrid"], "subcategories": ["export_readiness_assessment", "export_business_planning", "international_market_entry_advisory", "export_documentation_training", "trade_compliance_training", "exporter_capacity_building"]},
]


def list_categories():
    """Return defensive copies of the category catalog."""
    return [dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"])) for item in CATEGORIES]


def get_category(category_id: str):
    """Return a category by stable identifier, or None."""
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"]))
    return None


def validate_catalog():
    ids = [item["id"] for item in CATEGORIES]
    duplicates = sorted({item_id for item_id in ids if ids.count(item_id) > 1})
    return {"valid": not duplicates, "category_count": len(CATEGORIES), "duplicate_ids": duplicates}
