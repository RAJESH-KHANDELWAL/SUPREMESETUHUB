"""Factory-to-customer distribution channel taxonomy.

The stages describe channel participants and hand-offs; actual routes vary by
product, geography, contract and business model.
"""

CHANNELS = (
    {"id": "factory_dispatch", "name": "Factory Dispatch", "stage": "origin", "participants": ["manufacturer", "factory_dispatch_team"], "next_channels": ["finished_goods_warehouse", "end_customer_handover"]},
    {"id": "finished_goods_warehouse", "name": "Finished Goods Warehouse", "stage": "origin_handling", "participants": ["manufacturer_warehouse", "inventory_team"], "next_channels": ["company_depot", "carrying_forwarding_agents", "distribution_centres"]},
    {"id": "company_depot", "name": "Company Depot", "stage": "primary_distribution", "participants": ["company_depot_operator", "regional_sales_office"], "next_channels": ["carrying_forwarding_agents", "regional_distributors", "wholesalers"]},
    {"id": "carrying_forwarding_agents", "name": "Carrying & Forwarding Agents", "stage": "primary_distribution", "participants": ["c_and_f_agent", "stock_handling_partner"], "next_channels": ["super_stockists", "regional_distributors", "dealers_subdealers"]},
    {"id": "distribution_centres", "name": "Central / Regional Distribution Centres", "stage": "primary_distribution", "participants": ["distribution_centre_operator", "company_supply_team"], "next_channels": ["super_stockists", "regional_distributors", "modern_retail_chains"]},
    {"id": "super_stockists", "name": "Super Stockists", "stage": "primary_distribution", "participants": ["super_stockist"], "next_channels": ["national_distributors", "regional_distributors", "wholesalers"]},
    {"id": "national_distributors", "name": "National Distributors", "stage": "distribution", "participants": ["national_distributor"], "next_channels": ["regional_distributors", "state_distributors", "modern_retail_chains"]},
    {"id": "regional_distributors", "name": "Regional Distributors", "stage": "distribution", "participants": ["regional_distributor"], "next_channels": ["state_distributors", "district_distributors", "wholesalers", "dealers_subdealers"]},
    {"id": "state_distributors", "name": "State Distributors", "stage": "distribution", "participants": ["state_distributor"], "next_channels": ["district_distributors", "wholesalers", "dealers_subdealers"]},
    {"id": "district_distributors", "name": "District Distributors", "stage": "distribution", "participants": ["district_distributor"], "next_channels": ["wholesalers", "sub_wholesalers", "dealers_subdealers", "retailers_shopkeepers"]},
    {"id": "authorized_distributors", "name": "Authorized Distributors", "stage": "distribution", "participants": ["authorized_distributor"], "next_channels": ["dealers_subdealers", "retailers_shopkeepers", "institutional_bulk_buyers"]},
    {"id": "wholesalers", "name": "Wholesalers", "stage": "resale", "participants": ["wholesaler", "bulk_trader"], "next_channels": ["sub_wholesalers", "retailers_shopkeepers", "dealers_subdealers", "institutional_bulk_buyers"]},
    {"id": "sub_wholesalers", "name": "Sub-Wholesalers", "stage": "resale", "participants": ["sub_wholesaler"], "next_channels": ["retailers_shopkeepers", "dealers_subdealers", "retailers_shopkeepers"]},
    {"id": "stockists", "name": "Stockists", "stage": "resale", "participants": ["stockist", "inventory_reseller"], "next_channels": ["dealers_subdealers", "retailers_shopkeepers", "institutional_bulk_buyers"]},
    {"id": "dealers_subdealers", "name": "Dealers & Sub-Dealers", "stage": "resale", "participants": ["dealer", "sub_dealer"], "next_channels": ["retailers_shopkeepers", "end_customer_handover", "institutional_bulk_buyers"]},
    {"id": "retailers_shopkeepers", "name": "Retailers & Shopkeepers", "stage": "customer_facing", "participants": ["retailer", "shopkeeper"], "next_channels": ["end_customer_handover"]},
    {"id": "modern_retail_chains", "name": "Modern Retail Chains & Supermarkets", "stage": "customer_facing", "participants": ["supermarket", "department_store", "retail_chain"], "next_channels": ["end_customer_handover"]},
    {"id": "franchise_stores", "name": "Franchise Stores & Store Networks", "stage": "customer_facing", "participants": ["franchisee", "franchisor_store_network"], "next_channels": ["end_customer_handover"]},
    {"id": "b2b_marketplaces", "name": "B2B Marketplaces", "stage": "digital_trade", "participants": ["b2b_marketplace", "business_seller"], "next_channels": ["institutional_bulk_buyers", "wholesalers", "retailers_shopkeepers"]},
    {"id": "b2c_ecommerce_marketplaces", "name": "B2C E-commerce Marketplaces", "stage": "digital_customer_facing", "participants": ["ecommerce_marketplace", "online_seller"], "next_channels": ["end_customer_handover"]},
    {"id": "direct_to_consumer", "name": "Direct-to-Consumer Channels", "stage": "direct_channel", "participants": ["manufacturer_brand", "d2c_operator"], "next_channels": ["end_customer_handover"]},
    {"id": "social_commerce_online_sellers", "name": "Social Commerce & Online Sellers", "stage": "digital_customer_facing", "participants": ["social_commerce_seller", "online_reseller"], "next_channels": ["end_customer_handover"]},
    {"id": "institutional_bulk_buyers", "name": "Institutional & Bulk Buyers", "stage": "business_customer", "participants": ["institution", "corporate_buyer", "bulk_procurement_team"], "next_channels": ["end_customer_handover"]},
    {"id": "import_export_channel_partners", "name": "Import, Export & International Channel Partners", "stage": "cross_border_channel", "participants": ["exporter", "importer", "international_distributor", "trade_agent"], "next_channels": ["import_export_channel_partners", "wholesalers", "retailers_shopkeepers", "end_customer_handover"]},
    {"id": "end_customer_handover", "name": "Final Customer Handover", "stage": "final_handover", "participants": ["consumer", "business_end_user"], "next_channels": []},
)

def list_channels():
    return [dict(item) for item in CHANNELS]

def get_channel(channel_id):
    for item in CHANNELS:
        if item["id"] == channel_id:
            return dict(item)
    return None
