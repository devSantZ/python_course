"""
Args - Argumentos nomeados
* - *args - (empacotamento e desempacotamento)
args empacota o que eu enviar pra função dentro
de uma tupla
"""

# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4, 5

print(x, y, resto)


def soma(*args):
    somando = sum(args)
    return somando
    # argumentos = 0
    # for i in args:
    #     argumentos += i
    # return argumentos


soma1 = soma(3, 4, 1, 8)
print(soma1)
