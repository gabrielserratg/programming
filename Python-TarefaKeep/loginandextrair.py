import requests
from bs4 import BeautifulSoup
import time
#payload = {'email': '29741', 'senha': 'DI3dyM'}
payload = {'tipopessoa': 'A', 'login': '29741', 'senha': 'DI3dyM', 'codigo': 'rds'}
url = 'https://sistema.education1.com.br/rds/resp20/autenticar'
r = requests.post(url, data=payload)


#soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#lista_noticias = soup.find_all('table',class_='espaco')
#print(lista_noticias)
#print (r.content)
#Pagina de tarefas
url2 = 'https://sistema.education1.com.br/rds/resp20/tarefas'

Request =  requests.get(url2)

soup = BeautifulSoup(Request.content, 'html.parser')
result = soup.find_all('div')
print(result)