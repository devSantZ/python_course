"""
recuperando os valores da classe com um arquivo json
"""
import json


class Estadio:
    def __init__(self, nome, capacidade, gramado, estrutura,
                 localizacao, arquitetura):
        self.nome = nome
        self.capacidade = capacidade
        self.gramado = gramado
        self.estrutura = estrutura
        self.localizacao = localizacao
        self.arquitetura = arquitetura


def recuperar_json():
    with open('ex24.json', 'r') as file:
        data = json.load(file)
        return data


test = Estadio(**recuperar_json())
print(test.nome)