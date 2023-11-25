"""
evitando o uso de condicionais
"""

import os

lista_de_tarefas = []
lista_de_tarefas_refeitas = []


def limpar():
    return os.system("clear")


def exibir_tarefas():
    if len(lista_de_tarefas) == 0:
        print("Nada para listar")
    else:
        for i in lista_de_tarefas:
            print(i)


def desfazer():
    if len(lista_de_tarefas) == 0:
        return
    lista_de_tarefas_refeitas.append(lista_de_tarefas.pop())


def refazer():
    if len(lista_de_tarefas_refeitas) == 0:
        return
    lista_de_tarefas.append(lista_de_tarefas_refeitas.pop())


if __name__ == "__main__":
    comandos = {
        "listar": exibir_tarefas,
        "desfazer": desfazer,
        "refazer": refazer,
        "clear": limpar,
        "adicionar": lambda: lista_de_tarefas.append(entrada_usuario),
    }

    while True:
        print("Comandos: listar, desfazer, refazer")
        entrada_usuario = input("Digite uma tarefa ou comando: ").lower()

        if entrada_usuario in comandos:
            comandos[entrada_usuario]()
        else:
            print("Comando inválido")

# res professor

# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return
#
#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()
#
#
# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return
#
#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)
#
#
# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return
#
#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)
#
#
# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)
#
#
# tarefas = []
# tarefas_refazer = []
#
# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')
#
#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()

# if tarefa == 'listar':
#     listar(tarefas)
#     continue
# elif tarefa == 'desfazer':
#     desfazer(tarefas, tarefas_refazer)
#     listar(tarefas)
#     continue
# elif tarefa == 'refazer':
#     refazer(tarefas, tarefas_refazer)
#     listar(tarefas)
#     continue
# elif tarefa == 'clear':
#     os.system('clear')
#     continue
# else:
#     adicionar(tarefa, tarefas)
#     listar(tarefas)
#     continue
