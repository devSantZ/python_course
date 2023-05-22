"""
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""
p1 = {
    'nome': 'Diego',
    'sobrenome': 'Santos',
}
# get()
# print('usando "get()"', p1.get('nome', '0'))  # 0 será exibido caso não exista a chave na lista

# pop()
# nome = p1.pop('nome')
# print('usando pop', nome)
# print(p1)

# popitem()
# nome = p1.popitem()
# print('usando "popitem()"', nome)
# print(p1)

# update
p2 = {
    'idade': 21
}
p1.update(p2)
p1.update({
    'raça': 'Pardo',
    'altura': 1.68,
})
print(p1)
    