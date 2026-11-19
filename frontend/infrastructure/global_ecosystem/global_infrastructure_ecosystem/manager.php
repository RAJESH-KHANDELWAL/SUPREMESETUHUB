<?php
/** Frontend manager validating the canonical backend infrastructure domains. */
final class FrontendGlobalInfrastructureEcosystemManager {
    public const NAME = 'FRONTEND GLOBAL INFRASTRUCTURE ECOSYSTEM';
    public const VERSION = '1.1.0';
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];
    public function health(): array {
        $backend = dirname(dirname(dirname(dirname(__DIR__)))) . '/backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem';
        $checks = [
            '__init__.py' => is_file(__DIR__ . '/__init__.py'),
            'manager.py' => is_file(__DIR__ . '/manager.py'),
            'manager.php' => is_file(__DIR__ . '/manager.php'),
        ];
        $domains = [];
        foreach (self::DOMAINS as $domain) {
            $domains[$domain] = is_dir($backend . '/' . $domain);
        }
        $checks['backend_manager'] = is_file($backend . '/manager.py');
        $checks['all_21_domains_present'] = !in_array(false, $domains, true);
        return ['name'=>self::NAME,'version'=>self::VERSION,
                'status'=>!in_array(false,$checks,true)?'READY':'INCOMPLETE',
                'checks'=>$checks,'domain_checks'=>$domains,
                'expected_domain_count'=>count(self::DOMAINS),
                'present_domain_count'=>count(array_filter($domains)),
                'healthy'=>!in_array(false,$checks,true)];
    }
}
