from requests import request
from pprint import pprint
import json

USER_NAME = 'Ivansyn2013'
URL = f'https://api.github.com/users/{USER_NAME}/repos'
headers = {'User-Agent':'Python',
           'Accept': 'application/vnd.github+json'}

req = request('GET', URL, headers=headers)

if req.status_code == 200:
    data = req.json()

    with open('tmp/repo_list.json', 'w') as file:
        json.dump(data, file)


else:
    print(f'Ошибка {req.status_code}')

