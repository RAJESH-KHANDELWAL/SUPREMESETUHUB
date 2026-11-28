"""Sign-language coverage categories; sign languages are not universal."""
DOMAINS = ("national and regional sign languages", "sign-language interpretation", "signed video content", "deaf community terminology", "sign-language learning", "accessibility review")
def get_sign_language_domains() -> tuple[str, ...]:
 return DOMAINS
