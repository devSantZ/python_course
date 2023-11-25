"""
Adiantamento de Funções
"""


def soma(x, y):
    return x + y


def divide(x, y):
    return x / y


def exec(func, y):
    def interna(x):
        return func(x, y)

    return interna


soma_com_cinco = exec(soma, 5)
divide_por_2 = exec(divide, 2)

print(soma_com_cinco(2))
print(divide_por_2(10))
