"""Jurisdiction-aware business compliance discovery taxonomy.

Entries are screening topics, not legal conclusions. Applicability must be
confirmed against current official authorities and the actual business facts.
"""

INDIA_REQUIREMENTS = (
    {"id":"business_identity_and_entity","name":"Business identity and entity formation","area":"entity","applies_to":["all business forms; exact filings depend on entity type"],"examples":["PAN","entity incorporation or constitution records","authorised signatory details"],"trigger_factors":["entity_type","ownership_structure","business_activity"],"authority_level":"central_and_state_as_applicable","verification":"confirm current process with the relevant official registry or tax authority"},
    {"id":"tax_registration_and_returns","name":"Tax registration and reporting","area":"tax","applies_to":["businesses meeting applicable statutory conditions"],"examples":["GST registration where legally required or voluntarily chosen","income-tax registrations, returns and records as applicable"],"trigger_factors":["turnover","supply_type","state","inter_state_activity","business_model"],"authority_level":"central_and_state_as_applicable","verification":"check current GST and Income Tax Department rules for the transaction and entity"},
    {"id":"msme_registration_and_benefits","name":"MSME / Udyam registration","area":"msme","applies_to":["eligible micro, small and medium enterprises; optional unless a specific benefit or scheme requires it"],"examples":["Udyam registration"],"trigger_factors":["enterprise_classification","investment","turnover","scheme_or_contract"],"authority_level":"central","verification":"confirm current classification thresholds and official Udyam portal requirements"},
    {"id":"local_trade_and_establishment","name":"Local trade and establishment permissions","area":"local_business","applies_to":["premises- and activity-dependent businesses"],"examples":["Shops and Establishments registration where applicable","municipal trade licence or local permission where applicable"],"trigger_factors":["state","municipality","premises_use","employee_count","activity"],"authority_level":"state_and_local","verification":"check the relevant state labour department and municipal authority"},
    {"id":"premises_building_fire_and_storage","name":"Premises, building, fire and storage safety","area":"premises_safety","applies_to":["businesses whose premises, occupancy, storage or risk profile trigger approvals"],"examples":["building-use or occupancy permissions","fire safety approval or NOC where required","warehouse and hazardous-storage permissions where required"],"trigger_factors":["building_type","area","occupancy","stock_type","hazard_class","local_rules"],"authority_level":"state_and_local","verification":"obtain written applicability guidance from competent local and fire authorities"},
    {"id":"food_business_licensing","name":"Food business licensing","area":"product_sector","applies_to":["food businesses and specified food-chain activities"],"examples":["FSSAI registration or licence according to the applicable category"],"trigger_factors":["food_activity","scale","premises","distribution_role","turnover"],"authority_level":"central_and_state","verification":"check current FSSAI eligibility, category and licensing conditions"},
    {"id":"product_standards_and_labelling","name":"Product standards, testing and labelling","area":"product_sector","applies_to":["products and operators covered by notified standards or product-specific rules"],"examples":["BIS certification where compulsory or otherwise applicable","Legal Metrology packaged-commodity declarations where applicable","product testing and prescribed labels"],"trigger_factors":["product_category","manufacture_or_import","packaging","claims","sales_channel"],"authority_level":"central_and_state","verification":"identify the exact product rule, notified standard and responsible regulator before sale"},
    {"id":"regulated_goods_and_sector_licences","name":"Regulated goods and sector-specific licences","area":"sector_licence","applies_to":["regulated products, services and activities only"],"examples":["drug and cosmetics permissions where applicable","agriculture, chemicals, electronics or other sector-specific approvals as applicable"],"trigger_factors":["product_or_service","manufacturing_role","storage","sale","distribution","import"],"authority_level":"central_and_state","verification":"map the exact activity to the relevant sector regulator and current licence conditions"},
    {"id":"import_export_and_customs","name":"Import, export and customs","area":"cross_border_trade","applies_to":["businesses undertaking import/export or regulated cross-border trade"],"examples":["Importer Exporter Code (IEC) where required","customs declarations and tariff classification","product-specific import/export permissions"],"trigger_factors":["cross_border_trade","goods","origin_destination","restricted_or_prohibited_status"],"authority_level":"central","verification":"check DGFT, Indian Customs, current ITC(HS) policy and product regulator requirements"},
    {"id":"labour_and_employment","name":"Labour and employment compliance","area":"employment","applies_to":["employers and establishments meeting applicable legal conditions"],"examples":["applicable employment registrations and records","wage, workplace and social-security obligations"],"trigger_factors":["employee_count","worker_type","state","establishment_type","contracting_model"],"authority_level":"central_and_state","verification":"confirm current commencement, thresholds and state-specific rules with official labour authorities"},
    {"id":"environment_and_waste","name":"Environment, pollution and waste management","area":"environment","applies_to":["activities, premises, products or waste streams covered by environmental rules"],"examples":["Consent to Establish / Operate where required","waste-specific authorisations and producer obligations where applicable"],"trigger_factors":["process","emissions","effluent","waste_type","product_category","location"],"authority_level":"central_and_state","verification":"consult the relevant State Pollution Control Board and applicable central regulator"},
    {"id":"data_privacy_consumer_and_ecommerce","name":"Data privacy, consumer and e-commerce obligations","area":"digital_and_consumer","applies_to":["businesses processing personal data, selling to consumers or operating covered digital-commerce models"],"examples":["privacy notices and data-handling controls","consumer disclosures, grievance and e-commerce obligations where applicable"],"trigger_factors":["personal_data","consumer_sales","platform_role","online_marketplace","cross_border_data"],"authority_level":"central_and_state_as_applicable","verification":"review current notified law, rules and regulator guidance for the actual role and processing"}
)

# Unified country master index. Only India currently has a starter compliance topic dataset.
# Other entries are jurisdiction profiles, not verified legal requirement datasets.
JURISDICTIONS = (
    {"country_code":"IN","country_name":"India","coverage_status":"starter_reference","requirements_dataset":"india_starter","subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"AE","country_name":"United Arab Emirates","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"AU","country_name":"Australia","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"BD","country_name":"Bangladesh","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"CA","country_name":"Canada","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"DE","country_name":"Germany","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"FR","country_name":"France","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"GB","country_name":"United Kingdom","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"JP","country_name":"Japan","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"NZ","country_name":"New Zealand","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"PK","country_name":"Pakistan","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"SA","country_name":"Saudi Arabia","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"SG","country_name":"Singapore","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True},
    {"country_code":"US","country_name":"United States","coverage_status":"framework_only","requirements_dataset":None,"subnational_layers":["state_or_province_where_applicable","district_or_county_where_applicable","municipality_or_local_authority_where_applicable"],"official_verification_required":True}
)

def list_india_requirements():
    return [dict(item) for item in INDIA_REQUIREMENTS]

def get_india_requirement(requirement_id):
    for item in INDIA_REQUIREMENTS:
        if item["id"] == requirement_id:
            return dict(item)
    return None

def list_jurisdictions():
    return [dict(item) for item in JURISDICTIONS]


# India subnational jurisdiction index. This is a coverage index, not a state-law dataset.
INDIA_SUBNATIONAL_JURISDICTIONS = (
    {"subdivision_code":"AP","name":"Andhra Pradesh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"AR","name":"Arunachal Pradesh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"AS","name":"Assam","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"BR","name":"Bihar","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"CG","name":"Chhattisgarh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"GA","name":"Goa","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"GJ","name":"Gujarat","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"HR","name":"Haryana","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"HP","name":"Himachal Pradesh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"JH","name":"Jharkhand","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"KA","name":"Karnataka","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"KL","name":"Kerala","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"MP","name":"Madhya Pradesh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"MH","name":"Maharashtra","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"MN","name":"Manipur","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"ML","name":"Meghalaya","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"MZ","name":"Mizoram","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"NL","name":"Nagaland","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"OD","name":"Odisha","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"PB","name":"Punjab","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"RJ","name":"Rajasthan","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"SK","name":"Sikkim","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"TN","name":"Tamil Nadu","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"TS","name":"Telangana","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"TR","name":"Tripura","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"UP","name":"Uttar Pradesh","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"UK","name":"Uttarakhand","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"WB","name":"West Bengal","subdivision_type":"state","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"AN","name":"Andaman and Nicobar Islands","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"CH","name":"Chandigarh","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"DH","name":"Dadra and Nagar Haveli and Daman and Diu","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"DL","name":"Delhi","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"JK","name":"Jammu and Kashmir","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"LA","name":"Ladakh","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"LD","name":"Lakshadweep","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True},
    {"subdivision_code":"PY","name":"Puducherry","subdivision_type":"union_territory","country_code":"IN","coverage_status":"jurisdiction_profile_only","requirements_dataset":None,"official_verification_required":True}
)

def list_india_subnational_jurisdictions(subdivision_type=None):
    items = [dict(item) for item in INDIA_SUBNATIONAL_JURISDICTIONS]
    if subdivision_type:
        items = [item for item in items if item["subdivision_type"] == subdivision_type]
    return items

def get_india_subnational_jurisdiction(subdivision_code):
    code = subdivision_code.upper()
    for item in INDIA_SUBNATIONAL_JURISDICTIONS:
        if item["subdivision_code"] == code:
            return dict(item)
    return None


def get_jurisdiction(country_code):
    code = country_code.upper()
    for item in JURISDICTIONS:
        if item["country_code"] == code:
            return dict(item)
    return None
