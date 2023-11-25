"""
Em Python, a função reduce() faz parte do módulo functools e é usada para aplicar uma função a uma sequência de
elementos, reduzindo-a a um único valor. A função reduce() recebe dois argumentos: a função que será aplicada
cumulativamente e a sequência de elementos.

"""
from functools import reduce


produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


def soma(x, y):
    return x + y


total = reduce(soma, [x["preco"] for x in produtos])
print(round(total))
