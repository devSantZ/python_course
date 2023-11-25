"""
mapeamento de dados
O mapeamento de dados em Python refere-se ao processo de
transformar uma coleção de dados em uma estrutura diferente,
seja para reorganizar os dados, filtrá-los, ou para executar
operações específicas neles.
a funçao map() retorna pro padrão o tipo map, que pode ser 
convertido.
Função map(): A função map() em Python aplica uma função a 
cada elemento de uma sequência (por exemplo, uma lista) e 
retorna um iterador que contém os resultados. Você pode 
fornecer uma função embutida ou definir sua própria função 
para mapear os dados.
sintaxe básica: map(função, sequência)
"""
# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6]
quadrado = [numero**2 for numero in numeros]
print(f"{numeros = }\n{quadrado = }")  # -> numeros = [1, 2, 3, 4, 5, 6]
#                                          quadrado = [1, 4, 9, 16, 25, 36]


# Exemplo 2
def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperatura = [24, 32, -4, 15]
fahrenheit = list(map(converter_celsius_para_fahrenheit, temperatura))
print(fahrenheit)  # -> [75.2, 89.6, 24.8, 59.0]


# Usando map() para transformar os itens em strings
temperatura_duplicada = list(map(str, temperatura))
print(temperatura_duplicada)  # -> ['24', '32', '-4', '15']


# Soma de valores de uma lista
def soma_listas(*args):
    return sum(args)


lista_numero_1 = [3, 5, 1, 54, 2]
lista_numero_2 = [1, 4, 2, 6, 12]
numeros_somados = list(map(soma_listas, lista_numero_1, lista_numero_2))
print(numeros_somados)  # -> [4, 9, 3, 60, 14]

produtos = [
    {"nome": "Sabão", "preco": 12},
    {"nome": "Vassoura", "preco": 17},
    {"nome": "Biscoito", "preco": 2.50},
    {"nome": "Queijo", "preco": 32},
    {"nome": "Refrigerante", "preco": 8},
]

novos_produtos = [
    {**produto, "preco": round(produto["preco"] * 1.05, 2)}
    if produto["preco"] > 20
    else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep="\n")
