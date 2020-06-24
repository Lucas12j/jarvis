import requests
from bs4 import BeautifulSoup
import csv
from unidecode import unidecode

lista_final = []
array = []
url = "https://www.fundamentus.com.br/detalhes.php?papel"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
r = requests.get(url, headers=agent)
soup = BeautifulSoup(r.text, 'lxml')
nome = str(soup.select(".resultado tr td:nth-child(2)")) 
codigo = str(soup.select(".resultado tr td a"))
aux = 0

for i in nome.split('<td>'):
    if aux == 0:
        pass
    else:
        lista_final.append(      [   unidecode ((i.replace('</td>,','')).strip())    ]          )
    aux+=1
aux = 0
for i in codigo.split("</a>"):
    try:
        lista_final[aux].append(  i.split('">')[1] )
    except:
        pass
    aux +=1

tabela = csv.writer(open('library/Class_Finance/tabela.csv', 'w'))
for i in lista_final:
    tabela.writerow(i)
