# import requests
# from bs4 import BeautifulSoup as BS
# import fake_useragent

# user_agent = fake_useragent.UserAgent().random

# headers = {
#     'user-agent': user_agent
# }

# url = 'https://www.coingecko.com/'
# response = requests.get(url, headers=headers)

# html = BS(response.content, 'html.parser')
# table = html.select('.sort.table.mb-0.text-sm.text-lg-normal.table-scrollable')[0]
# trs = table.select('tr')[1:]
# for tr in trs:
#     coint = tr.select('.d-lg-inline.font-normal.text-3xs.tw-ml-0.tw-text-gray-500')[0].text.strip()
#     print(coint)



import requests
import fake_useragent
import json

user_agent = fake_useragent.UserAgent().random

headers = {
    'user-agent': user_agent
}

data = {
    "tickerId": 913255078
}

payload = {
    'data': json.dumps(data),
    'jsontemplate': 1,
    'jsonspec': 4,
    'jsonfix': 'on',
    'autoprocess': '',
    'version': 2,
}

url = 'https://jsonformatter.curiousconcept.com/process'
response = requests.post(url, headers=headers, params=payload)
print(response.json()['result']['data'])
