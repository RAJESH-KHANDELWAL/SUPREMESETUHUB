"""Adapter exposing Android Foundation through the global ecosystem."""

from ... import AndroidFoundationManager


class GlobalAndroidEcosystemManager:
    NAME = "GLOBAL ANDROID ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self, component):
        if component is None:
            raise ValueError("Foundation component is required")
        self._component = component

    def get_component(self):
        return self._component

    def project_contract(self):
        return self._component.project_contract()

    def status(self):
        return {
            "status": "INTEGRATED",
            "ecosystem": "GLOBAL_ANDROID_ECOSYSTEM",
            "component_key": "android",
            "component_status": self._component.status()["status"],
        }


def get_manager():
    return GlobalAndroidEcosystemManager(AndroidFoundationManager())
