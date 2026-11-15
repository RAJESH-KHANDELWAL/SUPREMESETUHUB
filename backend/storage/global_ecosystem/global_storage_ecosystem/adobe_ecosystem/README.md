# Adobe Ecosystem

Canonical Adobe provider namespace for SUPREMESETUHUB.

```text
adobe_ecosystem/
└── what_adobe_provides/
    ├── products_and_services/
    └── storage_ecosystem/
        ├── README.md
        ├── catalog.py
        ├── manifest.json
        └── nine product-specific storage packages/
```

Product catalogue entries are descriptive metadata, not claims of API access or storage capability. Storage adapters must use the matching documented Adobe API and entitlement. No generic file CRUD is inferred from a product name. A connector is CONNECTED only after an authenticated provider operation succeeds. Credentials belong in the deployment secret manager, never in Git.

The earlier adobe_storage_ecosystem path is retained temporarily for compatibility. The canonical hierarchy is this Adobe / What Adobe Provides / Storage Ecosystem path.
