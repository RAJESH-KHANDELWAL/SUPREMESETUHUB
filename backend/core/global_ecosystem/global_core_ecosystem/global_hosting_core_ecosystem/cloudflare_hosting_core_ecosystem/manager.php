<?php
/** Provider metadata facade. */
final class HostingProviderManager {
 public const STATUS="CORE_CATALOG_ONLY";
 public static function status(string $providerId):array{return ["success"=>true,"provider_id"=>strtoupper($providerId),"status"=>self::STATUS,"live_connection_verified"=>false,"api_transport_in_core"=>false,"persistence_enabled"=>false];}
}
