"""Read-only APP diagnostics."""
def app_diagnostics(service):
    h=service.health();return {"domain":"APP","ecosystem":"GLOBAL_APP_ECOSYSTEM","status":h["status"],"lifecycle":h["lifecycle"],"components":h["components"],"adapters":h["adapters"],"runtime":h["runtime"],"automatic_component_execution":False}
__all__=["app_diagnostics"]
