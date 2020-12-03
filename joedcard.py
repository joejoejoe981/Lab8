
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dcard.tw/forum/all')

if r.status_code == 200:
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('h3', class_ = 'sc-1kalffa-0 ksmfRV')
    for i in data:
            print(i.string)
            print(i.get('href'))

