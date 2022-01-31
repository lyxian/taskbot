import requests
import sys

data = {
    'action': sys.argv[1],
    # 'action': 'ADD',
    # 'action': 'STOP',
    'name': 'first'
}

URL = 'http://localhost:5005'

if __name__ == '__main__':
    response = requests.post(url=URL, json=data)
    print(response.text)