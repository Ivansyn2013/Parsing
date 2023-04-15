from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from requests.exceptions import ConnectionError
from pprint import pprint


def init_vac():
    vac_name = input('Введите название вакансии:')
    return hh_vacs(vac_name)


def hh_vacs(vac, delay=2):
    URL = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    params = {'text': f'{vac}',
              'area': '1'}

    responce = requests.get(URL, headers=headers, params=params)

    print(type(responce.status_code))
    sleep(delay)

    if responce.status_code == 200:
        return parsing_bs4(responce)
    raise ConnectionError(f'Ошибка ответа сервера {responce.status_code}')


def parsing_bs4(responce):
    soup = bs(responce.content, 'html.parser')
    list_of_main_div = soup.find_all('div', {'class': 'serp-item'})
    result = []
    for vac in list_of_main_div:
        children = list(list(vac.children)[0].children)[0]

        data = {name: text.text for name, text in zip(['vac_name', 'company'], children.find_all('a'))}
        salary_list = children.find_all('span')
        for element in salary_list:
            if element.previous_sibling:
                try:
                    if 'bloko-v-spacing' in element.previous_sibling.get('class'):
                        data['salary'] = element.text
                except AttributeError:
                    pass
        result.append(data)
    return result


if __name__ == '__main__':
    print(init_vac())
