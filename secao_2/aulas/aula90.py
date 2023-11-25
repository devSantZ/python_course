"""
iterables e iterators

iteravel: Um objeto iterável é aquele que pode ser percorrido,
    ou seja, você pode obter um iterador a partir dele. Em termos 
    simples, um iterável é uma sequência de elementos que pode ser
    iterada (percorrida) um a um. Exemplos comuns de iteráveis em 
    Python incluem listas, tuplas, strings, dicionários e conjunto.
    
iterador: Um iterador é um objeto que representa um estado de 
    iteração sobre um iterável. Ele mantém uma referência para o 
    elemento atual em uma sequência e sabe como acessar o próximo 
    elemento. Em Python, um iterador é implementado por meio 
    de dois métodos: __iter__() e __next__(). O método __iter__() 
    retorna o próprio objeto iterador, enquanto o método 
    __next__() retorna o próximo elemento da sequência.
"""
import sys


lista = [i for i in range(1000)]
gerador = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(gerador))


def iterador(x):
    iterador_x = iter(x)
    while x:
        try:
            print(next(iterador_x))
            continue
        except StopIteration:
            return


lista = [1, 2, 3, 4, 5, 6]
tupla = ("Diego", 3, 5, True, 2.4, "Python")
dicionario = {
    "nome": "Lucas",
    "sobrenome": "Santos",
    "idade": 32,
    "endereco": [{"rua1": "Nomer1", "rua2": "Nomer2"}],
}

teste = iterador(lista)
print(teste)

teste2 = iterador(tupla)
print(teste2)

teste3 = iterador(dicionario)
print(teste3)
