import json
import os
from time import sleep


pessoas = [
    {
        'firstname': 'Diego',
        'lastname': 'Santos',
        'age': 22,
        'email': 'diego@gmail.com',
        'addresses': [
            {'line1': 'Sao Paulo'},
            {'line2': 'Rio de Janeiro'},
            {'line3': 'Santa Catarina'}
        ]
    },
        {
        'firstname': 'Marta',
        'lastname': 'Pereira',
        'age': 15,
        'email': 'marta@gmail.com',
        'addresses': [
            {'line1': 'Brasilia'},
            {'line2': 'Maranhao'},
            {'line3': 'parana'}
        ]
    }
]


def load():
    os.system('clear')
    print('carregando json: ------------------- 0%')
    sleep(1)
    os.system('clear')
    print('carregando json: ====--------------- 10%')
    sleep(1)
    os.system('clear')
    print('carregando json: =========----------- 40%')
    sleep(1)
    os.system('clear')
    print('carregando json: =================--- 80%')
    sleep(1)
    os.system('clear')
    print('carregando json: ==================== 100%')
    os.system('clear')


# Gerando um arquivo .json
def generate_json():
    BASE_DIR = os.path.dirname(__file__)
    SAVE_TO = os.path.join(BASE_DIR, 'aula113.json')

    with open(SAVE_TO, 'w', encoding='utf-8') as file:
        return json.dump(pessoas, file, indent=2)
    
    
# Gerando um arquivo .json
def get_json():
    BASE_DIR = os.path.dirname(__file__)
    JSON_FILE = os.path.join(BASE_DIR, 'aula113.json')

    with open(JSON_FILE, 'r') as file:
        pessoas = json.load(file)
    return pessoas


if __name__ == '__main__':
    while True:
        try:
            print(get_json())
            break
        except FileNotFoundError:
            load()
            generate_json()
        
        
        