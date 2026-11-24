<?php
declare(strict_types=1);
/** Read-only PHP reader for GLOBAL APP taxonomy JSON. */
final class GlobalAppStorageCatalog {
 private string $taxonomyPath;
 public function __construct(?string $taxonomyPath=null){$this->taxonomyPath=$taxonomyPath??__DIR__.'/../taxonomy/global_app_storage_taxonomy.json';}
 public function load():array {
  if(!is_file($this->taxonomyPath)||!is_readable($this->taxonomyPath))throw new RuntimeException('GLOBAL APP taxonomy missing or unreadable');
  $raw=file_get_contents($this->taxonomyPath);if($raw===false)throw new RuntimeException('Unable to read taxonomy');
  $data=json_decode($raw,true,512,JSON_THROW_ON_ERROR);if(($data['ecosystem_id']??null)!=='GLOBAL_APP_STORAGE_ECOSYSTEM')throw new UnexpectedValueException('Unexpected taxonomy ecosystem_id');return $data;
 }
 public function all():array {$rows=[];foreach($this->load()['groups'] as $group)foreach($group['categories'] as $category)$rows[]=['group'=>$group['group'],'category'=>$category,'name'=>'GLOBAL_APP_'.$category.'_STORAGE_ECOSYSTEM','status'=>'CATALOG_ONLY','provider_product_verified'=>'false'];return $rows;}
 public function find(string $name):?array {$needle=strtoupper(trim($name));foreach($this->all() as $row)if($row['name']===$needle||$row['category']===$needle)return $row;return null;}
}
