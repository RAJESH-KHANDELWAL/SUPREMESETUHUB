"""Finance, Banking & Insurance industry API domain package."""
INDUSTRY_ID = "finance_banking_insurance"
INDUSTRY_NAME = "Finance, Banking & Insurance"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import FinanceService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "FinanceService"]
