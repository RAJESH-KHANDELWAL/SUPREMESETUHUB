"""aws_billing_cost_core_ecosystem product-family manager facade."""
from .service import AwsBillingCostCoreService
class AwsBillingCostCoreManager:
 def __init__(self)->None:self._service=AwsBillingCostCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsBillingCostCoreManager:return AwsBillingCostCoreManager()
__all__=["AwsBillingCostCoreManager","get_manager"]
