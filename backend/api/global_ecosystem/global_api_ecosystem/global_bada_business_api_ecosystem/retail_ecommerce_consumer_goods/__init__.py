"""Retail, E-commerce & Consumer Goods domain package."""
INDUSTRY_ID = "retail_ecommerce_consumer_goods"
INDUSTRY_NAME = "Retail, E-commerce & Consumer Goods"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import RetailService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "RetailService"]
