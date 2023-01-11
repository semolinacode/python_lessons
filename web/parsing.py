import requests
from bs4 import BeautifulSoup as BS
import fake_useragent
import json


def get_price(token_name='bitcoin'):
    url = f'https://www.coingecko.com/en/coins/{token_name}'
    user_agent = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user_agent
    }
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    # print(response.json())
    # print(response.text)

    html = BS(response.content, 'html.parser')
    price_lst = html.select('.tw-text-gray-900.tw-text-3xl span')
    if len(price_lst) == 0:
        print('Не могу найти цену')
        return None
    return float(price_lst[0].text.replace('$', '').replace(',', ''))

# print(get_price('ethereum'))


data = {
    'a': 1,
    'b': 2,
}

payload = {
    'data': json.dumps(data),
    'jsontemplate': 1,
    'jsonspec': 4,
    'jsonfix': 'on',
    'autoprocess': '',
    'version': 2
}

url = 'https://jsonformatter.curiousconcept.com/process'
response = requests.post(url, params=payload)
print(response.json()['result']['valid'])
