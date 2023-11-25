"""
O dictionary comprehension, ou compreensão de 
dicionário, é uma construção do Python que permite
criar dicionários de forma concisa e eficiente, 
utilizando uma sintaxe compacta.
sintaxe básica:
{chave: valor for item in iterável}
    chave: é a expressão que define a chave pra
    cada par de chave-valor
    valor: expressão que define o valor
    correspondente
    iterável: sequẽncia de elementos no qual os
    pares chave-valor serão gerados
"""

# Quadrado dos valores
numeros = [1, 2, 3, 4, 5]
quadrados = {x: x**2 for x in numeros}
print(quadrados)  # -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Quadrado dos valores caso o valor seja par
pares = {x: x**2 for x in numeros if x % 2 == 0}
print(pares)  # -> {2: 4, 4: 16}


produtos = {
    "nome": "televisão",
    "marca": "samsung",
    "preco": 2700,
}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produtos.items()
}

print(dc)  # -> {'nome': 'TELEVISÃO', 'marca': 'SAMSUNG', 'preco': 2700}
