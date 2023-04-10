import requests
from lxml import html


def hh_vacs(vac):
    URL = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    params = {'text': f'{vac}',
              'area': '1'}

    responce = requests.get(URL, headers=headers, params=params)

    print(responce.status_code)
    dom = html.fromstring(responce.content)

    vacs = dom.xpath("//div[@class='serp-item']/div/div/div/div/h3/span/a")
    vac_list = []
    for vac in vacs:
        data = {}
        data['name'] = vac.xpath("text()")
        data['link'] = vac.xpath("@href")
        data['sallary'] = vac.xpath("../../../span/text()")
        data['site'] = URL
        vac_list.append(data)
    return data


def superjob_vacs(vac):
    URL = 'https://www.superjob.ru/vacancy/search'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    params = {'keywords': f'{vac}',
              'geo%5Bt%5D%5B0%5D': '4'}
    responce = requests.get(URL, headers=headers, params=params)
    print(responce.status_code)
    dom = html.fromstring(responce.content)
    vacs = dom.xpath('//div[@class="f-test-search-result-item"]')

    for vac in vacs:
        print(vac.xpath('/a'))


if __name__ == '__main__':
    vac = input('Введите название вакансии\n')
    superjob_vacs(vac)
