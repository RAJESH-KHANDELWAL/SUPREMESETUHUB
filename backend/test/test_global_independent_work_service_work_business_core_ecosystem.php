<?php
declare(strict_types=1);

require_once __DIR__ . '/../core/global_ecosystem/global_core_ecosystem/global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_service_work_business_core_ecosystem/manager.php';

$status = GlobalIndependentWorkServiceBusinessCoreManager::status();
$expectedId = 'GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM';

if (($status['ecosystem_id'] ?? null) !== $expectedId) {
    throw new RuntimeException('Service Work Business CORE ecosystem ID mismatch.');
}
if (($status['status'] ?? null) !== 'CORE_CATALOG_ONLY') {
    throw new RuntimeException('Unexpected Service Work Business CORE status.');
}
if (($status['canonical_owner'] ?? null) !== 'GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-CORE-ECOSYSTEM') {
    throw new RuntimeException('Canonical work-model owner mismatch.');
}
if (($status['python_is_canonical'] ?? null) !== true) {
    throw new RuntimeException('Python canonical ownership flag must be true.');
}

echo "Global Independent Work Service Work Business CORE PHP test: PASS\n";
