"""Expanded, source-aware provider registry. Records are catalog references only."""
# This list is intentionally extensible; it is not a claim of exhaustive global coverage.
PROVIDER_NAMES = [
"101domain","Afilias","Amazon Route 53","Azure DNS","Alibaba Cloud DNS","Aruba","Automattic","AWS Route 53 Domains",
"Bluehost","Cloudflare","CloudNS","ClouDNS","ConoHa","CoreDNS","Crazy Domains","CZNIC","DNS Made Easy","DNSimple",
"DNSPod","Domain.com","DomainFactory","DomainPeople","DreamHost","Dynadot","DynDNS","EasyDNS","EuroDNS","Gandi",
"GoDaddy","Google Cloud Domains legacy","Google Cloud DNS","Gcore DNS","Hetzner DNS","Hover","Host Europe",
"Hostinger","HostGator","HostPapa","Infomaniak","Internet.bs","IONOS","iwantmyname","Japan Registry Services",
"Key-Systems","Linode/Akamai DNS","Linode","Loopia","MarkMonitor","Mesh DNS","Name.com","Namecheap","Names.co.uk",
"NameSilo","Network Solutions","Nominet","NS1","OpenDNS","Openprovider","OpenSRS","Oracle Cloud DNS","OVHcloud",
"Porkbun","PowerDNS","Public Interest Registry","Register.com","Registrar.eu","ResellerClub","RRPproxy","Squarespace Domains",
"SafeDNS","Sav","Shinjiru","Squarespace","Tencent Cloud DNS","TLD Registrar Solutions","Tucows","Vercel DNS",
"Verisign","Wix Domains","XServer","ZDNS","Zonomi","Afraid.org","DuckDNS","Dynu","No-IP","FreeDNS",
"ACME.sh","Certbot","Let's Encrypt","ZeroSSL","Buypass","DigiCert","GlobalSign","Sectigo","Entrust","SSL.com",
"Google Trust Services","Cloudflare Registrar","CentralNic","Identity Digital","Neustar","Registry Services LLC",
"Donuts legacy","Radix","Minds + Machines","Nic.io","Nominet UK","EURid","DENIC","AFNIC","CNNIC","NIC.br",
"NIC Mexico","NIC Chile","NIC Argentina","NIC India","INRegistry","JPRS","KRNIC","TWNIC","HKIRC","Singapore NIC",
"DomainTools","WhoisXML API","ICANN Lookup","RDAP.org","SecurityTrails","ViewDNS","DNSChecker","IntoDNS","MXToolbox",
"DNSViz","DNSPerf","NSLookup.io","DomainIQ","Whoxy"," Whois.com","DomainTools Monitor","BrandShelter","CSC Digital Brand Services",
"MarkMonitor Brand Protection","Sedo","Afternic","Dan.com legacy","Atom.com","Escrow.com","NameJet","DropCatch",
"SnapNames","Park.io","Sav.com marketplace","GoDaddy Auctions","Dynadot Marketplace","Flippa Domains","DomainAgents",
"Domain.io","Epik","Uniregistry legacy","Domain Parking","Bodis","ParkingCrew","Sedo Parking","Google Domains legacy",
"OctoDNS","Terraform DNS providers","Ansible DNS modules","Pulumi DNS","DNSControl","ExternalDNS","Technitium DNS",
"Pi-hole","AdGuard DNS","NextDNS","Quad9","Cloudflare 1.1.1.1","Google Public DNS","OpenDNS resolver","Control D",
"CleanBrowsing","Cisco Umbrella","Infoblox","F5 DNS","Akamai DNS","NS1 Connect","Constellix","UltraDNS","Dyn legacy",
"Oracle Dyn legacy","IBM NS1","Route 53 Resolver","Azure Private DNS","Google Cloud Private DNS","Kubernetes CoreDNS",
"PowerDNS Authoritative","BIND","Knot DNS","Unbound","MaraDNS","YADIFA","Hurricane Electric DNS","HE.net DNS",
"DNS-O-Matic","DNS Exit","DNS Made Easy Managed DNS","Gandi LiveDNS","Namecheap DNS","Porkbun DNS","Hostinger DNS",
"IONOS DNS","OVH DNS","Hetzner DNS","DigitalOcean DNS","Linode DNS","Vultr DNS","Render custom domains",
"Netlify custom domains","Fly.io domains","Railway custom domains","Heroku custom domains","GitHub Pages custom domains",
"CloudFront alternate domains","Fastly domains","Bunny DNS","Vercel custom domains","Shopify domains","WPMU DNS",
"WordPress.com domains","Wix DNS","Squarespace DNS","Weebly DNS","Webflow custom domains"
]
def list_expanded_provider_registry():
    seen = set()
    rows=[]
    for name in PROVIDER_NAMES:
        key=name.strip().upper().replace(" ","_").replace("/","_")
        if key in seen: continue
        seen.add(key)
        rows.append({"provider_id":key,"name":name,"categories":[],"source_type":"CURATED_REFERENCE","source_url":None,
          "region_scope":"GLOBAL_OR_REGIONAL_UNVERIFIED","api_available":None,"adapter_status":"NOT_IMPLEMENTED",
          "catalog_status":"CATALOG_ONLY","connected":False,"verified_at":None})
    return rows
