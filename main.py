import sys
import json
from subdomain import get_subdomain
def main():
    if len(sys.argv)!=2:
        print("Usage: python main.py example.com")
        return
    domain=sys.argv[1]
    print(f"[+] Starting Recon on: {domain}")
    print("[+] Finding Subdomains...")
    subs=get_subdomain(domain)
    print(f"Subdomain Found: {len(subs)} subdomains...")
if __name__=="__main__":
    main()