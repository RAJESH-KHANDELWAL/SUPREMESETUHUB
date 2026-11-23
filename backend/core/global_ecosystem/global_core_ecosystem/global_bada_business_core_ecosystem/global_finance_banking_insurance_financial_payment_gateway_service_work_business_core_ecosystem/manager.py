"""Stable public manager for the finance service/work/business ecosystem."""
from .catalog import get_catalog
from .domain_catalog import get_domain, list_domains, search_domains, validate_mappings
from .orchestrator import FinanceServiceWorkBusinessOrchestrator
from .service import classify, status as service_status

class FinanceServiceWorkBusinessManager:
    NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"

    def __init__(self):
        self._orchestrator = FinanceServiceWorkBusinessOrchestrator()

    def catalog(self):
        return get_catalog()

    def list_domains(self):
        return list_domains()

    def get_domain(self, domain_id):
        return get_domain(domain_id)

    def search(self, keyword):
        return search_domains(keyword)

    def classify(self, domain_id, service_type):
        return classify(domain_id, service_type)

    def validate(self):
        return validate_mappings()

    def health(self):
        return self._orchestrator.health()

    def status(self):
        return {**service_status(), "name": self.NAME, "ecosystem_id": self.ECOSYSTEM_ID}

    def dependency_map(self):
        return self._orchestrator.dependency_map()

def get_manager():
    return FinanceServiceWorkBusinessManager()

__all__ = ["FinanceServiceWorkBusinessManager", "get_manager"]
