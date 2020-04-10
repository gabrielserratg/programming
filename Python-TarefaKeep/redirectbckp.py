import requests
from bs4 import BeautifulSoup
from lxml import html
#payload = {'email': '29741', 'senha': 'DI3dyM'}
payload = {'tipopessoa': 'A', 'login': '29741', 'senha': 'DI3dyM', 'codigo': 'rds'}
url = 'https://sistema.education1.com.br/rds/resp20/autenticar'
r = requests.post(url, data=payload)

#print (r.content)

