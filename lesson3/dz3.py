from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from requests.exceptions import ConnectionError
from pprint import pprint
from pymongo import MongoClient
import re


def init_db_session():
    client = MongoClient("mongodb://root:example@0.0.0.0:22222/")
    db = client['vacations']
    session = db['vacations']
    return session


def write_in_db(session, data):
    session.insert_many(data)


def read_db(session):
    suspend_salaty = int(input('Введи желаемую зарплату\n'))
    if suspend_salaty == 0 or '':
        result = session.find()
    else:
        salary_filter = {"salary.0":
                             {"$lte": suspend_salaty},
                         "salary.1":
                             {"$gte": suspend_salaty}}
        result = session.find(salary_filter)

    for i in result:
        print(i)


def init_vac():
    '''
    get vac name from user and start programm
    :return:
    '''
    vac_name = input('Введите название вакансии:')
    return hh_vacs(vac_name)


def hh_vacs(vac, delay=2):
    '''
    create request
    :param vac: vacation name
    :param delay: delay for requset
    :return: responce
    '''
    URL = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    params = {'text': f'{vac}',
              'area': '1'}

    responce = requests.get(URL, headers=headers, params=params)

    sleep(delay)

    if responce.status_code == 200:
        return parsing_bs4(responce)
    raise ConnectionError(f'Ошибка ответа сервера {responce.status_code}')


def parsing_bs4(responce):
    '''
    start parsing
    :param responce:
    :return: list with dicts
    '''
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
                        salary = re.findall(r'\d+', element.text.replace('\u202f', ''))
                        salary_forg = [int(x) for x in salary]
                        data['salary'] = sorted(salary_forg)
                except AttributeError:
                    pass
        result.append(data)
    return result


if __name__ == '__main__':
    # data = init_vac()
    session = init_db_session()
    print('*' * 30)
    # write_in_db(session, data)
    print('*' * 30)
    read_db(session)
