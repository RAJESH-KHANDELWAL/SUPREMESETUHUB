<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_FLIGHTS_STORAGE_ECOSYSTEM. */
final class GlobalAppFlightsStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_FLIGHTS_STORAGE_ECOSYSTEM';
 public const CATEGORY='FLIGHTS';
 public const CATEGORY_GROUP='MAPS_LOCATION_AND_TRAVEL';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
