"""Retail, e-commerce, wholesale and consumer-goods taxonomy."""
from __future__ import annotations

CATEGORIES = [
  {"id":"general_retail","name":"General & Specialty Retail","subcategories":["department_stores","convenience_stores","specialty_shops","multi_brand_retail"]},
  {"id":"ecommerce_marketplaces","name":"E-commerce & Marketplaces","subcategories":["online_marketplaces","direct_to_consumer","social_commerce","b2b_commerce"]},
  {"id":"wholesale_distribution","name":"Factory-to-Market Wholesale & Distribution Channels","subcategories":[
    "factory_direct_sales","factory_outlets_brand_outlets","carrying_forwarding_agents","super_stockists","national_distributors","regional_distributors","authorized_distributors","wholesale_traders","sub_wholesalers","dealers_and_subdealers","retailers","modern_trade_chains","franchise_partners","commission_sales_agents","trade_brokers","import_export_traders","b2b_marketplaces","institutional_bulk_buyers","resellers_and_recommerce","online_d2c_social_commerce","dropshipping_suppliers","government_tender_suppliers","rural_last_mile_trade","clearance_liquidation_traders"
  ]},
  {"id":"consumer_packaged_goods","name":"Consumer Packaged Goods","subcategories":["household_products","personal_care","packaged_foods","beverages"]},
  {"id":"fashion_apparel","name":"Fashion, Apparel & Accessories","subcategories":["clothing","footwear","bags_and_accessories","textiles"]},
  {"id":"electronics_appliances","name":"Electronics & Home Appliances","subcategories":["consumer_electronics","mobile_devices","home_appliances","repair_accessories"]},
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
