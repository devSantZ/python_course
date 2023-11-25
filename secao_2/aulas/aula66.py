"""
retorno das funções (return)
por padrão, as funções rotornam None
"""


def soma(x, y):
    if x > 10:
        return f"{x=}"
    return x + y


soma1 = soma(123, 4)
print(soma1)
