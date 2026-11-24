from ..catalog import get_ai_provider
PROVIDER=get_ai_provider("semantic_kernel")
CAPABILITIES=tuple(PROVIDER.get("capabilities",PROVIDER.get("models_or_services",[]))) if PROVIDER else ()
