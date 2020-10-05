import requests


r = requests.get("https://basstuiv@gmail.com")
print(r.status_code)
print(r.ok)
