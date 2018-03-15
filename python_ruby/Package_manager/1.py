import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.gopax.co.kr/notice')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title)
