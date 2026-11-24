<?php
declare(strict_types=1);
function hosting_domain_status():array{$name=basename(__DIR__);$name=preg_replace('/_hosting_core_ecosystem$/','',$name);$name=preg_replace('/^global_/','',$name);return ['domain_id'=>strtoupper($name),'status'=>'CORE_CATALOG_ONLY','live_connection_verified'=>false,'api_transport_in_core'=>false];}
