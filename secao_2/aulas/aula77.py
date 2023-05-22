"""
ainda sobre funções lambdas
"""


def executa(funcao, *args):
    """
    executa a função lambda quando chamada
    """
    return funcao(*args)


triplica = executa(
    lambda x: x*4,
    4,
)
print(triplica)

negativo = executa(
    lambda x: 'positivo' if x >= 0 else 'negativo',
    -3
)
print(negativo)

lista = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x*2, lista))
print(dobro)

par = executa(
    lambda x: x % 2 == 0,
    73643661
)
print(par)