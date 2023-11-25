"""
manipulando chaves e valores de um dicionário
"""
# CRUD
pessoa = {}

# Criando uma nova chave/valor
pessoa["nome"] = "Diego"
pessoa["sobrenome"] = "Santos"
pessoa["idade"] = 21

# Acessando chaves
print(pessoa)
print(pessoa["nome"])
print(pessoa["idade"])

# Editando chaves
chave_dinamica = "peso"
pessoa[chave_dinamica] = 62
print(pessoa[chave_dinamica])

# Apagando chaves
del pessoa[chave_dinamica]
print(pessoa)

if not pessoa.get(chave_dinamica) is None:
    print(pessoa[chave_dinamica])
else:
    print("Essa chave não exite!")
