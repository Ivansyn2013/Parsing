from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from requests.exceptions import ConnectionError
from pprint import pprint
from pymongo import MongoClient
import re

URL = 'https://www.roszdravnadzor.gov.ru/services/misearch'
DELAY = 2
USERAGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'

def get_response(url, delay=2):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}

    responce = requests.get(url, headers=headers, verify=False)
    #soup = bs(responce.content, 'html.parser')

    print(responce.status_code)
    print(responce.text)

if __name__ == "__main__":
    get_response(URL)