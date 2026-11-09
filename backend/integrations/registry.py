from typing import Any, Dict, List

from .provider.bada_business import BadaBusinessProvider
from .provider.aws import AWSProvider
from .provider.google import GoogleProvider
from .provider.microsoft import MicrosoftProvider
from .provider.salesforce import SalesforceProvider
from .provider.apple import AppleProvider
from .provider.esa import ESAProvider
from .provider.generic import GenericWebProvider
from .provider.openai import OpenAIProvider
from .provider.anthropic import AnthropicProvider
from .provider.adobe import AdobeProvider
from .provider.atlassian import AtlassianProvider
from .provider.cohere import CohereProvider
from .provider.deepseek import DeepSeekProvider
from .provider.github import GitHubProvider
from .provider.huggingface import HuggingFaceProvider
from .provider.ibm import IBMProvider
from .provider.meta import MetaProvider
from .provider.mistral import MistralProvider
from .provider.oracle import OracleProvider


class IntegrationRegistry:
    """Central registry for global integrations."""

    def __init__(self):
        self.providers = {
            "BADA_BUSINESS": BadaBusinessProvider(),
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
        return [provider.metadata() for provider in self.providers.values()]

    def health(self) -> List[Dict[str, Any]]:
        """Return provider health without overstating live connectivity."""
        return [provider.health() for provider in self.providers.values()]

    def get(self, name: str) -> Any:
        """Return a provider by name."""
        if not isinstance(name, str):
            raise TypeError("Provider name must be a string.")
        return self.providers.get(name.upper())


__all__ = ["IntegrationRegistry"]
