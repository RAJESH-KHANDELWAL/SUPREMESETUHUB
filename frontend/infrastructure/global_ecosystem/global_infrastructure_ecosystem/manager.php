<?php
/** Frontend Global Infrastructure Ecosystem manager; domain operations remain backend-owned. */
final class FrontendGlobalInfrastructureEcosystemManager {
    public const NAME = 'FRONTEND GLOBAL INFRASTRUCTURE ECOSYSTEM';
    public const VERSION = '1.4.1';
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];

    public function health(): array {
        $repository = dirname(dirname(dirname(dirname(__DIR__))));
        $backend = $repository . '/backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem';
        $backendDomains = [];
        foreach (self::DOMAINS as $domain) {
            $backendDomains[$domain] = is_dir($backend . '/' . $domain);
        }
        $required = ['__init__.py','manager.py','manager.php',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php'];
        $files = [];
        foreach ($required as $file) {
            $files[$file] = is_file(__DIR__ . '/' . $file);
        }
        $checks = [
            'backend_domains' => !in_array(false, $backendDomains, true),
            'required_files' => !in_array(false, $files, true)
        ];
        $healthy = !in_array(false, $checks, true);
        return ['name'=>self::NAME,'version'=>self::VERSION,
            'status'=>$healthy?'READY':'INCOMPLETE',
            'expected_backend_domain_count'=>count(self::DOMAINS),
            'backend_present_domain_count'=>count(array_filter($backendDomains)),
            'backend_domain_checks'=>$backendDomains,'required_file_checks'=>$files,
            'frontend_domain_files_expected'=>0,'frontend_domain_folders_expected'=>0,
            'checks'=>$checks,'healthy'=>$healthy,'provider_operations_enabled'=>false];
    }
}
