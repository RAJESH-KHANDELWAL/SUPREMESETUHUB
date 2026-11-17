# DeepSeek CORE Package Standard

Every capability package contains exactly ten subfolders: authentication/, capabilities/, docs/, events/, lifecycle/, models/, schemas/, security/, services/ and tests/. It also owns README.md, __init__.py, contracts.py, service.py, ecosystem_config.py and ecosystem_manifest.json. Caller-context PHP contracts belong in authentication/contract.php. Duplicate php/ trees are prohibited.

API transport, ENGINE execution, DATABASE persistence and STORAGE artifacts remain in their respective layers.
