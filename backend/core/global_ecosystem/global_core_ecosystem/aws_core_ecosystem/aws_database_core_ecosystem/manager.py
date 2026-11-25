"""aws_database_core_ecosystem product-family manager facade."""
from .service import AwsDatabaseCoreService
class AwsDatabaseCoreManager:
 def __init__(self)->None:self._service=AwsDatabaseCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsDatabaseCoreManager:return AwsDatabaseCoreManager()
__all__=["AwsDatabaseCoreManager","get_manager"]
