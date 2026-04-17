import requests
def get_subdomain(domain):
    domain="zorvyn.live"
    url=f"https://crt.sh/?q=%25.{domain}&output=json"
    response=requests.get(url,timeout=10)
    if response.status_code==200:
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
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
    