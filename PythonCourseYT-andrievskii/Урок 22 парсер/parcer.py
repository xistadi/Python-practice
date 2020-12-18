import requests
from bs4 import BeautifulSoup

url = 'https://xn--90adear.xn--p1ai/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class': 'b-crash-stat'})
td = table.findAll('td')
for item in td:
    print(item.text)