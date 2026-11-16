<?php
declare(strict_types=1);
final class GlobalAICoreContract {
 private array $payload;
 private function __construct(array $payload){$this->payload=$payload;}
 public static function fromArray(array $payload): self {
  foreach(['success','ecosystem_id','status'] as $key)if(!array_key_exists($key,$payload))throw new InvalidArgumentException('GLOBAL_AI_CORE_FIELD_REQUIRED: '.$key);
  if(!is_bool($payload['success'])||!is_string($payload['ecosystem_id'])||!is_string($payload['status']))throw new InvalidArgumentException('GLOBAL_AI_CORE_CONTRACT_TYPE_INVALID');
  return new self(self::sanitize($payload));
 }
 public static function fromJson(string $json): self {$data=json_decode($json,true,512,JSON_THROW_ON_ERROR);if(!is_array($data))throw new InvalidArgumentException('GLOBAL_AI_CORE_JSON_OBJECT_REQUIRED');return self::fromArray($data);}
 public function toArray(): array{return $this->payload;}
 public function toJson(): string{return json_encode($this->payload,JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES);}
 public function isLiveConnectionVerified(): bool{return ($this->payload['live_connection_verified']??false)===true;}
 private static function sanitize(array $data): array {$blocked=['token','access_token','refresh_token','client_secret','api_key','secret','authorization','password'];$out=[];foreach($data as $k=>$v){if(in_array(strtolower((string)$k),$blocked,true))continue;if(is_array($v))$v=self::sanitize($v);$out[$k]=$v;}return $out;}
}
