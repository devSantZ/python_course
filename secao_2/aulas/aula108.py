"""
filter -  usada para criar um novo iterador (ou uma lista, se convertido), que contém apenas os elementos de uma
sequência que atendem a uma determinada condição. Ela recebe dois argumentos: uma função de filtro e uma sequência.

A função de filtro é uma função que determina se um elemento deve ser incluído ou não na saída. Essa função é aplicada
a cada elemento da sequência e retorna True ou False, indicando se o elemento deve ser mantido ou descartado,
respectivamente.
"""


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


def filtrar_preco(produto):
    return produto["preco"] > 100


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos,
)


print_iter(produtos)
print_iter(novos_produtos)
