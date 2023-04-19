from lxml import html
from db_utils import write_in_db, init_db_session
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

    for el in news:
        print(el.xpath('./text()'))
        break

if __name__=='__main__':

    pasing_news_lenta()