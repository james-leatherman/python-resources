import requests

try:
    response = requests.get("http://your-service-url.com")
    if response.status_code != 200:
        print("Service down")
except Exception as e:
    print("Service unreachable")
