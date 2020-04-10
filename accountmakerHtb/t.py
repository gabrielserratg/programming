#import os
import subprocess
import requests
from bs4 import BeautifulSoup
from lxml import html
payload = {'','',''}

subprocess.call(["ls", "-l"])


url = "https://www.hackthebox.eu/invite"



r = requests.post(url, data=payload)

print (r.content)
