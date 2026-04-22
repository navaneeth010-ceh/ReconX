import requests
from graph import progress

def probe_host(domain):
    try:
        urls=[f"https://{domain}",
              f"http://{domain}"
              ]
        for url in urls:
         response=requests.get(url,headers={"User-Agent": "Mozilla/5.0"},allow_redirects=True)
         return{
            "domain":domain,
            "url": url,
            "status":response.status_code,
            "server":response.headers.get("Server")
            }
    except:
        return None
def probe_all(domains):
    result=[]
    total=len(domains)
    for i,d in enumerate(domains,start=1):
        progress(i,total)
        res=probe_host(d)
        if res:
            result.append(res)
    print()
    return result