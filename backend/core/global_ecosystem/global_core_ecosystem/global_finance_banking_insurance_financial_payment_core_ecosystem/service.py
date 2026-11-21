"""Application-facing read-only finance catalogue service."""

from .manager import FinanceEcosystemManager


class FinanceEcosystemService:
    def __init__(self, manager=None):
        self.manager = manager or FinanceEcosystemManager()

    def overview(self):
        return {
            "domains": self.manager.list_domains(),
            "package_count": len(self.manager.list_packages()),
            "transaction_execution_enabled": False,
        }

    def package(self, package_name):
        return self.manager.find_package(package_name)
