"""
recuperando os valores da classe com um arquivo json
"""
import json
from ex24_a import SAVE_TO, Estadio


def recuperar_json(i):
    with open(SAVE_TO, 'r') as file:
        data = json.load(file)
        estadio = Estadio(**data[i])
    return estadio


print(recuperar_json(1).nome)

