import requests


r = requests.get("https://bas@gmail.com")
print(r.status_code)
print(r.ok)
