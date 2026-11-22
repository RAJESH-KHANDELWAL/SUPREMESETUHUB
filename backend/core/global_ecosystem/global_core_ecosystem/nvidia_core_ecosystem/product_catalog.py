from copy import deepcopy
PRODUCTS=[
  {
    "product_id": "NVIDIA-CUDA-CORE-ECOSYSTEM",
    "slug": "cuda",
    "name": "CUDA",
    "capabilities": [
      "GPU_COMPUTE",
      "CUDA_TOOLKIT"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/cuda_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/cuda_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/cuda_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-TENSORRT-CORE-ECOSYSTEM",
    "slug": "tensorrt",
    "name": "TensorRT",
    "capabilities": [
      "INFERENCE_OPTIMIZATION"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/tensorrt_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/tensorrt_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/tensorrt_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-TRITON-CORE-ECOSYSTEM",
    "slug": "triton",
    "name": "Triton Inference Server",
    "capabilities": [
      "MODEL_SERVING"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/triton_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/triton_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/triton_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-NIM-CORE-ECOSYSTEM",
    "slug": "nim",
    "name": "NVIDIA NIM",
    "capabilities": [
      "INFERENCE_MICROSERVICES"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/nim_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/nim_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/nim_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-NEMO-CORE-ECOSYSTEM",
    "slug": "nemo",
    "name": "NVIDIA NeMo",
    "capabilities": [
      "MODEL_DEVELOPMENT",
      "FINE_TUNING"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/nemo_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/nemo_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/nemo_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-DGX-CORE-ECOSYSTEM",
    "slug": "dgx",
    "name": "NVIDIA DGX",
    "capabilities": [
      "AI_SUPERCOMPUTING"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/dgx_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/dgx_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/dgx_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-RTX-CORE-ECOSYSTEM",
    "slug": "rtx",
    "name": "NVIDIA RTX",
    "capabilities": [
      "RAY_TRACING",
      "AI_GRAPHICS"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/rtx_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/rtx_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/rtx_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-GEFORCE-CORE-ECOSYSTEM",
    "slug": "geforce",
    "name": "NVIDIA GeForce",
    "capabilities": [
      "GAMING_GPU"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/geforce_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/geforce_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/geforce_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-JETSON-CORE-ECOSYSTEM",
    "slug": "jetson",
    "name": "NVIDIA Jetson",
    "capabilities": [
      "EDGE_AI",
      "ROBOTICS"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/jetson_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/jetson_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/jetson_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-OMNIVERSE-CORE-ECOSYSTEM",
    "slug": "omniverse",
    "name": "NVIDIA Omniverse",
    "capabilities": [
      "DIGITAL_TWINS",
      "SIMULATION"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/omniverse_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/omniverse_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/omniverse_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-ISAAC-CORE-ECOSYSTEM",
    "slug": "isaac",
    "name": "NVIDIA Isaac",
    "capabilities": [
      "ROBOTICS_SIMULATION"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/isaac_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/isaac_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/isaac_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-DRIVE-CORE-ECOSYSTEM",
    "slug": "drive",
    "name": "NVIDIA DRIVE",
    "capabilities": [
      "AUTOMOTIVE_AI"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/drive_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/drive_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/drive_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-NETWORKING-CORE-ECOSYSTEM",
    "slug": "networking",
    "name": "NVIDIA Networking",
    "capabilities": [
      "INFINIBAND",
      "ETHERNET"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/networking_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/networking_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/networking_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-METROPOLIS-CORE-ECOSYSTEM",
    "slug": "metropolis",
    "name": "NVIDIA Metropolis",
    "capabilities": [
      "VIDEO_ANALYTICS"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/metropolis_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/metropolis_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/metropolis_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-CLARA-CORE-ECOSYSTEM",
    "slug": "clara",
    "name": "NVIDIA Clara",
    "capabilities": [
      "HEALTHCARE_AI"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/clara_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/clara_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/clara_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-AI-ENTERPRISE-CORE-ECOSYSTEM",
    "slug": "ai_enterprise",
    "name": "NVIDIA AI Enterprise",
    "capabilities": [
      "ENTERPRISE_AI"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/ai_enterprise_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/ai_enterprise_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/ai_enterprise_engine_ecosystem"
  },
  {
    "product_id": "NVIDIA-HPC-CORE-ECOSYSTEM",
    "slug": "hpc",
    "name": "NVIDIA HPC",
    "capabilities": [
      "HPC",
      "SCIENTIFIC_COMPUTING"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/nvidia_api_ecosystem/hpc_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem/hpc_core_ecosystem",
    "engine_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/nvidia_engine_ecosystem/hpc_engine_ecosystem"
  }
]
def list_products():return deepcopy(PRODUCTS)
def get_product(key):
 x=str(key).casefold().strip();return next((deepcopy(p) for p in PRODUCTS if x in (p["slug"],p["product_id"].casefold(),p["name"].casefold())),None)
def summary():return {"product_count":len(PRODUCTS),"enabled_product_count":len(PRODUCTS),"connected_product_count":0}
