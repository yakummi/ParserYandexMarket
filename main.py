import requests
from bs4 import BeautifulSoup
import json

data = {}
data['product'] = []

i = 1

while i <= 60:

    response = requests.get(url=f'https://ek.ua/list/200/{i}')

    soup = BeautifulSoup(response.text, 'html.parser')

    container = soup.find_all('div', 'model-short-div list-item--goods')

    for e in container:
        try:

            title = e.find('span', 'u').text
            print(title)
            price = e.find('div', {'class': 'model-price-range'}).text
            print((price.split('Сравнить')[0]))
            link = e.find('a', 'model-short-title no-u').get('href')
            print('https://ek.ua' + link)
            data['product'].append({
                'title': title,
                'price': (price.split('Сравнить')[0]),
                'link': 'https://ek.ua' + link
            })

        except Exception as ex:
            continue
    i = i + 1



with open('gdfgd.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)