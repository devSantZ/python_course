"""
copy, sorted, produtos.sort
Exercícios
() Gere novos_produtos por deep copy (cópia profunda)
Ordene os produtos por nome decrescente (do maior para menor)
Ordene os produtos por preco crescente (do menor para maior)
"""
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# (x) Aumente os preços dos produtos a seguir em 10% 
def acrescenta_10_por_cento():
    novos_produtos = [
        {**produto, 'preco': round(produto['preco'] * (1 + 10/ 100), 2)} 
        for produto in produtos
    ]
    return novos_produtos


# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
def ordena_por_nome():
    produtos_ordenados_por_nome = []
    for i in produtos:
        produtos_ordenados_por_nome.append(i['nome'])
        produtos_ordenados_por_nome = copy.deepcopy(produtos_ordenados_por_nome)
    return sorted(produtos_ordenados_por_nome)


# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
def ordena_por_preco():
    produtos_ordenados_por_preco = []
    for i in produtos:
        produtos_ordenados_por_preco.append(i['preco'])
    return sorted(produtos_ordenados_por_preco)



if __name__ == "__main__":
    aumenta_preco = acrescenta_10_por_cento()
    ordena_nome = ordena_por_nome()
    ordena_preco = ordena_por_preco()
    print(
          f'{aumenta_preco}\n'
          f'{ordena_nome}\n'
          f'{ordena_preco}\n'
)