import random, os, requests

with open("more_proxies.txt") as red:
    lines = red.readlines()

random_line = random.choice(lines)
proxy = random_line.strip()

test_url = "http://api.ipify.org?format=json"  # Use HTTP to avoid tunneling issues
timeout = 5
print("Testing HTTP proxies...\n")

response = requests.get(test_url, proxies = {"http": proxy }, timeout=timeout)
if response.status_code == 200:
    ip = response.json().get("origin")
    print(f"✅ {proxy} ➜ Working! IP: {ip}")
else:
    print(f"❌ {proxy} ➜ Status code: {response.status_code}")