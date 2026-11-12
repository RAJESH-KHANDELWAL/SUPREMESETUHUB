<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/config.php';

/** Global Ecosystem is a logical parent; its DB connection is owned by GDE. */
return [
    'layer' => 'GLOBAL_ECOSYSTEM',
    'connection_mode' => 'delegate',
    'connection_owner' => 'GLOBAL_DATABASE_ECOSYSTEM',
];
