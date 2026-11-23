<?php
declare(strict_types=1);
/** Read-only PHP facade for hospitality service-work business manifest. */
final class GlobalHospitalityBusinessManager {
    public const ECOSYSTEM_ID = 'GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-SERVICE-WORK-BUSINESS-CORE';
    public const VERSION = '2.0.0';
    public function health(): array { return ['success'=>true,'ecosystem_id'=>self::ECOSYSTEM_ID,'version'=>self::VERSION,'service_delivery_enabled'=>false,'payments_enabled'=>false]; }
    public function manifest(): array {
        $path=__DIR__.'/ecosystem_manifest.json';
        if (!is_file($path)) { throw new RuntimeException('Manifest unavailable'); }
        $raw=file_get_contents($path); if ($raw===false) { throw new RuntimeException('Manifest read failed'); }
        return json_decode($raw,true,512,JSON_THROW_ON_ERROR);
    }
}
