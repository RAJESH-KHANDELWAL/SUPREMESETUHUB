"""Compatibility facade for the maintained finance_banking_insurance package."""
from .industry_api_ecosystems import finance_banking_insurance as _implementation

INDUSTRY_ID = _implementation.INDUSTRY_ID
INDUSTRY_NAME = _implementation.INDUSTRY_NAME
COVERAGE = _implementation.COVERAGE
CHANNELS = _implementation.CHANNELS
STATUS = _implementation.STATUS
FinanceService = _implementation.FinanceService
__path__ = _implementation.__path__

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "FinanceService"]
