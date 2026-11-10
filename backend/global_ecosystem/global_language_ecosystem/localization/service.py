"""Locale settings validation for applications and content."""
from dataclasses import dataclass


@dataclass(frozen=True)
class LocaleSettings:
    locale: str
    timezone: str | None = None
    currency: str | None = None
    date_format: str | None = None
    number_format: str | None = None
    text_direction: str = "ltr"


def validate_locale_settings(settings: LocaleSettings) -> LocaleSettings:
    if not settings.locale.strip() or "_" not in settings.locale and "-" not in settings.locale:
        raise ValueError("locale should use a language-region form such as hi-IN or en-US")
    if settings.text_direction not in {"ltr", "rtl"}:
        raise ValueError("text_direction must be ltr or rtl")
    return settings
