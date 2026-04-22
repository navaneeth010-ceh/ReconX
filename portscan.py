import socket
from graph import progress
from concurrent.futures import ThreadPoolExecutor,as_completed

common_ports=[21,22,25,53,80,110,143,443,3306,8080]
def scan_port(domain,port):
    try:
        soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.settimeout(1)
        result=soc.connect_ex((domain,port))
        soc.close()
        if result==0:
            return port
    except:
        pass
    return None
def scan_ports(domain):
    open_port=[]
    total=len(common_ports)

    with ThreadPoolExecutor(max_workers=20) as executer:
        futures=[executer.submit(scan_port,domain,p) for p in common_ports]
        for i,future in enumerate(as_completed(futures),start=1):
            progress(i,total)
            res=future.result()
            if res:
                open_port.append(res)
    print()
    for port in open_port:
        print(f"[+] {domain}: {port} OPEN!")
    return open_port
