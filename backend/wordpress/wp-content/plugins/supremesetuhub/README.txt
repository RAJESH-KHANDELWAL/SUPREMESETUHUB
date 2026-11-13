SUPREMESETUHUB — CENTRAL WORDPRESS HUB

Parent brand:
SUPREMESETUHUB
👑 DR RAJESH KHANDELWAL IBC 👑

Companion plugin brands:
- SUPREME by SUPREMESETUHUB
- SUPREME ECOSYSTEM by SUPREMESETUHUB

Required root files:
- supremesetuhub.php
- supremesetuhub.py
- supreme_wordpress_connector.py
- supremesetuhub_wordpress_connector.php

The Python connector file is for the SUPREME backend companion. The PHP
connector file is loaded by the WordPress plugin bootstrap and registers:
  /wp-json/supremesetuhub/v1/connector-status

WordPress executes PHP, not Python. Python files are backend-side source.
The endpoint confirms that the connector route is registered; it does not
claim full authenticated integration with the separate plugins. Verify actual
plugin basenames and run end-to-end tests before production use.
