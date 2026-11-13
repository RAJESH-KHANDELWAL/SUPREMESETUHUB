SUPREMESETUHUB — CENTRAL WORDPRESS HUB

Parent brand:
SUPREMESETUHUB
👑 DR RAJESH KHANDELWAL IBC 👑

Separate companion plugin brands:
- SUPREME by SUPREMESETUHUB
- SUPREME ECOSYSTEM by SUPREMESETUHUB

Exact lowercase root filenames:
- supremesetuhub.php
- supremesetuhub.py
- supremesetuhub_wordpress_connector.php
- supremesetuhub_wordpress_connector.py

The main WordPress plugin bootstrap is supremesetuhub.php. It loads
supremesetuhub_wordpress_connector.php, which registers:
  /wp-json/supremesetuhub/v1/connector-status

The Python files are backend-side companion manifests. WordPress executes
PHP, not Python.

The connector's companion plugin basenames are configurable with WordPress
filters. Confirm the real folder/main-file paths of both separately installed
plugins before relying on their active status. The endpoint is a status
endpoint, not a complete authenticated remote-control integration.
