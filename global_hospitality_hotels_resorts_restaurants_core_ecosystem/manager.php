<?php
declare(strict_types=1);
/** Read-only PHP facade for the global hospitality industry core. */
final class GlobalHospitalityCoreManager {
    public const ECOSYSTEM_ID = 'GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-CORE-ECOSYSTEM';
    public function health(): array { return ['success'=>true, 'health'=>'HEALTHY', 'live_operations_enabled'=>false]; }
    public function manifest(): array {
        $raw = file_get_contents(__DIR__ . '/ecosystem_manifest.json');
        if ($raw === false) { throw new RuntimeException('Manifest unavailable'); }
        return json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
    }
    public function domains(): array { return $this->manifest()['domains'] ?? []; }
}
