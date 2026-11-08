"""Offline tests for independent APP composition and lifecycle foundation."""
import unittest
from backend.app.global_ecosystem.global_app_ecosystem import AppComponent,AppComponentAdapter,AppLifecycle,GlobalAppEcosystemManager,GlobalAppEcosystemService,InvalidLifecycleTransition,app_diagnostics,get_component_type,list_component_types
class AppFoundationTests(unittest.TestCase):
    def test_catalog_categories(self):
        ids={x["type_id"] for x in list_component_types()};self.assertTrue({"api-router","middleware","startup-hook","shutdown-hook"}.issubset(ids));self.assertEqual(get_component_type("api_router")["type_id"],"api-router")
    def test_registration_and_duplicate_guard(self):
        m=GlobalAppEcosystemManager();x=AppComponent("router","Main API Router","api-router");m.register_component(x);self.assertIs(m.get_component("router"),x)
        with self.assertRaises(ValueError):m.register_component(x)
        m.register_component(AppComponent("router","Replacement","api-router"),replace=True);self.assertEqual(m.get_component("router").name,"Replacement")
    def test_unknown_type_rejected(self):
        with self.assertRaises(KeyError):GlobalAppEcosystemService().register_component(AppComponent("x","X","unknown"))
    def test_adapter_invocation_and_disabled_guard(self):
        m=GlobalAppEcosystemManager();m.register_component(AppComponent("hook","Startup hook","startup-hook"));m.register_adapter("hook",AppComponentAdapter("hook",lambda x:x+1));self.assertEqual(m.invoke_adapter("hook",4),5)
        m.register_component(AppComponent("hook","Disabled","startup-hook",enabled=False),replace=True)
        with self.assertRaises(RuntimeError):m.invoke_adapter("hook",4)
    def test_missing_adapter_fails_closed(self):
        s=GlobalAppEcosystemService();s.register_component(AppComponent("hook","Hook","startup-hook"))
        with self.assertRaises(RuntimeError):s.invoke_adapter("hook")
    def test_lifecycle_guards_invalid_transition(self):
        l=AppLifecycle();self.assertEqual(l.transition("CONFIGURED"),"CONFIGURED");l.transition("STARTING");l.transition("RUNNING")
        with self.assertRaises(InvalidLifecycleTransition):l.transition("NEW")
    def test_registry_is_non_durable(self):self.assertEqual(GlobalAppEcosystemService().health()["components"]["persistence"],"NOT_CONFIGURED")
    def test_diagnostics_are_safe(self):
        d=app_diagnostics(GlobalAppEcosystemService());self.assertEqual(d["domain"],"APP");self.assertFalse(d["automatic_component_execution"]);self.assertFalse(d["runtime"]["secrets_exposed"])
    def test_layer_boundary(self):
        h=GlobalAppEcosystemService().health();self.assertEqual(h["domain"],"APP");self.assertNotIn("CORE",h);self.assertNotIn("ENGINE",h)
if __name__=="__main__":unittest.main()
