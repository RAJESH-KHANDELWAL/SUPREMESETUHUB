CATEGORIES=(
    {"id":"textile_fibres","name":"Textile Fibres & Yarns","subcategories":["natural_fibres","synthetic_fibres","blended_yarns","technical_yarns"]},
    {"id":"textile_manufacturing","name":"Textile Manufacturing","subcategories":["spinning","weaving","knitting","nonwoven_fabrics"]},
    {"id":"fabric_processing","name":"Fabric Processing & Finishing","subcategories":["dyeing","printing","bleaching","finishing_treatments"]},
    {"id":"apparel_manufacturing","name":"Apparel Manufacturing","subcategories":["garment_making","cut_make_trim","fashion_production","uniform_manufacturing"]},
    {"id":"fashion_design","name":"Fashion Design & Product Development","subcategories":["fashion_design_studios","pattern_making","sampling","product_development"]},
    {"id":"fashion_retail","name":"Fashion Retail & E-commerce","subcategories":["apparel_stores","online_fashion","fashion_marketplaces","brand_outlets"]},
    {"id":"footwear_leather","name":"Footwear & Leather Goods","subcategories":["footwear_manufacturing","leather_goods","accessories","sustainable_alternatives"]},
    {"id":"home_textiles","name":"Home Textiles","subcategories":["bedding","curtains","upholstery","rugs_and_carpets"]},
    {"id":"technical_textiles","name":"Technical & Industrial Textiles","subcategories":["medical_textiles","automotive_textiles","protective_textiles","geotextiles"]},
    {"id":"fashion_services","name":"Fashion Services","subcategories":["fashion_marketing","styling","fashion_photography","fashion_events"]},
    {"id":"textile_recycling","name":"Textile Recycling & Circularity","subcategories":["fibre_recycling","garment_reuse","textile_waste_management","circular_materials"]},
    {"id":"textile_trade","name":"Textile Trade & Sourcing","subcategories":["fabric_sourcing","garment_exports","supply_agents","quality_inspection"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for x in CATEGORIES:
  if x["id"]==category_id: return dict(x)
 return None
