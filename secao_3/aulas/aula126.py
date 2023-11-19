"""
__dict__ e vars para atributos da instancia
"""
from abc import abstractmethod
import os
import json


BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'auladadospessoa.json')


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    
    @abstractmethod
    def save_to_jason(data):
        with open(SAVE_TO, 'w', encoding='utf-8') as file:
            json.dump(data, file)



dados = {'nome': 'Diego', 'sobrenome': 'Santos', 'idade': 22}
p1 = Pessoa(**dados)
Pessoa.save_to_jason(vars(p1))
print(vars(p1))



print(p1.__dict__)
print(vars(p1))
p1.__dict__['partimonio'] = 21000000
