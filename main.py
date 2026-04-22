import sys
import json
from subdomain import get_subdomain_passive
from subdomain import get_subdomain_active
from portscan import scan_ports
from livehost import probe_all
def main():
    if len(sys.argv)!=2:
        print("Usage: python main.py example.com")
        return
    domain=sys.argv[1]
    print(f"[+] Starting Recon(passive) on: {domain}")
    print("\n[+] Finding Subdomains...")
    subs=get_subdomain_passive(domain)
    print(f"\nSubdomain Found: {len(subs)} subdomains...")
    if len(subs)!=0:
     for i in range(len(subs)):
      print(f"{i+1}) {subs[i]}")
    else:
       print("[+] Starting Active Subdomain Enumuration...")
       subs=get_subdomain_active(domain,"subdomains.lst")
       print()
       print(f"Subdomain Found: {len(subs)} subdomains...")
       for i in range(len(subs)):
        print(f"{i+1}) {subs[i]}")
    print("[+] Probing live host...")
    live=probe_all(subs)
    print(f"[+] Live Host Found: {len(live)}")
    for i,hosts in enumerate(live):
      print(f"{i+1}) {hosts}")
    print("\n[+] Starting Open Port Scanning...")
    final_result=[]
    for host in live:
       domains=host["domain"]
       ports=scan_ports(domains)
       final_result.append({
          "domain": domains,
          "status": host["status"],
          "server": host.get("server"),
          "port": ports
        })
       with open("result.json","w") as f:
         json.dump(final_result,f,indent=4)
    print("\n [+] Final result saved to result.json")
if __name__=="__main__":
    main()