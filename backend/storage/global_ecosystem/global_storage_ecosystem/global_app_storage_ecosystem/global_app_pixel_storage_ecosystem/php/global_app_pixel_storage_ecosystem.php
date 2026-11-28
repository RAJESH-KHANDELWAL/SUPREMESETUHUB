<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_PIXEL_STORAGE_ECOSYSTEM. */
final class GlobalAppPixelStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_PIXEL_STORAGE_ECOSYSTEM';
 public const CATEGORY='PIXEL';
 public const CATEGORY_GROUP='DEVICES_AND_OPERATING_SYSTEM';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
