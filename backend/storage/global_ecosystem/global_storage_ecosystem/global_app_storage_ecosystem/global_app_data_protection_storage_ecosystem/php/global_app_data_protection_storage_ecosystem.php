<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_DATA_PROTECTION_STORAGE_ECOSYSTEM. */
final class GlobalAppDataProtectionStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_DATA_PROTECTION_STORAGE_ECOSYSTEM';
 public const CATEGORY='DATA_PROTECTION';
 public const CATEGORY_GROUP='SECURITY_AND_PRIVACY';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
