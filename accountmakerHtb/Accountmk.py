import os
import requests
import subprocess
from bs4 import BeautifulSoup


os.system("curl -X POST https://www.hackthebox.eu/api/invite/generate")

print ("")
print ("")

based = input("Encoded: ")

f = open("log.txt", "w")
f.write(based)
f.close()
print("")
os.system("base64 -d log.txt")
print("")
decoded = input("Decoded: ")

url = "https://www.hackthebox.eu/invite"
x = requests.post(url , data=payload)
payload = {}




print("")
#print(r.content)