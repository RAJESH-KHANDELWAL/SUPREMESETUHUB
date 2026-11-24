"""Bharat-to-global application provider and platform catalog.
Entries are discovery metadata, not proof of API access, partnership, availability or live integration.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any
_ROWS = (
("google","Google","platform_vendor","global","consumer_enterprise","Android, Gmail, Maps, Drive, Photos, Workspace, Play Store"),
("apple","Apple","platform_vendor","global","operating_system_store","iOS, macOS, App Store, iCloud, Apple services"),
("microsoft","Microsoft","platform_vendor","global","operating_system_enterprise","Windows, Microsoft 365, Teams, Store, Xbox"),
("meta","Meta","platform_vendor","global","social_messaging","Facebook, Instagram, WhatsApp, Messenger, Threads"),
("amazon","Amazon","platform_vendor","global","commerce_cloud","Amazon Shopping, Kindle, Prime Video, Alexa"),
("adobe","Adobe","platform_vendor","global","creative_enterprise","Creative Cloud, Acrobat, Express, Lightroom"),
("samsung","Samsung","global_vendor","global","device_app_ecosystem","Galaxy Store, Samsung Health, SmartThings"),
("huawei","Huawei","regional_vendor","china","device_app_store","AppGallery, Petal Maps, Huawei Mobile Services"),
("alibaba","Alibaba","regional_vendor","china","commerce_enterprise","Taobao, Tmall, Alipay ecosystem"),
("tencent","Tencent","regional_vendor","china","social_entertainment","WeChat, QQ, Tencent Video"),
("bytedance","ByteDance","global_vendor","china","social_media_creation","TikTok, CapCut, Lemon8"),
("baidu","Baidu","regional_vendor","china","search_maps_ai_apps","Baidu App, Maps, Netdisk"),
("xiaomi","Xiaomi","global_vendor","china","device_app_ecosystem","GetApps, Mi Home, system apps"),
("huawei_appgallery","Huawei AppGallery","app_store","china","app_distribution","Android app distribution"),
("google_play","Google Play","app_store","global","app_distribution","Android app distribution and billing"),
("apple_app_store","Apple App Store","app_store","global","app_distribution","iOS and iPadOS app distribution"),
("microsoft_store","Microsoft Store","app_store","global","app_distribution","Windows apps and games"),
("f_droid","F-Droid","app_store","global","open_source_distribution","Free and open-source Android apps"),
("samsung_galaxy_store","Galaxy Store","app_store","global","device_app_distribution","Samsung device apps and games"),
("openai","OpenAI","app_provider","global","ai_productivity","ChatGPT app and developer tools"),
("notion","Notion","app_provider","global","productivity","Docs, wiki, projects, knowledge"),
("slack","Slack","app_provider","global","communication","Team messaging and workflows"),
("discord","Discord","app_provider","global","communication_community","Communities, voice and chat"),
("telegram","Telegram","app_provider","global","communication","Messaging, channels, bots"),
("signal","Signal","app_provider","global","communication_privacy","Private messaging and calls"),
("zoom","Zoom","app_provider","global","communication","Meetings, phone and collaboration"),
("salesforce","Salesforce","app_provider","global","enterprise_crm","CRM, Sales Cloud, Service Cloud"),
("shopify","Shopify","app_provider","global","commerce","Online stores and commerce tools"),
("stripe","Stripe","app_provider","global","payments","Payment and financial infrastructure apps"),
("paypal","PayPal","app_provider","global","payments","Wallet and merchant apps"),
("figma","Figma","app_provider","global","design_collaboration","Design, FigJam, Dev Mode"),
("canva","Canva","app_provider","global","design_content","Design, presentations, video, documents"),
("dropbox","Dropbox","app_provider","global","cloud_storage","File sync, sharing and backup"),
("box","Box","app_provider","global","enterprise_content","Content management and collaboration"),
("airtable","Airtable","app_provider","global","productivity_database","App building and work management"),
("asana","Asana","app_provider","global","project_management","Project and work management"),
("monday","monday.com","app_provider","global","work_management","Work OS and CRM"),
("trello","Trello","app_provider","global","project_management","Boards and task management"),
("atlassian","Atlassian","app_provider","global","developer_enterprise","Jira, Confluence, Bitbucket"),
("github","GitHub","app_provider","global","developer_platform","Code hosting, Actions, Codespaces"),
("gitlab","GitLab","app_provider","global","developer_platform","DevSecOps and source control"),
("linear","Linear","app_provider","global","developer_productivity","Issue and product management"),
("grammarly","Grammarly","app_provider","global","writing_productivity","Writing and communication assistance"),
("linkedin","LinkedIn","app_provider","global","professional_network","Professional networking and recruiting"),
("reddit","Reddit","app_provider","global","community","Communities and discussions"),
("pinterest","Pinterest","app_provider","global","discovery_content","Visual discovery and inspiration"),
("tiktok","TikTok","app_provider","global","social_media","Short-form video platform"),
("netflix","Netflix","app_provider","global","streaming","Video streaming"),
("spotify","Spotify","app_provider","global","streaming_audio","Music and podcasts"),
("wix","Wix","app_provider","global","website_builder","Website and business apps"),
("squarespace","Squarespace","app_provider","global","website_commerce","Websites and commerce"),
("wordpress","WordPress","app_platform","global","publishing_cms","Open-source CMS and publishing"),
("hubspot","HubSpot","app_provider","global","crm_marketing","CRM, marketing and service"),
("zendesk","Zendesk","app_provider","global","customer_support","Customer service and support"),
("miro","Miro","app_provider","global","collaboration","Visual collaboration"),
("zoho","Zoho","indian_global_vendor","india","business_saas","CRM, Books, Mail, Workplace, Creator"),
("phonepe","PhonePe","indian_app_provider","india","payments_finance","UPI, payments and financial services"),
("paytm","Paytm","indian_app_provider","india","payments_finance","Payments, wallet and merchant services"),
("bhim","BHIM","indian_public_app","india","upi_payments","UPI application"),
("npci","NPCI","indian_infrastructure","india","payment_network","UPI and retail payment ecosystem"),
("digilocker","DigiLocker","indian_public_app","india","digital_government","Digital documents and credentials"),
("umang","UMANG","indian_public_app","india","digital_government","Government service access"),
("aadhaar","Aadhaar","indian_identity_ecosystem","india","digital_identity","Identity ecosystem and related services"),
("irctc","IRCTC","indian_app_provider","india","travel_booking","Rail booking and travel services"),
("ola","Ola","indian_app_provider","india","mobility","Mobility and transport apps"),
("rapido","Rapido","indian_app_provider","india","mobility","Ride-hailing and mobility"),
("swiggy","Swiggy","indian_app_provider","india","food_delivery","Food and quick commerce"),
("zomato","Zomato","indian_app_provider","india","food_delivery","Food discovery and delivery"),
("flipkart","Flipkart","indian_app_provider","india","commerce","Ecommerce marketplace"),
("meesho","Meesho","indian_app_provider","india","commerce","Ecommerce and social commerce"),
("jio","Jio","indian_app_provider","india","telecom_entertainment","Jio apps and digital services"),
("tataneu","Tata Neu","indian_app_provider","india","commerce_lifestyle","Tata consumer services super-app"),
("ondc","ONDC","indian_digital_network","india","open_commerce","Open digital commerce network and buyer/seller apps"),
("bharatpe","BharatPe","indian_app_provider","india","merchant_finance","Merchant payments and financial services"),
("razorpay","Razorpay","indian_app_provider","india","payments_business","Business payments and commerce tools"),
("khatabook","Khatabook","indian_app_provider","india","business_finance","Digital ledger and MSME tools"),
("cred","CRED","indian_app_provider","india","finance_lifestyle","Credit-card and financial services app"),
("inshorts","Inshorts","indian_app_provider","india","news_media","News discovery"),
("sharechat","ShareChat","indian_app_provider","india","social_media","Indic-language social platform"),
("moj","Moj","indian_app_provider","india","social_media","Short-video platform"),
("josh","Josh","indian_app_provider","india","social_media","Short-video platform"),
("truecaller","Truecaller","global_app_provider","sweden","communication_identity","Caller identification and communication"),
("krutrim","Krutrim","indian_app_provider","india","ai_apps","Indian AI products and applications"),
("sarvam","Sarvam AI","indian_app_provider","india","ai_apps","Indic AI applications and services"),
("bharatgpt","BharatGPT","indian_app_provider","india","ai_apps","Indian AI application ecosystem"),
)
_APP_PROVIDER_CATALOG: tuple[dict[str, Any], ...] = tuple(
 {"id":r[0],"name":r[1],"category":r[2],"origin":r[3],"ecosystem_kind":r[4],
  "application_examples":r[5],"integration_status":"catalog_only","live_connection_verified":False}
 for r in _ROWS)
def list_app_providers(*,category:str|None=None,origin:str|None=None,ecosystem_kind:str|None=None)->tuple[dict[str,Any],...]:
 rows=_APP_PROVIDER_CATALOG
 if category is not None: rows=tuple(x for x in rows if x["category"]==category)
 if origin is not None: rows=tuple(x for x in rows if x["origin"]==origin)
 if ecosystem_kind is not None: rows=tuple(x for x in rows if x["ecosystem_kind"]==ecosystem_kind)
 return tuple(deepcopy(x) for x in rows)
def get_app_provider(provider_id:str)->dict[str,Any]|None:
 key=str(provider_id or "").strip().lower()
 for item in _APP_PROVIDER_CATALOG:
  if item["id"]==key:return deepcopy(item)
 return None
def validate_app_provider_registry()->tuple[str,...]:
 errors=[];seen=set()
 for index,item in enumerate(_APP_PROVIDER_CATALOG):
  key=item.get("id")
  if not isinstance(key,str) or not key.strip():errors.append(f"entry[{index}] has invalid id");continue
  if key in seen:errors.append(f"duplicate app provider id: {key}")
  seen.add(key)
  for field in ("name","category","origin","ecosystem_kind","application_examples"):
   if not item.get(field):errors.append(f"{key} is missing {field}")
  if item.get("integration_status") not in {"catalog_only","scaffold","integration_in_progress","configured","live_verified"}:errors.append(f"{key} has invalid integration_status")
  if item.get("integration_status")=="live_verified" and item.get("live_connection_verified") is not True:errors.append(f"{key} is marked live_verified without verification")
 return tuple(errors)
__all__=["list_app_providers","get_app_provider","validate_app_provider_registry"]
