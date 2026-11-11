"""DeepSeek ecosystem identifiers and capability boundaries."""
PROVIDER_ID = "deepseek"
PROVIDER_NAME = "DeepSeek"
API_BASE_URL = "https://api.deepseek.com"
API_KEY_ENV = "DEEPSEEK_API_KEY"
DEFAULT_MODELS = ("deepseek-chat", "deepseek-reasoner")
SUPPORTED_API_FAMILIES = ("chat_completions", "responses", "search", "fetch")
STATUS_CATALOG_ONLY = "CATALOG_ONLY"
STATUS_KEY_CONFIGURED = "KEY_CONFIGURED_NOT_CONNECTION_TESTED"
STATUS_CONNECTION_UNVERIFIED = "CONNECTION_NOT_VERIFIED"
