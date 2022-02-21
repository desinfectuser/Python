import requests

domain = input("Bitte Namen der Domäne eingeben: ")
file = open("subdomains.txt")

subdomains = []
for i in file.readlines():
    subdomains.append(i.replace('\n' ' '))

found = []
for sub in subdomains:
    url = f'http://{sub}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        found.append(sub)
        print(f"Gefundene Subdomains: {sub}")
