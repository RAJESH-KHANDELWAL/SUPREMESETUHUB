from ..ecosystem_service import PlatformService
def get_status()->dict:return PlatformService().describe()
