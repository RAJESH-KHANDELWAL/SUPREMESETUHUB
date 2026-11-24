from .. import _manifest
class ProductCoreService:
 def describe(self):return dict(_manifest())
 def readiness(self):return {'product_id':_manifest()['product_id'],'catalog_ready':True,'live_connection':False,'status':'ADAPTER_NOT_VERIFIED'}
