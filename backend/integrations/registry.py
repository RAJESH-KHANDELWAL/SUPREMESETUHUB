from typing import Any, Dict, List

from .providers.aws import AWSProvider
from .providers.google import GoogleProvider
from .providers.microsoft import MicrosoftProvider
from .providers.salesforce import SalesforceProvider
from .providers.apple import AppleProvider
from .providers.esa import ESAProvider
from .providers.generic import GenericWebProvider
from .providers.openai import OpenAIProvider
from .providers.anthropic import AnthropicProvider
from .providers.adobe import AdobeProvider
from .providers.atlassian import AtlassianProvider
from .providers.cohere import CohereProvider
from .providers.deepseek import DeepSeekProvider
from .providers.github import GitHubProvider
from .providers.huggingface import HuggingFaceProvider
from .providers.ibm import IBMProvider
from .providers.meta import MetaProvider
from .providers.mistral import MistralProvider
from .providers.oracle import OracleProvider


class IntegrationRegistry:
    """Central registry for global integrations."""

    def __init__(self):
        self.providers = {
            "GOOGLE": GoogleProvider(),
            "OPENAI": OpenAIProvider(),
            "ANTHROPIC": AnthropicProvider(),
            "ADOBE": AdobeProvider(),
            "ATLASSIAN": AtlassianProvider(),
            "COHERE": CohereProvider(),
            "DEEPSEEK": DeepSeekProvider(),
            "GITHUB": GitHubProvider(),
            "HUGGINGFACE": HuggingFaceProvider(),
            "IBM": IBMProvider(),
            "MICROSOFT": MicrosoftProvider(),
            "SALESFORCE": SalesforceProvider(),
            "META": MetaProvider(),
            "MISTRAL": MistralProvider(),
            "AWS": AWSProvider(),
            "APPLE": AppleProvider(),
            "ORACLE": OracleProvider(),
            "ESA": ESAProvider(),
            "GENERIC_WEB": GenericWebProvider(),
        }

    def list(self) -> List[Dict[str, Any]]:
        """Return metadata for all registered providers."""
        return [
            provider.metadata()
            for provider in self.providers.values()
        ]

    def health(self) -> List[Dict[str, Any]]:
        """Return configuration readiness without claiming live connectivity."""
        return [
            provider.health()
            for provider in self.providers.values()
        ]

    def get(self, name: str) -> Any:
        """Return a provider by name."""
        if not isinstance(name, str):
            raise TypeError("Provider name must be a string.")
        return self.providers.get(name.upper())


__all__ = [
    "IntegrationRegistry",
]
