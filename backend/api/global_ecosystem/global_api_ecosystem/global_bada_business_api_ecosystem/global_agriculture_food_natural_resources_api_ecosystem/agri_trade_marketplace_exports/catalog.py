"""Catalog metadata for Agri Trade & Marketplaces."""
CATEGORY_ID = "agri_trade_marketplace_exports"
CATEGORY_NAME = "Agri Trade & Marketplaces"
DESCRIPTION = "Wholesale, retail, commodity markets, exports, imports and B2B/B2C trade."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
