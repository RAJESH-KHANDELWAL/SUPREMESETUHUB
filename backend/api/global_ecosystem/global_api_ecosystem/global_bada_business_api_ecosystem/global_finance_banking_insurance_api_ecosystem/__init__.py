"""Finance, Banking & Insurance industry API domain package."""
INDUSTRY_ID = "finance_banking_insurance"
INDUSTRY_NAME = "Finance, Banking & Insurance"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .catalog import FINANCE_BANKING_INSURANCE_CATEGORIES
SUBCATEGORY_IDS = tuple(dict.fromkeys(
    [item["id"] for item in FINANCE_BANKING_INSURANCE_CATEGORIES]
    + [sub for item in FINANCE_BANKING_INSURANCE_CATEGORIES for sub in item["subcategories"]]
))
from .service import FinanceService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "SUBCATEGORY_IDS", "FinanceService"]
