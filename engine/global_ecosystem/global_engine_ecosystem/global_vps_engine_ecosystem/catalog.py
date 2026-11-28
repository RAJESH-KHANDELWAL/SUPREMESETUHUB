"""Independent ENGINE catalog for GLOBAL VPS."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL VPS"
CHILD_ECOSYSTEMS = [
    "ALIBABA CLOUD VPS",
    "AWS VPS",
    "BAIDU CLOUD VPS",
    "CHINA TELECOM CLOUD VPS",
    "CLOUDFLARE VPS",
    "DIGITALOCEAN VPS",
    "GOOGLE VPS",
    "HETZNER CLOUD VPS",
    "HUAWEI CLOUD VPS",
    "IBM VPS",
    "JD CLOUD VPS",
    "KINGSOFT CLOUD VPS",
    "MICROSOFT VPS",
    "NVIDIA VPS",
    "ORACLE VPS",
    "OVHCLOUD VPS",
    "RACKSPACE VPS",
    "SCALEWAY VPS",
    "TENCENT CLOUD VPS",
    "VULTR VPS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_VPS", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
