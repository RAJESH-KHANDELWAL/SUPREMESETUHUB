<?php
declare(strict_types=1);
function hosting_provider_status():array{$folder=basename(__DIR__);$folder=preg_replace('/_hosting_core_ecosystem$/','',$folder);$folder=preg_replace('/^global_/','',$folder);return ['provider_id'=>strtoupper($folder),'status'=>'CORE_CATALOG_ONLY','live_connection_verified'=>false,'api_transport_in_core'=>false,'persistence_enabled'=>false];}
