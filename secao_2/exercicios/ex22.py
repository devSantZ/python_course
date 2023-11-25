"""
Exercício - Lista de tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""
import os

lista_de_tarefas = []
lista_de_tarefas_refeitas = []


def limpar():
    return os.system("clear")


def exibir_tarefas():
    if len(lista_de_tarefas) == 0:
        print("Nada para listar")
        return
    for i in lista_de_tarefas:
        print(i)


def desfazer():
    if len(lista_de_tarefas) == 0:
        return
    lista_de_tarefas_refeitas.append(lista_de_tarefas[-1])
    lista_de_tarefas.pop()
    return lista_de_tarefas_refeitas


def refazer():
    if len(lista_de_tarefas) == 0:
        return
    var = lista_de_tarefas_refeitas[-1]
    return lista_de_tarefas.append(var)


if __name__ == "__main__":
    while True:
        print("Comandos: listar, desfazer, refazer")
        entrada_usuario = input("Digite uma tarefa ou comando: ").lower()

        if entrada_usuario == "listar":
            exibir_tarefas()

        elif entrada_usuario == "desfazer":
            desfazer()

        elif entrada_usuario == "refazer":
            refazer()

        elif entrada_usuario == "clear":
            limpar()

        else:
            lista_de_tarefas.append(entrada_usuario)
