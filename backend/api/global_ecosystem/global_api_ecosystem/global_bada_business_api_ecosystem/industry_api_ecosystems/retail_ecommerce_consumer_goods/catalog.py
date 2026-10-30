"""Retail, E-commerce & Consumer Goods category taxonomy."""
from __future__ import annotations
CATEGORIES = [
  {
    "id": "general_retail",
    "name": "General & Specialty Retail",
    "subcategories": [
      "department_stores",
      "convenience_stores",
      "specialty_shops",
      "multi_brand_retail"
    ]
  },
  {
    "id": "ecommerce_marketplaces",
    "name": "E-commerce & Marketplaces",
    "subcategories": [
      "online_marketplaces",
      "direct_to_consumer",
      "social_commerce",
      "b2b_commerce"
    ]
  },
  {
    "id": "wholesale_distribution",
    "name": "Wholesale & Distribution",
    "subcategories": [
      "wholesale_trade",
      "distributor_networks",
      "stockists_and_dealers",
      "sales_agents"
    ]
  },
  {
    "id": "consumer_packaged_goods",
    "name": "Consumer Packaged Goods",
    "subcategories": [
      "household_products",
      "personal_care",
      "packaged_foods",
      "beverages"
    ]
  },
  {
    "id": "fashion_apparel",
    "name": "Fashion, Apparel & Accessories",
    "subcategories": [
      "clothing",
      "footwear",
      "bags_and_accessories",
      "textiles"
    ]
  },
  {
    "id": "electronics_appliances",
    "name": "Electronics & Home Appliances",
    "subcategories": [
      "consumer_electronics",
      "mobile_devices",
      "home_appliances",
      "repair_accessories"
    ]
  },
  {
    "id": "beauty_personal_care",
    "name": "Beauty & Personal Care",
    "subcategories": [
      "beauty_products",
      "cosmetics",
      "personal_care_brands",
      "salon_supply"
    ]
  },
  {
    "id": "grocery_food_retail",
    "name": "Grocery & Food Retail",
    "subcategories": [
      "supermarkets",
      "grocery_delivery",
      "speciality_food_stores",
      "fresh_food"
    ]
  },
  {
    "id": "home_lifestyle",
    "name": "Home, Furniture & Lifestyle",
    "subcategories": [
      "furniture",
      "home_decor",
      "kitchenware",
      "home_improvement"
    ]
  },
  {
    "id": "retail_technology",
    "name": "Retail Technology & POS",
    "subcategories": [
      "point_of_sale",
      "inventory_software",
      "retail_analytics",
      "omnichannel_platforms"
    ]
  },
  {
    "id": "fulfilment_last_mile",
    "name": "E-commerce Fulfilment & Last Mile",
    "subcategories": [
      "order_fulfilment",
      "warehousing",
      "last_mile_delivery",
      "returns_management"
    ]
  },
  {
    "id": "franchise_store_networks",
    "name": "Franchise & Store Networks",
    "subcategories": [
      "retail_franchising",
      "dealerships",
      "store_expansion",
      "franchise_advisory"
    ]
  }
]
def list_categories():
    return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
