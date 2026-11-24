from .services.core_service import ProductCoreService
service=ProductCoreService()
def describe():return service.describe()
def readiness():return service.readiness()
