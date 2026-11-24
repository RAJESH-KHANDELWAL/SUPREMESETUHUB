<?php
declare(strict_types=1);
final class LeadsguruStorage {
 public const PLATFORM_ID='LEADSGURU';
 public function describe():array{return ['platform_id'=>self::PLATFORM_ID,'connection_state'=>'NOT_CONFIGURED','external_connections_verified'=>false,'storage_operations_enabled'=>false];}
}
