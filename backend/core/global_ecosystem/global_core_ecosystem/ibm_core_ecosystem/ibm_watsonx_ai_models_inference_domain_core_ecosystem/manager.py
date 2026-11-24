"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMWatsonxAiModelsInferenceCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("WATSONX_AI_MODELS_INFERENCE")
