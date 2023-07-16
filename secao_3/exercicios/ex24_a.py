"""
Exercício - Salvando a classe em json
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados.
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
    with open('ex24.json', 'w+') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)


maracana = Estadio('Maracanã', 78.838, 'natural', 'moderno',
                   'Rio de Janeiro', 'marcante')

salvar_classe(maracana.converter())