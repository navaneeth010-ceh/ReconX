import requests
import time
import dns.resolver
from graph import progress
from concurrent.futures import ThreadPoolExecutor,as_completed
def get_subdomain_passive(domain):
    url=f"https://api.hackertarget.com/hostsearch/?q={domain}"
    headers = {"User-Agent": "Mozilla/5.0"}
    for attempt in range(3):
        try:
            response=requests.get(url,headers=headers,timeout=10)
            if "error" in response.text.lower():
                print(f"[!] API Error ")
                return []
            subdomain=set()
            lines=response.text.splitlines()
            total=len(lines)
            for i,line in enumerate(response.text.splitlines(),start=1):
                sub=line.split(",")[0]
                progress(i,total)
                subdomain.add(sub.strip())
            return list(subdomain)
        except Exception as e:
            print(f"[RETRY {attempt+1} Error: {e}]")
            print("[ERROR] Failed after retries")
            return []
def loadwordlist(filepath):
    with open(filepath,"r") as f:
        return [line.strip() for line in f if line.strip()]
    
def checksubdomain(sub,domain):
    fulldomain=f"{sub}.{domain}"
    resolver=dns.resolver.Resolver()
    resolver.timeout=2;
    resolver.lifetime=2;
    try:
        resolver.resolve(fulldomain,'A')
        print(f"[+] Found: {fulldomain}")
        return fulldomain
    except:
        return None
def get_subdomain_active(domain,wordlist):
    subdomain=loadwordlist(wordlist)
    total=len(subdomain)
    found=[]
    with ThreadPoolExecutor(max_workers=20) as excecutor:
        futures=[excecutor.submit(checksubdomain,sub,domain)
                 for sub in subdomain
        ]
        for i,future in enumerate(as_completed(futures),start=1):
            progress(i,total)                                            
            result=future.result()
            if result:
                found.append(result)
    return list(set(found))