from ..catalog import get_ai_provider
PROVIDER=get_ai_provider("litellm")
CAPABILITIES=tuple(PROVIDER.get("capabilities",PROVIDER.get("models_or_services",[]))) if PROVIDER else ()
