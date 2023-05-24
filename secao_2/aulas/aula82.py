"""
list comprehension com mais de um for
"""

lista = []
for x in range(4):
    for y in range(4):
        lista.append((x, y))
print(lista)

#usando list comprehension
lista2 = [(x, y)for x in range(4) for y in range(4)]
print(lista2)
