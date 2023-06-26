"""             PERMUTATIONS
O método permutations do módulo itertools em Python é uma
função que retorna todas as permutações possíveis de um dado
conjunto de elementos. Ele produz todas as combinações possíveis
dos elementos, levando em consideração a ordem dos mesmos.
sintaxe: permutations(iterable, r=None) #r é o tamanho da permutação
===============================================================
                COMBINATIONS
O método combinations do módulo itertools em Python é uma função que
gera todas as combinações possíveis de um dado conjunto de elementos,
sem repetições. Ele produz todas as combinações únicas dos elementos,
independentemente da ordem em que eles aparecem.
sintaxe: combinations(iterable, r) # o tamanho é um parâmetro obrigatório
===============================================================
                PRODUCT
O método product do módulo itertools em Python é uma função que retorna o
produto cartesiano de um ou mais iteráveis. O produto cartesiano é uma
combinação de todos os elementos dos iteráveis, gerando todas as possíveis
combinações dos elementos.
sintaxe: product(*iterables, repeat=1) # repeat (opcional): É o número de
vezes que cada elemento dos iteráveis será repetido.
"""

from itertools import permutations, combinations, product

pessoas = [
    ['João', 'Marcos', 'Caio', 'Diego'],
    ['Maria', 'Luana', 'Isa', 'Marta'],
    ['Noite', 'Dia']
]

lista = ['Ana', 'Pedro', 'João', 'Caio', 'Marcio']

# Permutation
print('Permutação')
print(*list(permutations(lista, 2)), sep='\n')

# Combination
print('Combinação')
print(*list(combinations(lista, 2)), sep='\n')

# Product
print('Product')
print(*list(product(*pessoas)), sep='\n')