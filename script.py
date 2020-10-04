import sys
import math
from os import rename
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hallo, {}".format(who_to_greet)
    return greeting


r = requests.get("https://basstuiv@gmail.com")
print(r.status_code)
