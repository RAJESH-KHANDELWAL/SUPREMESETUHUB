"""Retail, e-commerce, consumer goods and electronics taxonomy."""
from __future__ import annotations

BUSINESS_DOMAINS = (
    {"id":"general_retail","name":"General & Specialty Retail","category_id":"general_retail"},
    {"id":"ecommerce_marketplaces","name":"E-commerce & Marketplaces","category_id":"ecommerce_marketplaces"},
    {"id":"wholesale_distribution","name":"Wholesale & Distribution","category_id":"wholesale_distribution"},
    {"id":"consumer_packaged_goods","name":"Consumer Packaged Goods","category_id":"consumer_packaged_goods"},
    {"id":"fashion_apparel","name":"Fashion, Apparel & Accessories","category_id":"fashion_apparel"},
    {"id":"consumer_electronics","name":"Consumer Electronics","category_id":"electronics_appliances"},
    {"id":"mobile_computing_devices","name":"Smartphones, Computers & Mobile Devices","category_id":"electronics_appliances"},
    {"id":"home_appliances","name":"Home & Kitchen Appliances","category_id":"electronics_appliances"},
    {"id":"smart_home_iot","name":"Smart Home & Connected Devices","category_id":"electronics_appliances"},
    {"id":"audio_visual_gaming","name":"Audio, Visual & Gaming Equipment","category_id":"electronics_appliances"},
    {"id":"cameras_imaging","name":"Cameras & Imaging Equipment","category_id":"electronics_appliances"},
    {"id":"beauty_personal_care","name":"Beauty & Personal Care Goods","category_id":"beauty_personal_care"},
    {"id":"grocery_food_retail","name":"Grocery & Food Retail","category_id":"grocery_food_retail"},
    {"id":"home_lifestyle","name":"Home, Furniture & Lifestyle Goods","category_id":"home_lifestyle"},
    {"id":"retail_technology","name":"Retail Technology & POS","category_id":"retail_technology"},
    {"id":"fulfilment_last_mile","name":"E-commerce Fulfilment & Last Mile","category_id":"fulfilment_last_mile"},
    {"id":"franchise_store_networks","name":"Franchise & Store Networks","category_id":"franchise_store_networks"},
    {"id":"electronics_repair_after_sales","name":"Electronics Repair & After-Sales Services","category_id":"electronics_appliances"},
    {"id":"refurbished_recommerce","name":"Refurbished & Second-Hand Electronics","category_id":"electronics_appliances"},
    {"id":"electronics_recycling_ewaste","name":"Electronics Recycling & E-Waste","category_id":"electronics_appliances"},
)

CATEGORIES = [
  {"id":"general_retail","name":"General & Specialty Retail","subcategories":["department_stores","convenience_stores","specialty_shops","multi_brand_retail"]},
  {"id":"ecommerce_marketplaces","name":"E-commerce & Marketplaces","subcategories":["online_marketplaces","direct_to_consumer","social_commerce","b2b_commerce"]},
  {"id":"wholesale_distribution","name":"Factory-to-Market Wholesale & Distribution Channels","subcategories":["factory_direct_sales","factory_outlets_brand_outlets","carrying_forwarding_agents","super_stockists","national_distributors","regional_distributors","authorized_distributors","wholesale_traders","sub_wholesalers","dealers_and_subdealers","retailers","modern_trade_chains","franchise_partners","commission_sales_agents","trade_brokers","import_export_traders","b2b_marketplaces","institutional_bulk_buyers","resellers_and_recommerce","online_d2c_social_commerce","dropshipping_suppliers","government_tender_suppliers","rural_last_mile_trade","clearance_liquidation_traders"]},
  {"id":"consumer_packaged_goods","name":"Consumer Packaged Goods","subcategories":["household_products","personal_care","packaged_foods","beverages"]},
  {"id":"fashion_apparel","name":"Fashion, Apparel & Accessories","subcategories":["clothing","footwear","bags_and_accessories","textiles"]},
  {"id":"electronics_appliances","name":"Electronics & Home Appliances","subcategories":["smartphones","feature_phones","laptops","desktop_computers","tablets","computer_components","computer_peripherals","televisions","monitors","projectors","headphones","earbuds","speakers","home_audio","cameras","lenses","photography_accessories","gaming_consoles","gaming_accessories","refrigerators","washing_machines","air_conditioners","air_coolers","microwave_ovens","kitchen_appliances","water_purifiers","vacuum_cleaners","small_home_appliances","smart_speakers","smart_lighting","smart_thermostats","smart_security_cameras","smart_sensors","home_automation_hubs","wearables_smartwatches","networking_wifi_devices","routers_mesh_wifi","electronic_accessories","device_protection","electronics_repair","authorised_service_centres","refurbished_electronics","device_trade_in","electronics_recycling","ewaste_collection"]},
  {"id":"beauty_personal_care","name":"Beauty & Personal Care","subcategories":["beauty_products","cosmetics","personal_care_brands","salon_supply"]},
  {"id":"grocery_food_retail","name":"Grocery & Food Retail","subcategories":["supermarkets","grocery_delivery","speciality_food_stores","fresh_food"]},
  {"id":"home_lifestyle","name":"Home, Furniture & Lifestyle","subcategories":["furniture","home_decor","kitchenware","home_improvement"]},
  {"id":"retail_technology","name":"Retail Technology & POS","subcategories":["point_of_sale","inventory_software","retail_analytics","omnichannel_platforms"]},
  {"id":"fulfilment_last_mile","name":"E-commerce Fulfilment & Last Mile","subcategories":["order_fulfilment","warehousing","last_mile_delivery","returns_management"]},
  {"id":"franchise_store_networks","name":"Franchise & Store Networks","subcategories":["retail_franchising","dealerships","store_expansion","franchise_advisory"]}
]

def list_categories():
    return [{**x, "subcategories": list(x["subcategories"])} for x in CATEGORIES]

def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id:
            return {**x, "subcategories": list(x["subcategories"])}
    return None

def list_business_domains():
    return [dict(x) for x in BUSINESS_DOMAINS]

def get_business_domain(domain_id: str):
    for x in BUSINESS_DOMAINS:
        if x["id"] == domain_id:
            return dict(x)
    return None
