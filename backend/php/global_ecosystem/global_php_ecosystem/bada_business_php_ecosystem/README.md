# BADA BUSINESS PHP ECOSYSTEM

This module is a PHP-side, read-only adapter for Bada Business catalog
resources. It belongs to:

`backend/php/global_ecosystem/global_php_ecosystem/`

## Bootstrap

```php
require_once __DIR__ . '/bootstrap.php';

$adapter = new \\SupremeSetuHub\\GlobalEcosystem\\PHP\\BadaBusiness\\BadaBusinessPHPAdapter($catalogLinks);
$catalog = $adapter->catalog();
$matches = $adapter->search('digital');
```

Pass catalog records from the canonical backend catalog; this adapter does not
duplicate referral URLs. It does not claim a live Bada Business connection and
does not perform login, account, payment, enrollment, lead, or transaction
actions. Authentication and official API access remain unconfigured until
verified separately.

The adapter reports `connected: false` by design.
