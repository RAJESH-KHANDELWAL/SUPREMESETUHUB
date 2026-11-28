<?php
declare(strict_types=1);
/** Safe result contract. Secrets are redacted and never stored. */
final class GlobalSocialMediaCoreContract {
 private function __construct(private array $payload) {}
 public static function fromArray(array $payload): self {
  if (!array_key_exists('success',$payload)||!array_key_exists('status',$payload)) throw new InvalidArgumentException('SOCIAL_MEDIA_CORE_RESULT_SCHEMA_INVALID');
  return new self(self::sanitize($payload));
 }
 public static function fromJson(string $json): self {
  $data=json_decode($json,true,512,JSON_THROW_ON_ERROR);
  if (!is_array($data)) throw new InvalidArgumentException('SOCIAL_MEDIA_CORE_RESULT_MUST_BE_OBJECT');
  return self::fromArray($data);
 }
 public function toArray(): array { return $this->payload; }
 public function toJson(): string { return json_encode($this->payload,JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES); }
 public function isLiveConnectionVerified(): bool { return ($this->payload['live_connection_verified']??false)===true; }
 private static function sanitize(array $data): array {
  $blocked=['access_token','refresh_token','client_secret','password','authorization','cookie','private_key','api_key'];$out=[];
  foreach($data as $key=>$value){$sensitive=false;foreach($blocked as $needle){if(str_contains(strtolower((string)$key),$needle)){$sensitive=true;break;}}
   $out[$key]=$sensitive?'[REDACTED]':(is_array($value)?self::sanitize($value):$value);
  }return $out;
 }
}
