"""Offline tests for the shared app adapter factory."""
import unittest
from backend.global_ecosystem.global_app_ecosystem.adapters.factory import AppAdapterFactory
from backend.global_ecosystem.global_app_ecosystem.adapters.errors import ProviderNotRegisteredError

class AdapterFactoryTests(unittest.TestCase):
    def test_register_and_create(self):
        factory=AppAdapterFactory()
        factory.register("demo", lambda marker=None: {"marker": marker})
        self.assertEqual(factory.create("DEMO", marker="ok"), {"marker":"ok"})
        self.assertEqual(factory.registered(), ("demo",))
    def test_unknown_provider_is_explicit(self):
        with self.assertRaises(ProviderNotRegisteredError):
            AppAdapterFactory().create("missing")
    def test_duplicate_registration_is_rejected(self):
        factory=AppAdapterFactory(); factory.register("demo", lambda: None)
        with self.assertRaises(ValueError): factory.register("demo", lambda: None)

if __name__ == "__main__": unittest.main()
