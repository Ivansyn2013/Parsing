import requests
from lxml import html

vac = input('Введите название вакансии\n')

URL = 'https://hh.ru/search/vacancy'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
params = {'text': f'{vac}',
          'area': '1'}

responce = requests.get(URL, headers=headers, params=params)

print(responce.status_code)
dom = html.fromstring(responce.content)

list_pars = dom.xpath("//div[@class='serp-item']")
print(list_pars)
