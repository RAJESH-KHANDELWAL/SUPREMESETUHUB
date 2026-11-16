<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_FITNESS_STORAGE_ECOSYSTEM. */
final class GlobalAppFitnessStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_FITNESS_STORAGE_ECOSYSTEM';
 public const CATEGORY='FITNESS';
 public const CATEGORY_GROUP='HEALTH_AND_WELLNESS';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
