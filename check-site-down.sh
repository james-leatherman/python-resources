import requests

try:
    response = requests.get("http://example.com")
    print("Website up") if response.status_code == 200 else print("Website down")
except:
    print("Website unreachable")
