"""Language registry and opt-in translation API for SUPREMESETUHUB.

Human languages and programming languages are intentionally separate catalogues.
Translation requires an explicitly configured provider; this module never assumes
that a translation engine or speech provider is already deployed.
"""
from __future__ import annotations

import os
from typing import Literal

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/languages", tags=["Languages and translation"])

HUMAN_LANGUAGES = [
    {"code":"en","name":"English","native_name":"English","region":"Global"},
    {"code":"hi","name":"Hindi","native_name":"हिन्दी","region":"India"},
    {"code":"gu","name":"Gujarati","native_name":"ગુજરાતી","region":"India"},
    {"code":"bn","name":"Bengali","native_name":"বাংলা","region":"India/Bangladesh"},
    {"code":"ta","name":"Tamil","native_name":"தமிழ்","region":"India/Sri Lanka"},
    {"code":"te","name":"Telugu","native_name":"తెలుగు","region":"India"},
    {"code":"mr","name":"Marathi","native_name":"मराठी","region":"India"},
    {"code":"pa","name":"Punjabi","native_name":"ਪੰਜਾਬੀ","region":"India"},
    {"code":"ur","name":"Urdu","native_name":"اردو","region":"South Asia"},
    {"code":"kn","name":"Kannada","native_name":"ಕನ್ನಡ","region":"India"},
    {"code":"ml","name":"Malayalam","native_name":"മലയാളം","region":"India"},
    {"code":"or","name":"Odia","native_name":"ଓଡ଼ିଆ","region":"India"},
    {"code":"as","name":"Assamese","native_name":"অসমীয়া","region":"India"},
    {"code":"ne","name":"Nepali","native_name":"नेपाली","region":"Nepal"},
    {"code":"sa","name":"Sanskrit","native_name":"संस्कृतम्","region":"India"},
    {"code":"kok","name":"Konkani","native_name":"कोंकणी","region":"India"},
    {"code":"sd","name":"Sindhi","native_name":"سنڌي","region":"South Asia"},
    {"code":"ks","name":"Kashmiri","native_name":"कॉशुर","region":"India"},
    {"code":"doi","name":"Dogri","native_name":"डोगरी","region":"India"},
    {"code":"mai","name":"Maithili","native_name":"मैथिली","region":"India/Nepal"},
    {"code":"mni","name":"Manipuri","native_name":"মৈতৈলোন্","region":"India"},
    {"code":"sat","name":"Santali","native_name":"ᱥᱟᱱᱛᱟᱲᱤ","region":"India"},
    {"code":"brx","name":"Bodo","native_name":"बड़ो","region":"India"},
    {"code":"en-US","name":"English (United States)","native_name":"English (US)","region":"United States"},
    {"code":"en-GB","name":"English (United Kingdom)","native_name":"English (UK)","region":"United Kingdom"},
    {"code":"ar","name":"Arabic","native_name":"العربية","region":"Middle East/North Africa"},
    {"code":"fa","name":"Persian","native_name":"فارسی","region":"Iran"},
    {"code":"he","name":"Hebrew","native_name":"עברית","region":"Israel"},
    {"code":"fr","name":"French","native_name":"Français","region":"France/Global"},
    {"code":"de","name":"German","native_name":"Deutsch","region":"Germany/Austria"},
    {"code":"es","name":"Spanish","native_name":"Español","region":"Spain/Latin America"},
    {"code":"pt","name":"Portuguese","native_name":"Português","region":"Portugal/Brazil"},
    {"code":"it","name":"Italian","native_name":"Italiano","region":"Italy"},
    {"code":"nl","name":"Dutch","native_name":"Nederlands","region":"Netherlands/Belgium"},
    {"code":"ru","name":"Russian","native_name":"Русский","region":"Russia"},
    {"code":"uk","name":"Ukrainian","native_name":"Українська","region":"Ukraine"},
    {"code":"pl","name":"Polish","native_name":"Polski","region":"Poland"},
    {"code":"tr","name":"Turkish","native_name":"Türkçe","region":"Türkiye"},
    {"code":"el","name":"Greek","native_name":"Ελληνικά","region":"Greece/Cyprus"},
    {"code":"sv","name":"Swedish","native_name":"Svenska","region":"Sweden"},
    {"code":"da","name":"Danish","native_name":"Dansk","region":"Denmark"},
    {"code":"no","name":"Norwegian","native_name":"Norsk","region":"Norway"},
    {"code":"fi","name":"Finnish","native_name":"Suomi","region":"Finland"},
    {"code":"is","name":"Icelandic","native_name":"Íslenska","region":"Iceland"},
    {"code":"zh","name":"Chinese (Simplified)","native_name":"简体中文","region":"China"},
    {"code":"zh-TW","name":"Chinese (Traditional)","native_name":"繁體中文","region":"Taiwan"},
    {"code":"ja","name":"Japanese","native_name":"日本語","region":"Japan"},
    {"code":"ko","name":"Korean","native_name":"한국어","region":"South Korea"},
    {"code":"th","name":"Thai","native_name":"ไทย","region":"Thailand"},
    {"code":"vi","name":"Vietnamese","native_name":"Tiếng Việt","region":"Vietnam"},
    {"code":"id","name":"Indonesian","native_name":"Bahasa Indonesia","region":"Indonesia"},
    {"code":"ms","name":"Malay","native_name":"Bahasa Melayu","region":"Malaysia"},
    {"code":"fil","name":"Filipino","native_name":"Filipino","region":"Philippines"},
    {"code":"sw","name":"Swahili","native_name":"Kiswahili","region":"East Africa"},
    {"code":"am","name":"Amharic","native_name":"አማርኛ","region":"Ethiopia"},
    {"code":"ha","name":"Hausa","native_name":"Hausa","region":"West Africa"},
    {"code":"yo","name":"Yoruba","native_name":"Yorùbá","region":"West Africa"},
    {"code":"zu","name":"Zulu","native_name":"isiZulu","region":"Southern Africa"},
    {"code":"af","name":"Afrikaans","native_name":"Afrikaans","region":"Southern Africa"},
    {"code":"ps","name":"Pashto","native_name":"پښتو","region":"Afghanistan/Pakistan"},
    {"code":"ku","name":"Kurdish","native_name":"Kurdî","region":"Middle East"},
    {"code":"az","name":"Azerbaijani","native_name":"Azərbaycanca","region":"Azerbaijan"},
    {"code":"kk","name":"Kazakh","native_name":"Қазақша","region":"Kazakhstan"},
    {"code":"uz","name":"Uzbek","native_name":"Oʻzbekcha","region":"Uzbekistan"},
    {"code":"mn","name":"Mongolian","native_name":"Монгол","region":"Mongolia"},
    {"code":"my","name":"Burmese","native_name":"မြန်မာ","region":"Myanmar"},
    {"code":"km","name":"Khmer","native_name":"ខ្មែរ","region":"Cambodia"},
    {"code":"lo","name":"Lao","native_name":"ລາວ","region":"Laos"},
    {"code":"si","name":"Sinhala","native_name":"සිංහල","region":"Sri Lanka"},
    {"code":"ga","name":"Irish","native_name":"Gaeilge","region":"Ireland"},
    {"code":"cy","name":"Welsh","native_name":"Cymraeg","region":"Wales"},
    {"code":"eo","name":"Esperanto","native_name":"Esperanto","region":"International"},
]

PROGRAMMING_LANGUAGES = [
    {"name":"Python","type":"general-purpose"},{"name":"JavaScript","type":"web"},{"name":"TypeScript","type":"web"},
    {"name":"Java","type":"general-purpose"},{"name":"C","type":"systems"},{"name":"C++","type":"systems"},
    {"name":"C#","type":"general-purpose"},{"name":"Go","type":"systems"},{"name":"Rust","type":"systems"},
    {"name":"Kotlin","type":"mobile"},{"name":"Swift","type":"mobile"},{"name":"Dart","type":"mobile/web"},
    {"name":"PHP","type":"web"},{"name":"Ruby","type":"web"},{"name":"R","type":"data/science"},
    {"name":"SQL","type":"database"},{"name":"HTML","type":"markup"},{"name":"CSS","type":"stylesheet"},
    {"name":"Bash","type":"shell"},{"name":"PowerShell","type":"shell"},{"name":"Perl","type":"scripting"},
    {"name":"Lua","type":"scripting/embedded"},{"name":"Scala","type":"general-purpose"},{"name":"Groovy","type":"JVM"},
    {"name":"Objective-C","type":"Apple platforms"},{"name":"Elixir","type":"functional"},{"name":"Erlang","type":"functional"},
    {"name":"Haskell","type":"functional"},{"name":"Clojure","type":"functional"},{"name":"F#","type":"functional"},
    {"name":"OCaml","type":"functional"},{"name":"Julia","type":"scientific computing"},{"name":"MATLAB","type":"scientific computing"},
    {"name":"Fortran","type":"scientific computing"},{"name":"COBOL","type":"business systems"},{"name":"Assembly","type":"low-level"},
    {"name":"Solidity","type":"smart contracts"},{"name":"Vyper","type":"smart contracts"},{"name":"Verilog","type":"hardware"},
    {"name":"VHDL","type":"hardware"},{"name":"SystemVerilog","type":"hardware"},{"name":"Zig","type":"systems"},
    {"name":"Nim","type":"systems"},{"name":"Crystal","type":"general-purpose"},{"name":"D","type":"systems"},
    {"name":"Ada","type":"safety-critical"},{"name":"Prolog","type":"logic"},{"name":"Lisp","type":"functional"},
    {"name":"Scheme","type":"functional"},{"name":"Racket","type":"functional"},{"name":"Smalltalk","type":"object-oriented"},
    {"name":"Scratch","type":"visual/education"},{"name":"ABAP","type":"enterprise"},{"name":"Apex","type":"enterprise"},
    {"name":"PL/SQL","type":"database"},{"name":"T-SQL","type":"database"},{"name":"GDScript","type":"game development"},
    {"name":"Haxe","type":"cross-platform"},{"name":"ActionScript","type":"legacy web"},{"name":"QML","type":"UI"},
]

SUPPORTED_CODES = {item["code"] for item in HUMAN_LANGUAGES}
BASE_CODES = {code.split("-")[0] for code in SUPPORTED_CODES}

class TranslateBatchRequest(BaseModel):
    texts: list[str] = Field(min_length=1, max_length=40)
    source: str = Field(default="auto", max_length=16)
    target: str = Field(min_length=2, max_length=16)

class TranslateRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    source: str = Field(default="auto", max_length=16)
    target: str = Field(min_length=2, max_length=16)

@router.get("/catalog")
def language_catalog():
    return {
        "success": True,
        "human_languages": HUMAN_LANGUAGES,
        "human_language_count": len(HUMAN_LANGUAGES),
        "programming_languages": PROGRAMMING_LANGUAGES,
        "programming_language_count": len(PROGRAMMING_LANGUAGES),
        "translation_provider_configured": bool(os.getenv("SUPREME_TRANSLATION_API_URL")),
        "speech_translation_note": "Browser speech support varies; real-time translated audio/video requires separate speech recognition, translation and speech synthesis providers.",
    }

@router.post("/translate/batch")
async def translate_batch(request: TranslateBatchRequest):
    """Translate a bounded batch of interface strings with one provider request."""
    if any(not item.strip() or len(item) > 1500 for item in request.texts):
        raise HTTPException(status_code=422, detail="INVALID_BATCH_TEXT")
    if request.target not in SUPPORTED_CODES and request.target not in BASE_CODES:
        raise HTTPException(status_code=422, detail="UNSUPPORTED_TARGET_LANGUAGE")
    if request.source != "auto" and request.source not in SUPPORTED_CODES and request.source not in BASE_CODES:
        raise HTTPException(status_code=422, detail="UNSUPPORTED_SOURCE_LANGUAGE")
    endpoint = os.getenv("SUPREME_TRANSLATION_API_URL", "").strip()
    if not endpoint:
        raise HTTPException(status_code=503, detail="TRANSLATION_PROVIDER_NOT_CONFIGURED")
    if not endpoint.startswith("https://") and not (
        os.getenv("SUPREME_ALLOW_LOCAL_TRANSLATION_HTTP") == "1"
        and endpoint.startswith("http://127.0.0.1")
    ):
        raise HTTPException(status_code=503, detail="TRANSLATION_PROVIDER_MUST_USE_HTTPS")
    payload = {"q": request.texts, "source": request.source, "target": request.target, "format": "text"}
    api_key = os.getenv("SUPREME_TRANSLATION_API_KEY")
    if api_key:
        payload["api_key"] = api_key
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(18.0, connect=4.0)) as client:
            response = await client.post(endpoint.rstrip("/") + "/translate", json=payload)
            response.raise_for_status()
            data = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(status_code=502, detail="TRANSLATION_PROVIDER_REQUEST_FAILED") from exc
    translated = data.get("translatedText")
    if isinstance(translated, str):
        translated = [translated]
    if not isinstance(translated, list) or len(translated) != len(request.texts) or not all(isinstance(item, str) for item in translated):
        raise HTTPException(status_code=502, detail="TRANSLATION_PROVIDER_INVALID_BATCH_RESPONSE")
    return {"success": True, "source": request.source, "target": request.target, "translated_texts": translated, "provider": "configured_external_translation_service"}

@router.post("/translate")
async def translate(request: TranslateRequest):
    source = request.source
    target = request.target
    if target not in SUPPORTED_CODES and target not in BASE_CODES:
        raise HTTPException(status_code=422, detail="UNSUPPORTED_TARGET_LANGUAGE")
    if source != "auto" and source not in SUPPORTED_CODES and source not in BASE_CODES:
        raise HTTPException(status_code=422, detail="UNSUPPORTED_SOURCE_LANGUAGE")
    endpoint = os.getenv("SUPREME_TRANSLATION_API_URL", "").strip()
    if not endpoint:
        raise HTTPException(
            status_code=503,
            detail={
                "code": "TRANSLATION_PROVIDER_NOT_CONFIGURED",
                "message": "Configure SUPREME_TRANSLATION_API_URL with a trusted translation provider before live translation can run.",
            },
        )
    if not endpoint.startswith("https://") and not (
        os.getenv("SUPREME_ALLOW_LOCAL_TRANSLATION_HTTP") == "1"
        and endpoint.startswith("http://127.0.0.1")
    ):
        raise HTTPException(status_code=503, detail="TRANSLATION_PROVIDER_MUST_USE_HTTPS")
    payload = {"q": request.text, "source": source, "target": target, "format": "text"}
    api_key = os.getenv("SUPREME_TRANSLATION_API_KEY")
    if api_key:
        payload["api_key"] = api_key
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(12.0, connect=4.0)) as client:
            response = await client.post(endpoint.rstrip("/") + "/translate", json=payload)
            response.raise_for_status()
            data = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(status_code=502, detail="TRANSLATION_PROVIDER_REQUEST_FAILED") from exc
    translated = data.get("translatedText")
    if not isinstance(translated, str) or not translated.strip():
        raise HTTPException(status_code=502, detail="TRANSLATION_PROVIDER_INVALID_RESPONSE")
    return {
        "success": True,
        "source": data.get("detectedLanguage", {}).get("language", source) if isinstance(data.get("detectedLanguage"), dict) else source,
        "target": target,
        "translated_text": translated,
        "provider": "configured_external_translation_service",
        "review_note": "Machine translation can be inaccurate; verify critical, legal, medical and financial content.",
    }
