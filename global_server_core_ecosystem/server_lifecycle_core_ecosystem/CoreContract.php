<?php

declare(strict_types=1);
namespace SupremeSetuHub\ServerCore\server_lifecycle_core;
/** Declarative contract only; no infrastructure operation is executed. */
final class CoreContract {
 public const DOMAIN_ID = 'server_lifecycle_core';
 public const DOMAIN_LABEL = 'Server Lifecycle Core';
 public const DESCRIPTION = 'Lifecycle states and transition rules; no provisioning or deletion execution.';
 public const LAYER = 'CORE';
 public const SCHEMA_VERSION = '1.0.0';
 public const EXECUTION_ENABLED = false;
 public static function descriptor(): array { return ['domain_id'=>self::DOMAIN_ID,'label'=>self::DOMAIN_LABEL,'description'=>self::DESCRIPTION,'layer'=>self::LAYER,'schema_version'=>self::SCHEMA_VERSION,'status'=>'DECLARATIVE_CORE_CONTRACT','execution_enabled'=>self::EXECUTION_ENABLED]; }
}
