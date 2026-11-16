<?php
declare(strict_types=1);
require_once dirname(__DIR__, 2) . '/database.php';
/** Canonical GDE config alias; returns all five named database configurations. */
return supreme_main_foundation_config()['databases'];
