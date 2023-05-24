"""
filtro de dados em list comprehension

Em Python, a função filter() é uma função embutida 
que permite filtrar elementos de uma sequência
(como uma lista, tupla ou conjunto) com base em uma
determinada condição. Ela retorna um iterador 
contendo apenas os elementos da sequência que 
atendem à condição especificada.

sintaxe basica: filter(função, sequẽncia)

    função: É a função que define a condição pela 
    qual os elementos são filtrados. Essa função 
    deve retornar True ou False com base em alguma 
    lógica ou condição aplicada a cada elemento da
    sequência.
    sequência: É a sequência de elementos que você 
    deseja filtrar.

A função filter() percorre cada elemento da sequência
e aplica a função especificada a cada elemento. Se a
função retornar True, o elemento é incluído no 
resultado; caso contrário, é excluído.
"""


def func(x):
    if len(x)>5:
        return x
        
lista = ['Diego', 'Jão', 'nomemuitogrande', 'i']
filtro = list(filter(func, lista))

print(filtro)


def maior_que_cinco(x):
    return x > 5

numeros = [2, 8, 5, 10, 1, 6]
resultado = filter(maior_que_cinco, numeros)

for num in resultado:
    print(num)
