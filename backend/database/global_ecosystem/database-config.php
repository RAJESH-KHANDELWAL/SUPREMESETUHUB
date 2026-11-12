<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/database.php';

/** Global Ecosystem resolves to the one central SUPREMESETUHUB DB config. */
return supreme_main_database_connection_config();
