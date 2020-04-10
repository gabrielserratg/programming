import requests
from bs4 import BeautifulSoup
from lxml import html
#payload = {'email': '29741', 'senha': 'DI3dyM'}
payload = {'tipopessoa': 'A', 'login': '29741', 'senha': 'DI3dyM', 'codigo': 'rds'}


url = "https://sistema.education1.com.br/rds/resp20/autenticar"
urlredict = "https://sistema.education1.com.br/rds/resp20/login/"


#r = requests.post(url, data=payload)

session_requests = requests.session()

result = session_requests.get(url)
tree = html.fromstring(result.text)

    # Perform login
    result = session_requests.post(url, data=payload, headers=dict(referer = url))

    #result for testing
    r = requests.post(urlredict, data=payload)


    # Scrape url
    result = session_requests.get(urlredict, headers = dict(referer = urlredict))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)



#print (r.content)
