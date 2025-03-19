
from bs4 import BeautifulSoup as bs
import requests 

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)

html = response.text
soup = bs (html, 'lxml')


telephone_list = soup.find_all('div', class_='listbox_title oh')
telephone_price = soup.find_all('div',class_='listbox_price text-center')

phones = []

for i in range (len(telephone_list)):
    title = telephone_list[i].text.strip()
    price = telephone_price[i].text.strip()
    link = 'https://www.kivano.kg'+telephone_list[i].find('a').get('href')

    phone = {
        'title': title,
        'price': price,
        'link': link
    }

    phones.append(phone)

for phone in phones:
    print(f"Название: {phone['title']}, Цена: {phone['price']}, Ссылка: {phone['link']}")

import json

with open('hackaton1.json', 'w') as file:
    json.dump(phones,file)