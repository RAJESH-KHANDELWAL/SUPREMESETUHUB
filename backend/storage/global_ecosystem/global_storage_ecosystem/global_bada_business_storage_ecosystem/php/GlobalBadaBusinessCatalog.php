<?php
declare(strict_types=1);
/** Read-only PHP reader for the shared GLOBAL BADA BUSINESS taxonomy. */
final class GlobalBadaBusinessCatalog {
 private string $path;
 public function __construct(?string $path=null){$this->path=$path??__DIR__.'/../taxonomy/global_bada_business_storage_taxonomy.json';}
 public function load():array {
  if(!is_file($this->path)||!is_readable($this->path))throw new RuntimeException('Taxonomy missing or unreadable');
  $raw=file_get_contents($this->path);if($raw===false)throw new RuntimeException('Unable to read taxonomy');
  $data=json_decode($raw,true,512,JSON_THROW_ON_ERROR);if(($data['ecosystem_id']??null)!=='GLOBAL_BADA_BUSINESS_STORAGE_ECOSYSTEM')throw new UnexpectedValueException('Unexpected taxonomy identity');return $data;
 }
 public function all():array{return $this->load()['groups'];}
}
