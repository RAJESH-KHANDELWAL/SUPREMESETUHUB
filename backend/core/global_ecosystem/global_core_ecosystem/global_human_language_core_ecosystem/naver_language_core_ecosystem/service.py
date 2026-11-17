"""Provider Core service facade; no external calls."""
from .services.core_service import service


def describe():
    return service.describe()


def readiness():
    return service.readiness()


def capabilities():
    return service.capabilities()
