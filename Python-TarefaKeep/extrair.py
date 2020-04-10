import requests
from bs4 import BeautifulSoup
 
url = 'https://sistema.education1.com.br/rds/aluno/'

req =  requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

lista_noticias = soup.find_all('h1')


print(lista_noticias)