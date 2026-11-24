"""Controller facade for SUPREME PRINT ON DEMAND."""
from backend.print_on_demand.service import PrintOnDemandService


class PrintOnDemandController:
    def __init__(self, service: PrintOnDemandService | None = None):
        self.service = service or PrintOnDemandService()

    def catalog(self, market="IN"):
        return self.service.catalog(market)

    def quote(self, **kwargs):
        return self.service.quote(**kwargs)

    def create_brief(self, **kwargs):
        return self.service.create_brief(**kwargs)

    def list_briefs(self, user_id):
        return self.service.list_briefs(user_id)
