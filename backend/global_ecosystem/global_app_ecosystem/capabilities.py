"""Application form-factor, delivery and capability taxonomy."""
from __future__ import annotations
from typing import Any
APP_TYPES: tuple[dict[str, Any], ...] = (
 {"id":"native_mobile","name":"Native mobile app","platforms":["android","ios"]},
 {"id":"cross_platform_mobile","name":"Cross-platform mobile app","platforms":["android","ios"]},
 {"id":"web_app","name":"Web application","platforms":["browser"]},
 {"id":"progressive_web_app","name":"Progressive web app","platforms":["browser","installable_web"]},
 {"id":"desktop_app","name":"Desktop application","platforms":["windows","macos","linux"]},
 {"id":"system_app","name":"System and utility app","platforms":["operating_system"]},
 {"id":"enterprise_app","name":"Enterprise application","platforms":["web","mobile","desktop"]},
 {"id":"saas_app","name":"Software as a service","platforms":["cloud","browser","mobile"]},
 {"id":"browser_extension","name":"Browser extension","platforms":["chrome","edge","firefox","safari"]},
 {"id":"wearable_app","name":"Wearable application","platforms":["watch","wearable"]},
 {"id":"tv_app","name":"Television and streaming-device app","platforms":["android_tv","tvos","smart_tv"]},
 {"id":"embedded_iot_app","name":"Embedded and IoT application","platforms":["embedded","iot","edge"]},
 {"id":"game_app","name":"Game application","platforms":["mobile","desktop","console","web"]},
 {"id":"app_store","name":"Application distribution store","platforms":["android","ios","desktop","enterprise"]},
 {"id":"developer_platform","name":"Application development platform","platforms":["cloud","local","browser"]},
)
APP_CAPABILITY_GROUPS: tuple[dict[str, Any], ...] = (
 {"id":"identity_accounts","name":"Identity, profiles and account management","capabilities":["registration","profile_management","account_recovery","preferences"]},
 {"id":"communication","name":"Communication and collaboration","capabilities":["messaging","email","voice","video","presence","notifications"]},
 {"id":"content_media","name":"Content and media","capabilities":["capture","editing","publishing","streaming","moderation"]},
 {"id":"commerce_payments","name":"Commerce and payments","capabilities":["catalog","cart","checkout","orders","payments","subscriptions"]},
 {"id":"productivity_workflow","name":"Productivity and workflow","capabilities":["documents","tasks","calendar","automation","approvals"]},
 {"id":"data_storage","name":"Data, files and storage","capabilities":["upload","sync","backup","search","sharing","export"]},
 {"id":"location_mobility","name":"Location and mobility","capabilities":["maps","navigation","booking","tracking","dispatch"]},
 {"id":"developer_delivery","name":"Development and delivery","capabilities":["build","test","release","monitor","debug","deploy"]},
 {"id":"security_privacy","name":"Security and privacy","capabilities":["encryption","consent","permissions","audit","threat_detection"]},
 {"id":"accessibility_localization","name":"Accessibility and localization","capabilities":["screen_reader","captions","translation","indic_language_support","regionalization"]},
 {"id":"analytics_personalization","name":"Analytics and personalization","capabilities":["analytics","recommendations","experimentation","personalization"]},
 {"id":"app_lifecycle","name":"Application lifecycle management","capabilities":["install","update","configure","launch","suspend","uninstall"]},
)
def list_app_types() -> tuple[dict[str, Any],...]: return tuple({**x,"platforms":list(x["platforms"])} for x in APP_TYPES)
def list_app_capability_groups() -> tuple[dict[str, Any],...]: return tuple({**x,"capabilities":list(x["capabilities"])} for x in APP_CAPABILITY_GROUPS)
__all__=["APP_TYPES","APP_CAPABILITY_GROUPS","list_app_types","list_app_capability_groups"]
