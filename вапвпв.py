import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent

data = {}
data['offer'] = []

i = 1

while i <= 100:
    response = requests.get(f'https://hotline.ua/ua/av/naushniki-garnitury/?p={i}',headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find_all('div', 'list-item list-item--row')

    for e in container:
        # try:
        monitor = e.find('a', 'list-item__title text-md').text
        link_monitor = e.find('a', 'list-item__title text-md').get('href')
        response2 = requests.get('https://hotline.ua/' + link_monitor, headers={'User-Agent': UserAgent().chrome})
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        container_next = soup2.find_all('div', 'price content')
        print(monitor)
        #
        # except Exception as e:
        #     continue