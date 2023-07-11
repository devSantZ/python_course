"""
salvando tarefas em um arquivo json
"""

import os
import json

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'lista_tarefa.json')

lista_de_tarefas = []
lista_de_tarefas_refeitas = []

def limpar():
    return os.system('clear')


def exibir_tarefas():
    if len(lista_de_tarefas) == 0:
        print('Nada para listar')
    else:
        for i in lista_de_tarefas:
            print(i)


def desfazer():
    if len(lista_de_tarefas) == 0:
        return
    lista_de_tarefas_refeitas.append(lista_de_tarefas.pop())
    with open(SAVE_TO, 'r') as file:
        data = json.load(file)
        x = data.pop()
        return x


def refazer():
    if len(lista_de_tarefas_refeitas) == 0:
        return
    lista_de_tarefas.append(lista_de_tarefas_refeitas.pop())


def salvar_em_json():
    with open(SAVE_TO, 'w') as file:
        return json.dump(lista_de_tarefas, file, indent=2)


if __name__ == '__main__':
    comandos = {
        'listar': exibir_tarefas,
        'desfazer': desfazer,
        'refazer': refazer,
        'clear': limpar,
    }

    while True:
        salvar_em_json()
        print('Comandos: listar, desfazer, refazer, salvar')
        entrada_usuario = input('Digite uma tarefa ou comando: ').lower()

        if entrada_usuario in comandos:
            comandos[entrada_usuario]()
        else:
            lista_de_tarefas.append(entrada_usuario)

