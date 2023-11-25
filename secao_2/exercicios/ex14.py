"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
"""


def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total


def par(*args):
    numeros_pares = []
    numeros_impares = []
    for i in args:
        if i % 2 == 0:
            print(f"{i} é par")
            numeros_pares.append(i)
        else:
            print(f"{i} é impar")
            numeros_impares.append(i)
    return f"NUMEROS PARES = {numeros_pares}\nNUMEROS IMPARES = {numeros_impares}"


conta1 = multiplica(1, 2, 3, 4, 10)
print(conta1)
par_impar = par(1, 2, 3, 4, 5, 6)
print(par_impar)
