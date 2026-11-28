"""Core metadata guardrails; not a substitute for Shopify API authorization."""
BLOCKED={"token","access_token","refresh_token","client_secret","api_key","secret","password","authorization"}
class ShopifyCorePolicy:
    @staticmethod
    def require_tenant_context(context):
        if context is None or not callable(getattr(context,"validate",None)): raise PermissionError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()
    @staticmethod
    def sanitize(value):
        if isinstance(value,dict): return {k:ShopifyCorePolicy.sanitize(v) for k,v in value.items() if str(k).casefold() not in BLOCKED}
        if isinstance(value,list): return [ShopifyCorePolicy.sanitize(v) for v in value]
        return value
