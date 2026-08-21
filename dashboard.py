import os
import time
import shutil
import random
from datetime import datetime

def clear():
    os.system("clear")

def battery():
    try:
        with open("/sys/class/power_supply/battery/capacity") as f:
            return f.read().strip() + "%"
    except:
        return "N/A"

def storage():
    try:
        total, used, free = shutil.disk_usage("/")
        return f"{used // (1024**3)} GB / {total // (1024**3)} GB"
    except:
        return "N/A"

def matrix():
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%@"
    for _ in range(12):
        print("".join(random.choice(chars) for _ in range(65)))
        time.sleep(0.08)

clear()

print("\033[92m")
print("╔════════════════════════════════════════════════════════════╗")
print("║              S A N S K A R I   R O R                     ║")
print("║                 HACKER TERMINAL 2.0                      ║")
print("╚════════════════════════════════════════════════════════════╝")
print("\033[0m")

time.sleep(1)

print("\033[92m[+] INITIALIZING SYSTEM...\033[0m")
time.sleep(0.7)

print("\033[92m[+] SECURITY CHECK...\033[0m")
time.sleep(0.7)

print("\033[92m[+] LOADING MATRIX...\033[0m")
time.sleep(0.7)

matrix()

clear()

while True:
    now = datetime.now().strftime("%H:%M:%S")

    print("\033[92m")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                  SANSKARI ROR                              ║")
    print("║               SYSTEM DASHBOARD                             ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print(f"║  TIME       : {now:<42}║")
    print(f"║  BATTERY    : {battery():<42}║")
    print(f"║  STORAGE    : {storage():<42}║")
    print("║  STATUS     : SYSTEM ONLINE                               ║")
    print("║  SECURITY   : ACTIVE                                      ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print("║  [1] SYSTEM SCAN                                          ║")
    print("║  [2] MATRIX MODE                                          ║")
    print("║  [3] EXIT                                                  ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    choice = input("\033[92mSANSKARI-ROR@TERMUX:~$ \033[0m")

    if choice == "1":
        print("\n\033[92m[*] SCANNING LOCAL DEVICE...\033[0m")
        for i in range(0, 101, 10):
            print(f"\rSCAN PROGRESS: {i}%", end="", flush=True)
            time.sleep(0.15)
        print("\n\033[92m[+] SCAN COMPLETE — DEVICE SECURE\033[0m")
        input("\nPress ENTER...")

    elif choice == "2":
        clear()
        matrix()
        input("\nPress ENTER to return...")

    elif choice == "3":
        print("\033[92m\nSYSTEM SHUTDOWN...\033[0m")
        break

    else:
        print("\033[91mInvalid option!\033[0m")
        time.sleep(1)

    clear()

