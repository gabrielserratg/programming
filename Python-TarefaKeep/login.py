import requests
from bs4 import BeautifulSoup


payload = {'email': '29741', 'senha': 'DI3dyM'}
url = 'https://sistema.education1.com.br/rds/aluno/autenticar'
r = requests.post(url, data=payload)

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

lista_noticias = soup.find_all('table',class_='espaco')

print(lista_noticias)

print (r.content)