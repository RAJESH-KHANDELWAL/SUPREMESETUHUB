# CANONICAL BACKEND STRUCTURE

The seven ecosystem domain roots are DATABASE, CLOUD, STORAGE, SERVER, VPN, VPS, and SSH.

Each domain follows this hierarchy:

backend/<DOMAIN>/
  __init__.py
  service.py
  GLOBAL_ECOSYSTEM/
    __init__.py
    service.py
    GLOBAL_<DOMAIN>_ECOSYSTEM/
      __init__.py
      registry.py
      service.py
      README.md

GLOBAL_ECOSYSTEM is the shared ecosystem layer within each domain. GLOBAL_<DOMAIN>_ECOSYSTEM is the specific domain ecosystem layer. Provider-specific folders and files belong inside the matching ecosystem package.

Python is the authoritative backend runtime. PHP files belong only to components that genuinely execute in PHP, such as a WordPress plugin/bridge; they should not be copied into Python packages just to duplicate extensions. Never store credentials or private keys in source files. Registry metadata does not mean live connectivity is enabled.
