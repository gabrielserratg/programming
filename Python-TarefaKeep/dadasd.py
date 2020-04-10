import requests
from lxml import html
from bs4 import BeautifulSoup
import gkeepapi

print("excute in python3!")

#Login e var
keep = gkeepapi.Keep()
success = keep.login('fortestestest82@gmail.com', 'gabrielserra')
LOGIN_URL = "https://sistema.education1.com.br/rds/resp20/autenticar"
URL = "https://sistema.education1.com.br/rds/resp20/tarefas"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {'tipopessoa': 'A', 'login': '29741', 'senha': 'DI3dyM', 'codigo': 'rds'}

    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    #print(result.text)

    #SCRAPE
    soup = BeautifulSoup(result.content, 'html.parser')
    result = soup.find_all('div', class_='quadrado-app tarefa')

    #print (result)

    for lista in result:
        info = lista.find_all('div')
        for lista_dados in info:
            #listainfo = lista_dados.next_element
            #print(listainfo)
            print(lista_dados.next_element)


    note = keep.createNote('Tarefa', lista_dados.next_element)
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Blue
    keep.sync()


        
    #print(bucket_names)
if __name__ == '__main__':
    main()