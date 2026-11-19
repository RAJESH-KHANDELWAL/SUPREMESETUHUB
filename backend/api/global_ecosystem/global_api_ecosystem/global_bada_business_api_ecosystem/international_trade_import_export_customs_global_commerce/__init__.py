"""International Trade, Import-Export, Customs & Global Commerce API ecosystem."""
INDUSTRY_ID = "international_trade_import_export_customs_global_commerce"
INDUSTRY_NAME = "International Trade, Import-Export, Customs & Global Commerce API Ecosystem"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import InternationalTradeService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "InternationalTradeService"]
