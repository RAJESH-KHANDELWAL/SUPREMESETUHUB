from copy import deepcopy
DOMAINS=[
  {
    "domain_id": "NVIDIA-DOMAIN-01",
    "name": "GOVERNANCE",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-02",
    "name": "GPU_COMPUTE",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-03",
    "name": "AI_DEVELOPMENT",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-04",
    "name": "INFERENCE",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-05",
    "name": "TRAINING",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-06",
    "name": "ENTERPRISE_AI",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-07",
    "name": "DATACENTER",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-08",
    "name": "GPU_CLUSTER",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-09",
    "name": "NETWORKING",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-10",
    "name": "GRAPHICS",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-11",
    "name": "GAMING",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-12",
    "name": "EDGE_AI",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-13",
    "name": "ROBOTICS",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-14",
    "name": "DIGITAL_TWINS",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-15",
    "name": "AUTOMOTIVE",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-16",
    "name": "VIDEO_ANALYTICS",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-17",
    "name": "HEALTHCARE",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-18",
    "name": "HPC",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-19",
    "name": "DEVELOPER_CLOUD",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-20",
    "name": "SECURITY",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-21",
    "name": "LICENSING_TENANCY",
    "status": "TAXONOMY_ONLY"
  },
  {
    "domain_id": "NVIDIA-DOMAIN-22",
    "name": "SUPPORT",
    "status": "TAXONOMY_ONLY"
  }
]
def list_domains():return deepcopy(DOMAINS)
