SUPREMESETUHUB — CENTRAL WORDPRESS CONNECTOR

Parent brand:
SUPREMESETUHUB
👑 DR RAJESH KHANDELWAL IBC 👑

Separate companion plugin brand names:
1. SUPREME by SUPREMESETUHUB
2. SUPREME ECOSYSTEM by SUPREMESETUHUB

Core files:
- supremesetuhub.php — Main WordPress plugin bootstrap.
- supremesetuhub.py — Python-side hub manifest.
- wordpress_connector.php — WordPress runtime connector.
- wordpress_connector.py — Python backend connector manifest.

WordPress executes PHP. Python files are intended for the Python backend and do
not run inside WordPress. The REST status route is:
  /wp-json/supremesetuhub/v1/connector-status

The connector checks active plugin entries using the expected plugin basenames.
Confirm those basenames match the actual installed companion plugin folder/file
names before relying on the active-state values. This is a status integration,
not a complete authenticated remote-control bridge.
