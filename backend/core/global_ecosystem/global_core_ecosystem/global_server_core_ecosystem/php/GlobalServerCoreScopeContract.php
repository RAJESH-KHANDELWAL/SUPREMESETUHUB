<?php
declare(strict_types=1);

/**
 * Read-only PHP 8+ normalizer for GLOBAL SERVER CORE scope metadata.
 * Validates catalog shape only; it never grants access or authorizes deployments.
 */
final class GlobalServerCoreScopeContract
{
    public static function normalize(array $payload): array
    {
        $tierCatalog = $payload['service_tiers'] ?? [];
        $workloadCatalog = $payload['workload_domains'] ?? [];
        $geography = $payload['geographic_scope'] ?? null;

        if (!is_array($tierCatalog) || !is_array($workloadCatalog) || !is_array($geography)) {
            throw new InvalidArgumentException('Invalid server scope catalog structure');
        }
        $tiers = $tierCatalog['tiers'] ?? $tierCatalog;
        $domains = $workloadCatalog['domains'] ?? $workloadCatalog;
        if (!is_array($tiers) || !is_array($domains)) {
            throw new InvalidArgumentException('Invalid tier or workload list');
        }

        $requiredTiers = [
            'NORMAL', 'BASIC', 'STANDARD', 'PREMIUM',
            'PROFESSIONAL', 'ENTERPRISE', 'SUPREME',
        ];
        $actualTiers = [];
        foreach ($tiers as $tier) {
            if (!is_array($tier) || !isset($tier['tier_id'])) {
                throw new InvalidArgumentException('Each service tier requires tier_id');
            }
            $actualTiers[] = strtoupper((string) $tier['tier_id']);
        }
        if ($actualTiers !== $requiredTiers) {
            throw new InvalidArgumentException('Service tier order does not match the canonical contract');
        }

        $seenDomains = [];
        foreach ($domains as $domain) {
            if (!is_array($domain) || empty($domain['domain_id'])) {
                throw new InvalidArgumentException('Each workload domain requires domain_id');
            }
            $id = strtoupper((string) $domain['domain_id']);
            if (isset($seenDomains[$id])) {
                throw new InvalidArgumentException('Duplicate workload domain_id: ' . $id);
            }
            $seenDomains[$id] = true;
        }

        $india = $geography['india'] ?? [];
        $country = strtoupper((string) ($india['country_code'] ?? ''));
        $coverageModel = strtoupper((string) ($geography['coverage_model'] ?? ''));
        if ($country !== 'IN' || $coverageModel !== 'INDIA_FIRST_GLOBAL_EXTENSIBLE') {
            throw new InvalidArgumentException('Geography must retain Bharat-first scope');
        }

        return [
            'service_tiers' => $tiers,
            'workload_domains' => $domains,
            'geographic_scope' => $geography,
            'authorization_granted' => false,
            'remote_operations_enabled' => false,
        ];
    }
}
