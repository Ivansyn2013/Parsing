import os

from dotenv import load_dotenv
from requests import request
from pprint import  pprint
import json

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
USER_ID = os.getenv('USER_ID')

URL = f'https://shikimori.one/api/v2/user_rates/{USER_ID}'
headers = {
    'User-Agent':'Api Test',
    'Authorization': f'Bearer {API_TOKEN}',
           }
params = {}

responce = request('GET', URL, headers=headers, params=params)

print( f'{responce.status_code}')
data = responce.json()

with open('tmp/api_list.json', 'w') as file:
    json.dump(data, file)


