"""
Problemas dos parametros mutaveis em funções python
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def muda_lista(*args):
    return [x*2 for x in args]

def test(x):
    if x > 5:
        return x

teste = list(filter(test, lista))
print(teste)