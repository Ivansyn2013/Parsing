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
    return vac_list


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

    vacs_list = []
    for vac in vacs:
        data = {}
        data['name'] = vac.xpath('./div/div/div/div/div/div/div/div/div/div/div/span/a/text()')
        data['link'] =vac.xpath('./div/div/div/div/div/div/div/div/div/div/div/span/a/@href')
        data['sallary']= vac.xpath(
            'div/div/div/div/div/div/div/div/div/div/div/div/div/span/text()')
        data['site'] = URL
        vacs_list.append(data)
    return vacs_list

if __name__ == '__main__':
    vac = input('Введите название вакансии\n')
    print(superjob_vacs(vac))
    print('*'*100)
    print(hh_vacs(vac))
