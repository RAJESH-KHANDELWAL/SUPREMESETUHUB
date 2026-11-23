<?php
declare(strict_types=1);
/** Read-only PHP facade for the hospitality core manifest. */
final class GlobalHospitalityCoreManager {
    public const ECOSYSTEM_ID='GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-CORE';
    public const VERSION='2.0.0';
    public function health(): array { return ['success'=>true,'ecosystem_id'=>self::ECOSYSTEM_ID,'version'=>self::VERSION,'live_booking_enabled'=>false,'payments_enabled'=>false]; }
    public function manifest(): array {
        $path=__DIR__.'/ecosystem_manifest.json';
        if(!is_file($path)){throw new RuntimeException('Manifest unavailable');}
        $raw=file_get_contents($path); if($raw===false){throw new RuntimeException('Manifest read failed');}
        return json_decode($raw,true,512,JSON_THROW_ON_ERROR);
    }
}
