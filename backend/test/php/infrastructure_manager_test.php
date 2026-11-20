<?php
require_once __DIR__ . '/../../infrastructure/manager.php';
require_once __DIR__ . '/../../infrastructure/global_ecosystem/global_infrastructure_ecosystem/manager.php';
$root = (new BackendInfrastructureManager())->health();
$ecosystem = (new BackendGlobalInfrastructureEcosystemManager())->health();
if (!$root['healthy']) { fwrite(STDERR, "Infrastructure manager checks failed: " . json_encode($root['checks']) . PHP_EOL); exit(1); }
if (!$ecosystem['healthy']) { fwrite(STDERR, "Global Infrastructure Ecosystem checks failed: " . json_encode($ecosystem['domain_checks']) . PHP_EOL); exit(1); }
echo "INFRASTRUCTURE MANAGER TEST: PASS" . PHP_EOL;
echo "GLOBAL INFRASTRUCTURE ECOSYSTEM: " . $ecosystem['present_domain_count'] . "/" . $ecosystem['expected_domain_count'] . " domains present" . PHP_EOL;
