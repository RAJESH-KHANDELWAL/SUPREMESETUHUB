<?php
declare(strict_types=1);
/** Read-only PHP facade for hospitality service-work business catalog. */
final class GlobalHospitalityBusinessManager {
    public const ECOSYSTEM_ID = 'GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM';
    public function health(): array { return ['success'=>true, 'health'=>'HEALTHY', 'service_delivery_enabled'=>false, 'transactions_enabled'=>false]; }
    public function manifest(): array {
        $raw = file_get_contents(__DIR__ . '/ecosystem_manifest.json');
        if ($raw === false) { throw new RuntimeException('Manifest unavailable'); }
        return json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
    }
    public function domains(): array { return $this->manifest()['domains'] ?? []; }
}
