<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';

/** Canonical GDE config alias; returns the central SUPREMESETUHUB DB. */
return supreme_main_database_connection_config();
