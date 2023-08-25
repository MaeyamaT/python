import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding

soup=BeautifulSoup(res.text,'html.parser')

names=soup.select('tr td:first-child')
for name in names:
    print(name.text)
