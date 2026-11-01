"""Initial industry navigation registry; taxonomy metadata only."""
INDUSTRY_ECOSYSTEMS = (
 {"id":"agriculture-food","name":"Agriculture, Food and Natural Resources","status":"taxonomy_only"},
 {"id":"manufacturing-industry","name":"Manufacturing and Industrial Services","status":"taxonomy_only"},
 {"id":"technology-software","name":"Technology, Software, AI and Cloud","status":"taxonomy_only"},
 {"id":"finance-banking","name":"Finance, Banking and Insurance","status":"taxonomy_only"},
 {"id":"real-estate-construction","name":"Real Estate and Construction","status":"taxonomy_only"},
 {"id":"professional-services","name":"Legal, Consulting and Professional Services","status":"taxonomy_only"},
 {"id":"retail-ecommerce","name":"Retail, E-commerce and Consumer Goods","status":"taxonomy_only"},
 {"id":"transport-logistics","name":"Transport, Mobility and Logistics","status":"taxonomy_only"},
)
def list_industries():
    return [dict(x) for x in INDUSTRY_ECOSYSTEMS]
