"""
Introdução à List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""
lista = [i for i in range(10)]
print(lista)


def mult(x=1, y=0):
    valores = [i * x for i in range(y)]
    return valores


teste = mult(3, 10)
print(teste)
