<?php
declare(strict_types=1);

/**
 * Contract tests for GLOBAL AFFILIATE MARKETING BUSINESS CORE.
 * This test is read-only and does not call external affiliate providers.
 */
require_once dirname(__DIR__, 7)
    . '/backend/core/global_ecosystem/global_core_ecosystem/global_bada_business_core_ecosystem/global_affiliate_marketing_business_core_ecosystem/manager.php';

function expectAffiliateCore(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

$manager = new GlobalAffiliateMarketingCoreManager();
$health = $manager->health();
expectAffiliateCore(
    $health['ecosystem_id'] === GlobalAffiliateMarketingCoreManager::ECOSYSTEM_ID,
    'ecosystem identity'
);
expectAffiliateCore($health['healthy'] === true, 'required CORE files exist');
expectAffiliateCore($health['status'] === 'READY', 'CORE health status');
expectAffiliateCore($health['live_connections_verified'] === false, 'no false live-connection claim');
expectAffiliateCore($health['payout_execution_enabled'] === false, 'payout execution remains disabled');

$inventory = $manager->masterCatalogInventory();
expectAffiliateCore($inventory['success'] === true, 'master catalog loads');
expectAffiliateCore(
    $inventory['catalogue_id'] === 'GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM',
    'master catalog identity'
);
expectAffiliateCore($inventory['target_unique_entries'] === 2468, 'master catalog target count');
expectAffiliateCore(
    $inventory['current_unique_entries'] + $inventory['remaining_unique_entries'] === 2468,
    'master catalog current and remaining counts'
);
expectAffiliateCore($inventory['source_numbered_entries'] === 248, 'source numbered entry count');
expectAffiliateCore($inventory['cross_reference_entries'] === 2, 'cross-reference count');
expectAffiliateCore($inventory['section_count'] === 13, 'master catalog section count');

$affiliateEntry = $manager->getMasterCatalogEntry('S08_affiliate_business');
expectAffiliateCore(is_array($affiliateEntry), 'affiliate business entry is available');
expectAffiliateCore(
    $affiliateEntry['entry_id'] === 'S08_affiliate_business',
    'affiliate business entry identity'
);
expectAffiliateCore(
    $manager->getMasterCatalogEntry('UNKNOWN_ENTRY') === null,
    'unknown master catalog entry returns null'
);

echo "All Global Affiliate Marketing CORE PHP tests passed.\n";
