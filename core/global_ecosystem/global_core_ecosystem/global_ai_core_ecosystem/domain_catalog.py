"""AI domain taxonomy and provider coverage."""
from .catalog import list_ai_providers
AI_DOMAIN_DEFINITIONS={
"BHARAT_INDIC_AND_REGIONAL_AI":"Indic languages, Bharat-first datasets and regional AI.",
"GLOBAL_FOUNDATION_MODELS":"Global hosted foundation-model providers.",
"OPEN_MODEL_FAMILIES":"Open-weight model families and distributions.",
"AGENT_FRAMEWORKS_AND_ORCHESTRATION":"Agent frameworks, graph orchestration and tool routing.",
"ENTERPRISE_AND_BUSINESS_AI":"Enterprise, cloud, data and business AI platforms.",
"INFERENCE_AND_AI_INFRASTRUCTURE":"Model serving, acceleration, routing and inference infrastructure.",
"GENERATIVE_MEDIA_AND_CREATIVE_AI":"Image, video, audio, music and creative generation.",
"SPEECH_AUDIO_AND_LANGUAGE_AI":"Speech recognition, synthesis, translation and language systems.",
"VIDEO_AND_MEDIA_GENERATION":"Video synthesis, editing and media workflows.",
"SEARCH_KNOWLEDGE_AND_RETRIEVAL":"Search, research, RAG and knowledge discovery.",
"DEVELOPER_AND_CODE_AI":"Code generation and software engineering.",
"SAFETY_GOVERNANCE_AND_EVALUATION":"Moderation, evaluation, observability and governance.",
"AI_RESEARCH_AND_EVALUATION":"Research, benchmarks and scientific work.",
"ON_DEVICE_AND_EDGE_AI":"Local inference, mobile intelligence and edge AI.",
"MULTIMODAL_AND_SPATIAL_AI":"Cross-modal perception, spatial and embodied AI.",
"HEALTHCARE_AND_LIFE_SCIENCES_AI":"Policy-gated healthcare and scientific applications.",
"FINANCE_AND_RISK_AI":"Policy-gated finance, risk and fraud workflows.",
"EDUCATION_AND_LEARNING_AI":"Tutoring, learning and education workflows.",
"SPECIALTY_CROSS_PRODUCT_AI":"Specialty or not-yet-classified provider categories."}
_CATEGORY={"ai_provider":"GLOBAL_FOUNDATION_MODELS","agent_framework":"AGENT_FRAMEWORKS_AND_ORCHESTRATION","model_family":"OPEN_MODEL_FAMILIES","open_model_family":"OPEN_MODEL_FAMILIES","bharat_ai_research_ecosystem":"BHARAT_INDIC_AND_REGIONAL_AI","enterprise_ai_platform":"ENTERPRISE_AND_BUSINESS_AI","ai_infrastructure":"INFERENCE_AND_AI_INFRASTRUCTURE","creative_ai":"GENERATIVE_MEDIA_AND_CREATIVE_AI","speech_ai":"SPEECH_AUDIO_AND_LANGUAGE_AI","video_ai":"VIDEO_AND_MEDIA_GENERATION","research_ecosystem":"AI_RESEARCH_AND_EVALUATION"}
def domain_for_provider(x):
 c=x.get("category",""); pid=x.get("id","")
 if c in _CATEGORY:return _CATEGORY[c]
 s=(c+" "+pid).casefold()
 rules=[(("speech","audio","voice","translation"),"SPEECH_AUDIO_AND_LANGUAGE_AI"),(("video","runway","hunyuan"),"VIDEO_AND_MEDIA_GENERATION"),(("image","creative","firefly","flux","diffusion","suno"),"GENERATIVE_MEDIA_AND_CREATIVE_AI"),(("search","perplexity","retrieval","llamaindex","haystack"),"SEARCH_KNOWLEDGE_AND_RETRIEVAL"),(("ollama","vllm","groq","cerebras","fireworks","together","openrouter","replicate","litellm"),"INFERENCE_AND_AI_INFRASTRUCTURE"),(("copilot","databricks","salesforce","snowflake","watsonx","bedrock","azure","joule","oracle"),"ENTERPRISE_AND_BUSINESS_AI"),(("autogen","crewai","langchain","langgraph","semantic_kernel","dspy"),"AGENT_FRAMEWORKS_AND_ORCHESTRATION"),(("bharat","indic","sarvam","krutrim","hanooman","gnani","corover"),"BHARAT_INDIC_AND_REGIONAL_AI"),(("apple_intelligence",),"ON_DEVICE_AND_EDGE_AI")]
 for needles,domain in rules:
  if any(n in s for n in needles):return domain
 return "SPECIALTY_CROSS_PRODUCT_AI"
def list_ai_domain_inventory():
 grouped={k:[] for k in AI_DOMAIN_DEFINITIONS}
 for p in list_ai_providers():grouped[domain_for_provider(p)].append(p)
 return [{"id":k,"name":v,"provider_count":len(grouped[k]),"providers":[{"id":p["id"],"name":p["name"],"category":p["category"]} for p in grouped[k]]} for k,v in AI_DOMAIN_DEFINITIONS.items()]
def ai_domain_summary():
 inv=list_ai_domain_inventory()
 return {"success":True,"domain_count":len(inv),"active_domain_count":sum(x["provider_count"]>0 for x in inv),"provider_count":sum(x["provider_count"] for x in inv),"unclassified_provider_count":next(x["provider_count"] for x in inv if x["id"]=="SPECIALTY_CROSS_PRODUCT_AI"),"domains":inv}
