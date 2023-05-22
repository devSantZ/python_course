"""Shallow copy 'copy()' """
import copy


# Cópia raza 'shallow copy'
a1 = {
    'a1': 1,
    'a2': 2,
}

a2 = a1.copy()
a2['nome'] = 'Diego'
print(f'{a1 = }')
print(f'{a2 = }')

# Cópia profunda 'deepcopy'
b1 = {
    'b1': 1,
    'b2': 2,
    'li': [
        'carro', 'moto', 'barco',
    ]
}
b2 = copy.deepcopy(b1)
b2['b3'] = 3
print(f'{b1 = }')
print(f'{b2 = }')

