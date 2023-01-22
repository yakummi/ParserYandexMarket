import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

x = 1

categoryid = 1
valutaid = 'UAH'

data = {}
data['offer'] = []

while x <= 3:
    try:
        response = requests.get(f'https://hotline.ua/computer/monitory/?p={x}', headers={'User-Agent': UserAgent().chrome})
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'list-item list-item--row')
        for elements_container in container:
            monitor = elements_container.find('a', 'list-item__title text-md').text
            link_monitor = elements_container.find('a', 'list-item__title text-md').get('href')
            response2 = requests.get('https://hotline.ua/'+link_monitor, headers={'User-Agent': UserAgent().chrome})
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            # container_next = soup2.find_all('div', 'list__item row flex')
            container_next = soup2.find_all('div', 'price content')
            for contai in container_next:
                title = contai.find_all('div', 'list__item row flex')
                for elements_next in title:
                    shop_name = elements_next.find('div', 'text-wrapper').text
                    # shop_name = elements_next.find('a', 'shop__title mb-row').get('href')
                    title = elements_next.find('a', 'shop__title mb-row').text
                    link = elements_next.find('a', 'shop__title mb-row').get('href')
                    response_link = requests.get('https://hotline.ua'+link, headers={'User-Agent': UserAgent().chrome})
                    print(response_link)
                    print(shop_name)
                    print((title.replace(' ', '')).replace('\n', ''))
                    if (title.replace(' ', '')).replace('\n', '') == 'ЖЖУК':
                        print((monitor.lstrip()).replace('\n', ''))
                        print((title.replace(' ', '')).replace('\n', ''))
                        price = elements_next.find('span', 'price__value').text
                        data['offer'].append({
                            'categoryId': categoryid,
                            'currencyId': valutaid,
                            'name': (monitor.lstrip()).replace('\n', ''),
                            'shop_name': shop_name,
                            'price': price.replace('\xa0', ''),
                            'shop_url': response_link.url,
                            'url': 'https://hotline.ua'+link_monitor
                        })
                    else:
                        continue
        x = x + 1
    except Exception as ex:
        continue


with open('jjj.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
