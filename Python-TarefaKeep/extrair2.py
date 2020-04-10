import requests
from bs4 import BeautifulSoup
 
url = 'https://sistema.education1.com.br/rds/resp20'

Request =  requests.get(url)

soup = BeautifulSoup(Request.content, 'html.parser')

result = soup.find_all('h2')

print(result)

file = open('out2.txt', 'w')
file.write(str(result))
file.close()
