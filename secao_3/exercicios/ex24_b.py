"""
recuperando os valores da classe com um arquivo json
"""
import json
from ex24_a import SAVE_TO, Estadio


def recuperar_json():
    with open(SAVE_TO, 'r') as file:
        data = json.load(file)
        return data


test = Estadio(**recuperar_json())
print(test.nome)