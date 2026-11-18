"""Application service for healthcare taxonomy operations."""
from .catalog import get_domain, list_domains
from .models import EcosystemStatus

class HealthcareMedicalLifeSciencesService:
    def status(self):
        return EcosystemStatus()
    def list_domains(self):
        return list_domains()
    def get_domain(self, domain_id):
        return get_domain(domain_id)
