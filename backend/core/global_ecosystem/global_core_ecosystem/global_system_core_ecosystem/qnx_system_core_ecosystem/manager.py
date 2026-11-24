"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class QnxSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "qnx"

def get_manager() -> QnxSystemCoreManager:
    return QnxSystemCoreManager()
