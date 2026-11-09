"""Beauty and lifestyle-products taxonomy for India and global markets.

Fashion apparel/textiles and general personal-care services remain in their
existing canonical ecosystems; this package focuses on beauty products,
beauty-sector operations and related discovery.
"""

BUSINESS_DOMAINS = (
    {"id":"beauty_cosmetics","name":"Beauty & Cosmetics","category_id":"cosmetics_products"},
    {"id":"skincare_products","name":"Skincare Products","category_id":"skincare_products"},
    {"id":"haircare_products","name":"Haircare Products","category_id":"haircare_products"},
    {"id":"makeup_products","name":"Makeup Products & Professional Supplies","category_id":"cosmetics_products"},
    {"id":"fragrance_perfume","name":"Fragrance & Perfume","category_id":"fragrance"},
    {"id":"nail_beauty_products","name":"Nail Beauty Products","category_id":"nail_beauty"},
    {"id":"beauty_tools_devices","name":"Beauty Tools & Devices","category_id":"beauty_tools_devices"},
    {"id":"beauty_ingredients_formulation","name":"Beauty Ingredients & Formulation","category_id":"ingredients_formulation"},
    {"id":"beauty_manufacturing_private_label","name":"Beauty Manufacturing & Private Label","category_id":"manufacturing_private_label"},
    {"id":"beauty_packaging","name":"Beauty Packaging & Components","category_id":"packaging_supply"},
    {"id":"beauty_testing_compliance","name":"Beauty Product Testing & Compliance Information","category_id":"testing_compliance"},
    {"id":"beauty_wholesale","name":"Beauty Wholesale & Bulk Supply","category_id":"trade_distribution"},
    {"id":"beauty_distribution","name":"Beauty Distribution & Import/Export","category_id":"trade_distribution"},
    {"id":"beauty_retail","name":"Beauty Retail & Stores","category_id":"retail_ecommerce"},
    {"id":"beauty_ecommerce","name":"Beauty E-commerce & Marketplaces","category_id":"retail_ecommerce"},
    {"id":"clean_sustainable_beauty","name":"Clean, Ethical & Sustainable Beauty","category_id":"sustainable_beauty"},
    {"id":"beauty_technology","name":"Beauty Technology & Digital Platforms","category_id":"beauty_technology"},
    {"id":"beauty_education_training","name":"Beauty Education & Product Training","category_id":"education_professional"},
    {"id":"beauty_brands_marketing","name":"Beauty Brands, Marketing & Brand Services","category_id":"brands_marketing"},
    {"id":"beauty_professional_supplies","name":"Professional Beauty & Salon Supplies","category_id":"professional_supplies"},
)

CATEGORIES = (
    {"id":"cosmetics_products","name":"Cosmetics & Makeup Products","subcategories":["face_makeup","eye_makeup","lip_products","body_cosmetics","professional_makeup_supplies"]},
    {"id":"skincare_products","name":"Skincare Products","subcategories":["cleansers","moisturisers","serums","sunscreen_products","body_care_products","nonclinical_skincare"]},
    {"id":"haircare_products","name":"Haircare Products","subcategories":["shampoo_conditioner","hair_treatments","hair_styling_products","hair_colour_products","scalp_care_products"]},
    {"id":"fragrance","name":"Fragrance & Perfume","subcategories":["perfumes","deodorants","body_mists","essential_oil_fragrance_products","fragrance_gifting"]},
    {"id":"nail_beauty","name":"Nail Beauty Products","subcategories":["nail_polish","nail_care_products","nail_art_supplies","artificial_nails","professional_nail_supplies"]},
    {"id":"beauty_tools_devices","name":"Beauty Tools & Devices","subcategories":["beauty_gadgets","skincare_devices","hair_styling_tools","makeup_tools_brushes","salon_equipment"]},
    {"id":"ingredients_formulation","name":"Ingredients & Product Formulation","subcategories":["cosmetic_raw_materials","formulation_labs","ingredient_sourcing","product_development","contract_formulation"]},
    {"id":"manufacturing_private_label","name":"Manufacturing & Private Label","subcategories":["cosmetics_manufacturing","skincare_manufacturing","haircare_manufacturing","private_label_products","contract_manufacturing"]},
    {"id":"packaging_supply","name":"Packaging & Components","subcategories":["bottles_jars","tubes_pumps","closures_dispensers","labels_cartons","sustainable_packaging"]},
    {"id":"testing_compliance","name":"Testing, Safety & Compliance Information","subcategories":["product_safety_testing","stability_testing","quality_documentation","label_information","regulatory_guidance_referrals"]},
    {"id":"trade_distribution","name":"Wholesale, Trade & Distribution","subcategories":["beauty_wholesalers","authorised_distributors","import_export","bulk_supply","trade_sourcing"]},
    {"id":"retail_ecommerce","name":"Beauty Retail & E-commerce","subcategories":["beauty_stores","online_beauty_retail","beauty_marketplaces","brand_webshops","omnichannel_retail"]},
    {"id":"sustainable_beauty","name":"Clean, Ethical & Sustainable Beauty","subcategories":["refillable_products","cruelty_free_claims_information","vegan_beauty_products","responsible_sourcing","circular_packaging"]},
    {"id":"beauty_technology","name":"Beauty Technology & Digital Platforms","subcategories":["virtual_try_on","skin_hair_assessment_tools","beauty_recommendation_software","salon_retail_software","beauty_analytics"]},
    {"id":"education_professional","name":"Beauty Education & Professional Training","subcategories":["cosmetology_education","makeup_training","product_knowledge_training","beauty_business_training","professional_development"]},
    {"id":"brands_marketing","name":"Beauty Brands & Marketing","subcategories":["brand_development","beauty_content_marketing","influencer_campaign_services","product_launch_support","brand_directory_discovery"]},
    {"id":"professional_supplies","name":"Professional Beauty & Salon Supplies","subcategories":["salon_consumables","professional_hair_products","esthetician_supplies","spa_product_supplies","salon_equipment_supply"]},
)

def list_categories():
    return [{**item, "subcategories": list(item["subcategories"])} for item in CATEGORIES]

def get_category(category_id):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return {**item, "subcategories": list(item["subcategories"])}
    return None

def list_business_domains():
    return [dict(item) for item in BUSINESS_DOMAINS]

def get_business_domain(domain_id):
    for item in BUSINESS_DOMAINS:
        if item["id"] == domain_id:
            return dict(item)
    return None
