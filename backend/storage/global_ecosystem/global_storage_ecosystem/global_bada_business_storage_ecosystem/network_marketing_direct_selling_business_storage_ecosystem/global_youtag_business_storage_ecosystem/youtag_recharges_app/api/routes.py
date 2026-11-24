from ..ecosystem_service import AppService
def get_status()->dict:return AppService().describe()
