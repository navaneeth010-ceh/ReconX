import requests
def get_subdomain(domain):
    url=f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
       response=requests.get(url,timeout=10)
       data=response.json()
       subdomains=set()
       for entry in data:
            name=entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    subdomains.add(sub.strip())
                    if domain in sub:
                        subdomains.add(sub.strip())
       return subdomains.list()
    except Exception as e:
        print(f"[ERROR] Subdomain fetch fail: {e}")
        return[]