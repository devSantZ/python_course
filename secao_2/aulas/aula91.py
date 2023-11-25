"""
Introdução às Generator functions em Python
Generator functions são funções que podem pausar
"""


def gerador(n=0):
    yield 1
    print("oi y1")
    yield 2
    print("oi y2")
    yield 3
    print("oi y3")
    return f"{n}, acabouu"


gen = gerador(2)
# print(next(gen)) # -> Primeiro yield
# print(next(gen)) # -> Segundo yield
# print(next(gen)) # -> Terceiro yield
# print(next(gen)) # -> StopIteration

"""
Basicamente o next() chama a próxima iteração até
que não exista mais um iterável, exatamente o que
faz o laço for.   
"""

for i in gen:
    print(i)


# Exemplo 1
def func_generator(*args):
    while True:
        yield args
        break


ex = func_generator("oi", "pedro", "arthur")
for i in ex:
    print("\n".join(i))


# Exemplo 2
def generator_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


lista_par = []
numeros = generator_pares(20)

for numero_par in numeros:
    lista_par.append(numero_par)
print(lista_par)
