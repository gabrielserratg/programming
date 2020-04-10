import requests
import time
import pylint

url = 'http://localhost/index.html'


count = int(input("Count: "))

infinito = 5001

if count > infinito:
    print("infinity Sending...")
    for r in range(99999999999999):
        requests.get(url)
else:
    print("Sending... GET,POST")
    for r in range(count):
        requests.get(url)
