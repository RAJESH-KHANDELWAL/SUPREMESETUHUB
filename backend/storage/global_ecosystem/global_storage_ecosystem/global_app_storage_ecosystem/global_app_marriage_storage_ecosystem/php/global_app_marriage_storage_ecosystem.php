<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_MARRIAGE_STORAGE_ECOSYSTEM. */
final class GlobalAppMarriageStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_MARRIAGE_STORAGE_ECOSYSTEM';
 public const CATEGORY='MARRIAGE';
 public const CATEGORY_GROUP='RELATIONSHIP_AND_ADULT_CLASSIFICATION';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
