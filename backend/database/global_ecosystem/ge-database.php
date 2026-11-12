<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/database.php';
require_once __DIR__ . '/ge-database-config.php';

/** Global Ecosystem delegates the physical connection to its GDE child. */
if (!function_exists('ge_database_connection')) {
    function ge_database_connection(): PDO
    {
        static $connection = null;
        if ($connection instanceof PDO) {
            return $connection;
        }
        $connection = supreme_database_connect(ge_database_config());
        return $connection;
    }
}
