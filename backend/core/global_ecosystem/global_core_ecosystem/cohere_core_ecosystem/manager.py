"""Stable public facade for Cohere CORE."""
from .service import CohereCoreService

class CohereCoreManager:
    def __init__(self):
        self.service = CohereCoreService()

    def list_capabilities(self):
        return self.service.capabilities()

    def validate(self, request):
        return self.service.validate(request)
