
from bs4 import BeautifulSoup as bs
import requests 

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)

html = response.text
soup = bs (html, 'lxml')


telephone_list = soup.find_all('div', class_='listbox_title oh')
telephone_price = soup.find_all('div',class_='listbox_price text-center')

titles = []
prices = []
links = []

for telephone in telephone_list:
        title = telephone.text.strip()
        titles.append(title)
# print(titles)

for telephone in telephone_price:
        price = telephone.text.strip()
        prices.append(price)


for telephone in telephone_list:
    link = 'https://www.kivano.kg' + telephone.find('a').get('href')
    links.append(link)

print(f'Название - {titles}\nЦена - {prices}\nСсылка - {links}')

import json 

with open ('zadanie1.json', 'w') as file:
    json.dump(titles,file )
    json.dump(prices,file)
    json.dump(links,file)



