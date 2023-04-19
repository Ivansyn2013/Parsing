from lxml import html
from db_utils import write_in_db, init_db_session, read_db
import requests
def pasing_news_lenta():
    URL = 'https://lenta.ru/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    responce = requests.get(URL, headers=headers)

    if responce.status_code != 200:
        print(responce.status_code)
        return f'Error {responce.status_code}'

    dom = html.fromstring(responce.content)

    news = dom.xpath('//div[2]/div[3]/main/div/section[1]/div[1]/div['
                     '1]/div/a/div/span')

    session = init_db_session()
    news_list = []
    for num, el in enumerate(news):
        new = el.xpath('./text()')[0].encode('iso-8859-1').decode('utf-8')
        print(new)
        news_dict = {'number': num,
                     'news': new
                     }
        news_list.append(news_list)

    session = init_db_session()
    write_in_db(session, news_list)


if __name__=='__main__':
    session = init_db_session()
    pasing_news_lenta()
    print(read_db(session))