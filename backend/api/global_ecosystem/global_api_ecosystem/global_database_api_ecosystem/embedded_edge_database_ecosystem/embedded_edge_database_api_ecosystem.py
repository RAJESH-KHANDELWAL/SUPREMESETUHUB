"""Catalog-only global database category module; not a live connector."""

EMBEDDED_MOBILE_AND_EDGE_DATABASES = {
    "category": "EMBEDDED_MOBILE_AND_EDGE_DATABASES",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "SQLite",
        "DuckDB",
        "Realm",
        "ObjectBox",
        "Couchbase Lite",
        "PouchDB",
        "RxDB",
        "WatermelonDB",
        "Isar",
        "Hive",
        "Core Data",
        "CloudKit",
        "IndexedDB",
        "LevelDB",
        "RocksDB",
        "LMDB",
        "libSQL",
        "Turso"
    ],
}
