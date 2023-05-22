"""Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""
computador = {
    'placa mãe': 'B650m',
    'processador': 'ryzen 5 7600hs',
    'ram': '16gb',
    'placa de video': 'RTX 3090ti',
    'perifericos': [
        {'mouse': 'logitech g pro'},
        {'teclado': 'redragon K617'},
        {'headset': 'havit h2002d'},
    ],
}

# len()
quantidade_de_chaves = len(computador)
print(quantidade_de_chaves)

# keys()
chaves = computador.keys()
print(list(chaves))

# values()
valores = computador.values()
print(list(valores))

# items()
itens = computador.items()
print(list(itens))
for chave, valor in computador.items():
    print(f'{chave}: {valor}')

# setdefault()
valor_padrao = computador.setdefault('monitor', 'sem monitor')
print(valor_padrao)
