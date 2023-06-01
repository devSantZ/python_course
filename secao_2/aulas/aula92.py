"""
yiel from
a expressão yield from é usada para delegar a execução
de um gerador para outro gerador, permitindo a criação
de uma cadeia de iterações. É especialmente útil quando
você tem geradores aninhados ou precisa extrair valores
de um gerador interno sem precisar iterar manualmente 
sobre ele.
"""

def gerador_1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 'gen 1'
    
def gerador_2(parm):
    yield from gerador_1()
    yield 5
    yield 6
    yield 7
    yield 'gen 2'
    
# g1 = gerador_1()
# for i in g1:
#     print(i)
# print()

g2 = gerador_2(gerador_1)
for i in g2:
    print(i)
print()



# Exemplo
def gerador_interno():
    for i in range(1, 4):
        yield i

def gerador_externo():
    yield from gerador_interno()
    yield 'Final'

for valor in gerador_externo():
    print(valor)
