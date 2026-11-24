<?php
declare(strict_types=1);
/** Sanitized language-neutral Slack Core result contract. */
final class SlackCoreContract {
 private array $payload;
 private function __construct(array $payload){$this->payload=$payload;}
 public static function fromArray(array $payload):self {
  foreach(['success','ecosystem_id','status'] as $key)if(!array_key_exists($key,$payload))throw new InvalidArgumentException('SLACK_CORE_FIELD_REQUIRED: '.$key);
  if(!is_bool($payload['success'])||!is_string($payload['ecosystem_id'])||!is_string($payload['status']))throw new InvalidArgumentException('SLACK_CORE_CONTRACT_TYPE_INVALID');
  return new self(self::sanitize($payload));
 }
 public static function fromJson(string $json):self {$data=json_decode($json,true,512,JSON_THROW_ON_ERROR);if(!is_array($data))throw new InvalidArgumentException('SLACK_CORE_JSON_OBJECT_REQUIRED');return self::fromArray($data);}
 public function toArray():array{return $this->payload;}
 public function toJson():string{return json_encode($this->payload,JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES);}
 public function isLiveConnectionVerified():bool{return ($this->payload['live_connection_verified']??false)===true;}
 private static function sanitize(array $value):array {$blocked=['token','access_token','refresh_token','client_secret','api_key','secret','authorization','password','signing_secret'];$out=[];foreach($value as $k=>$v){if(in_array(strtolower((string)$k),$blocked,true))continue;$out[$k]=is_array($v)?self::sanitize($v):$v;}return $out;}
}
