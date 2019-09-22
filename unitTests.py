import json
import requests
url = 'http://127.0.0.1:5000/api/clubs'

def create_club():
    payload = {'name': 'Ahmed Club', 'description': 'best club out there', 'tags': 'Monkey'}
    r = requests.post(url, data=payload)
    print(r)