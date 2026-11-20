# Hosting Provider Core Package

This package identifies one hosting-related provider/platform in the global catalog. It exposes read-only metadata only. It does not connect to provider APIs, provision infrastructure, change DNS, deploy workloads, process billing or store credentials.

The canonical classification and provider record live in the parent `catalog.py` and `hosting_categories.py`.
