"""
Exercício - Salvando a classe em json
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados.
"""
import json
import os

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'ex24.json')


class Estadio:
    def __init__(self, nome, capacidade, gramado, 
                 estrutura, localizacao, arquitetura):
        self.nome = nome
        self.capacidade = capacidade
        self.gramado = gramado
        self.estrutura = estrutura
        self.localizacao = localizacao
        self.arquitetura = arquitetura

    def converter(self):
        return {
            'nome': self.nome,
            'capacidade': self.capacidade,
            'gramado': self.gramado,
            'estrutura': self.estrutura,
            'localizacao': self.localizacao,
            'arquitetura': self.arquitetura,
        }


def salvar_classe(info):
    with open(SAVE_TO, 'w') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)


maracana = Estadio('Maracanã', 78.838, 'natural', 'moderno',
                   'Rio de Janeiro', 'marcante')
pacaiambu = Estadio('Pacaiambu', 40.199, 'conservado, natural', 'tradicional',
                   'São Paulo', 'clássica')
estadios = [vars(maracana), vars(pacaiambu)]

if __name__ == '__main__':
    salvar_classe(estadios)