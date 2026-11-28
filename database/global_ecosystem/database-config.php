<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/config.php';
/** Return all five database configurations; no credentials are synthesized. */
return supreme_main_foundation_config()['databases'];
