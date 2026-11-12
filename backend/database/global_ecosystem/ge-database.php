<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/database.php';

/** Legacy GE connection name; no separate GDE database is opened. */
if (!function_exists('ge_database_connection')) {
    function ge_database_connection(): PDO
    {
        return supreme_main_database_connection();
    }
}
