from .. import _manifest
class ProductCoreService:
 def describe(self): return dict(_manifest())
 def readiness(self):
  m=self.describe(); return {"product_id":m["product_id"],"catalog_ready":True,"live_connection":False,"status":"CATALOG_ONLY" if not m.get("api") or m["integration_mode"] in ("PRODUCT_INFORMATION_ONLY","SDK_INTEGRATION") else "ADAPTER_NOT_VERIFIED"}
