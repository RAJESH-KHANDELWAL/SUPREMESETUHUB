<?php
declare(strict_types=1);
/** PHP 8+ Apple Core JSON contract validator; no network I/O. */
final class AppleCoreContract {
 private const REQUIRED=['success','ecosystem_id','status'];
 private const SECRET_KEYS=['token','access_token','refresh_token','client_secret','api_key','secret','private_key','key_material'];
 public static function normalize(array $payload):array {
  foreach(self::REQUIRED as $key) if(!array_key_exists($key,$payload)) throw new InvalidArgumentException('APPLE_CORE_REQUIRED_FIELD_MISSING: '.$key);
  if(!is_bool($payload['success'])||!is_string($payload['ecosystem_id'])||!is_string($payload['status'])) throw new InvalidArgumentException('APPLE_CORE_INVALID_CONTRACT_TYPES');
  return self::redact($payload);
 }
 private static function redact(array $value):array { $safe=[]; foreach($value as $key=>$item){if(in_array(strtolower((string)$key),self::SECRET_KEYS,true))continue;$safe[$key]=is_array($item)?self::redact($item):$item;}return $safe; }
 public static function isLiveConnectionVerified(array $payload):bool{return ($payload['live_connection_verified']??false)===true;}
}
