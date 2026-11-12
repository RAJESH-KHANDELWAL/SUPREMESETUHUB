<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/config.php';
require_once dirname(__DIR__, 2) . '/database.php';

/** Load the dedicated GDE database configuration; no WordPress fallback. */
return supreme_database_config('GDE_DB_');
