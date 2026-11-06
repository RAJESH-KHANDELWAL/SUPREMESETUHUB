"""Master catalog for the Global Language API Ecosystem.

Mirrors the repository's provider/category catalog architecture. This is a
discovery index: catalog entries do not imply live provider integrations.
"""
from __future__ import annotations

GLOBAL_LANGUAGE_API_ECOSYSTEM = {
    "name": "GLOBAL LANGUAGE API ECOSYSTEM",
    "family": "LANGUAGE",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "catalog_scope": "Language identifiers, locales, scripts, translation, speech, localization, language intelligence, dictionaries, and educational adult-language resources.",
    "existing_provider_modules": {
        "google": "google_language_api_ecosystem/google_language_api_ecosystem.py",
        "microsoft": "microsoft_language_api_ecosystem/microsoft_language_api_ecosystem.py",
    },
    "category_modules": {
        "language_catalog": "language_catalog_ecosystem/language_catalog_api_ecosystem.py",
        "translation": "translation_language_ecosystem/translation_language_api_ecosystem.py",
        "speech": "speech_language_ecosystem/speech_language_api_ecosystem.py",
        "language_detection": "language_detection_ecosystem/language_detection_api_ecosystem.py",
        "transliteration": "transliteration_language_ecosystem/transliteration_language_api_ecosystem.py",
        "scripts_and_writing_systems": "scripts_writing_system_ecosystem/scripts_writing_system_api_ecosystem.py",
        "localization_and_locales": "localization_locale_ecosystem/localization_locale_api_ecosystem.py",
        "dictionary_and_lexicon": "dictionary_lexicon_ecosystem/dictionary_lexicon_api_ecosystem.py",
        "ocr_and_document_language": "ocr_document_language_ecosystem/ocr_document_language_api_ecosystem.py",
        "adult_language": "adult_language_ecosystem/adult_language_api_ecosystem.py",
    },
    "provider_modules": {
        "google": "google_language_api_ecosystem/google_language_api_ecosystem.py",
        "microsoft": "microsoft_language_api_ecosystem/microsoft_language_api_ecosystem.py",
        "amazon_aws": "aws_language_api_ecosystem/aws_language_api_ecosystem.py",
        "ibm": "ibm_language_api_ecosystem/ibm_language_api_ecosystem.py",
        "deepl": "deepl_language_api_ecosystem/deepl_language_api_ecosystem.py",
        "openai": "openai_language_api_ecosystem/openai_language_api_ecosystem.py",
        "meta": "meta_language_api_ecosystem/meta_language_api_ecosystem.py",
        "baidu": "baidu_language_api_ecosystem/baidu_language_api_ecosystem.py",
        "tencent": "tencent_language_api_ecosystem/tencent_language_api_ecosystem.py",
        "naver": "naver_language_api_ecosystem/naver_language_api_ecosystem.py",
        "yandex": "yandex_language_api_ecosystem/yandex_language_api_ecosystem.py",
        "alibaba": "alibaba_language_api_ecosystem/alibaba_language_api_ecosystem.py",
    },
}
