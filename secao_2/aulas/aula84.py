"""
Set comprehension, ou compreensão de conjunto, é 
uma construção do Python que permite criar conjuntos
de forma concisa e eficiente, utilizando uma sintaxe
compacta.
A estrutura básica de um set comprehension é 
semelhante à do dictionary comprehension, mas sem 
especificar pares chave-valor.
sintaxe básica:
{expressão for item in iterável}
    expressão: representa a expressão que define cada 
    elemento do conjunto resultante.
    item:representa cada elemento do iterável.
    iterável: é a sequência de elementos da qual os 
    elementos do conjunto serão gerados.
"""
# ex1
conjunto = {x**2 for x in range(10) if x % 2 == 0}
print(conjunto)  # -> {0, 4, 16, 36, 64}


# ex2
numeros = [1, 2, 3, 4, 5]
quadrados = {x**2 for x in numeros}
print(quadrados)  # -> {1, 4, 9, 16, 25}


# ex3
numeros = [1, 2, 3, 4, 5]
pares = {x for x in numeros if x % 2 == 0}
print(pares)  # -> {2, 4}
