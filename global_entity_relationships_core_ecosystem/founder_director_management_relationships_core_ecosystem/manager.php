<?php
/** Folder-aware PHP contract facade; no database/API writes. */
final class RelationshipModuleManager {
 public static function moduleKey(): string { return basename(__DIR__); }
 public static function ecosystemName(): string { return 'GLOBAL '.strtoupper(str_replace('_',' ',preg_replace('/_core_ecosystem$/','',self::moduleKey()))).' CORE ECOSYSTEM'; }
 public static function ecosystemId(): string { return 'GLOBAL-'.strtoupper(str_replace('_','-',preg_replace('/_core_ecosystem$/','',self::moduleKey()))).'-CORE-ECOSYSTEM'; }
 public static function status(): array { return ['ecosystem_id'=>self::ecosystemId(),'name'=>self::ecosystemName(),'module_key'=>self::moduleKey(),'status'=>'METADATA_AND_VALIDATION_ONLY','live_connection_verified'=>false,'persistence_enabled'=>false]; }
 public static function validate(array $record): array { foreach(['relationship_id','source_entity_id','target_entity_id','relationship_type'] as $field){if(empty($record[$field])) throw new InvalidArgumentException('Missing required field: '.$field);} if($record['source_entity_id']===$record['target_entity_id']) throw new InvalidArgumentException('Self relationship disallowed'); $state=$record['verification_status']??'UNVERIFIED'; if($state==='VERIFIED' && empty($record['source_urls'])) throw new InvalidArgumentException('Evidence required for verified status'); return ['valid'=>true,'ecosystem_id'=>self::ecosystemId(),'record'=>$record]; }
}
