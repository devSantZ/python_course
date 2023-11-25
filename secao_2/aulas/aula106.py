"""
groupby - Agrupando valores
"""
from itertools import groupby

alunos = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Letícia", "nota": "B"},
    {"nome": "Fabrício", "nota": "A"},
    {"nome": "Rosemary", "nota": "C"},
    {"nome": "Joana", "nota": "D"},
    {"nome": "João", "nota": "A"},
    {"nome": "Eduardo", "nota": "B"},
    {"nome": "André", "nota": "A"},
    {"nome": "Anderson", "nota": "C"},
]

ordena = lambda x: x["nota"]

alunos_agrupado = sorted(alunos, key=ordena)
grupo_por_nota = groupby(alunos_agrupado, key=ordena)

for nota, grupo in grupo_por_nota:
    print(10 * "+")
    print(f"alunos com nota {nota}", sep="\n")
    for aluno in grupo:
        print(f'nome: {aluno.get("nome")}')


# Lista de pessoas
pessoas = [
    {"nome": "João", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Ana", "idade": 27, "cidade": "Rio de Janeiro"},
    {"nome": "Lucas", "idade": 22, "cidade": "São Paulo"},
]

# Ordenar a lista pelo campo 'cidade'
pessoas.sort(key=lambda x: x["cidade"])

# Agrupar as pessoas por cidade
grupos = groupby(pessoas, key=lambda x: x["cidade"])

# Iterar sobre cada grupo
for cidade, grupo in grupos:
    print(f"Cidade: {cidade}")
    print("Pessoas:")
    for pessoa in grupo:
        print(pessoa["nome"], pessoa["idade"])
    print()
