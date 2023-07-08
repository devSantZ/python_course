import json
import os
# from time import sleep


# pessoas = [
#     {
#         'firstname': 'Diego',
#         'lastname': 'Santos',
#         'age': 22,
#         'email': 'diego@gmail.com',
#         'addresses': [
#             {'line1': 'Sao Paulo'},
#             {'line2': 'Rio de Janeiro'},
#             {'line3': 'Santa Catarina'}
#         ]
#     },
#         {
#         'firstname': 'Marta',
#         'lastname': 'Pereira',
#         'age': 15,
#         'email': 'marta@gmail.com',
#         'addresses': [
#             {'line1': 'Brasilia'},
#             {'line2': 'Maranhao'},
#             {'line3': 'parana'}
#         ]
#     }
# ]


# def load():
#     os.system('clear')
#     print('carregando json: ------------------- 0%')
#     sleep(1)
#     os.system('clear')
#     print('carregando json: ====--------------- 10%')
#     sleep(1)
#     os.system('clear')
#     print('carregando json: =========----------- 40%')
#     sleep(1)
#     os.system('clear')
#     print('carregando json: =================--- 80%')
#     sleep(1)
#     os.system('clear')
#     print('carregando json: ==================== 100%')
#     os.system('clear')


# # Gerando um arquivo .json
# def generate_json():
#     BASE_DIR = os.path.dirname(__file__)
#     SAVE_TO = os.path.join(BASE_DIR, 'aula113.json')

#     with open(SAVE_TO, 'w', encoding='utf-8') as file:
#         return json.dump(pessoas, file, indent=2)
    
    
# # Gerando um arquivo .json
# def get_json():
#     BASE_DIR = os.path.dirname(__file__)
#     JSON_FILE = os.path.join(BASE_DIR, 'aula113.json')

#     with open(JSON_FILE, 'r') as file:
#         pessoas = json.load(file)
#     return pessoas


# if __name__ == '__main__':
#     while True:
#         try:
#             print(get_json())
#             break
#         except FileNotFoundError:
#             load()
#             generate_json()
        
        
BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'aulas113_carro.json')

carro = {
    'marca': 'BMW',
    'modelo': 'BMW 220 IA TOURER 2.0 turbo active flex',
    'tipo': 'SUV',
    'ano': '2016',
    'quilometragem': 70000,
    'potencia': '2.9',
    'combustivel': 'flex',
    'cor': 'branca',
    'portas': 4,
    'cambio': 'automatico',
    'direcao': 'hidraulica',
}

with open(SAVE_TO, 'w') as file:
    json.dump(carro, file, indent=2, ensure_ascii=False)  # ensure_ascii false exibe caracteres especiais   
    
with open(SAVE_TO, 'r') as file:
    print(json.load(file))