"""Herança Múltipla - Python Orientado a Objetos
Quer dizer que no Python, uma classe pode estender várias outras classes.
Herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança múltipla e mixins
Log -> FileLog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, FileLog)

A, B, C, D
D(B, C) - C(A) - B(A) - A

método -> falar
          A
        /   \
       B     C
        \   /
          D

Python 3 usa C3 superclass linearization
para gerar o mro.
Você não precisa estudar isso (é complexo)
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos
Use o método de classe Classe.mro()
Ou o atributo __mro__ (Dunder - Double Underscore)
"""

"""
Em Python, a herança múltipla permite que uma classe herde atributos e métodos de mais de uma classe pai. Isso significa que uma classe pode ser derivada de várias classes base. No entanto, a herança múltipla pode ser complicada, especialmente quando as classes base possuem métodos ou atributos com o mesmo nome. Para resolver esses conflitos, Python usa a ordem de resolução de método (MRO) para determinar a ordem em que as classes pai são pesquisadas quando ocorre uma referência a um atributo ou método na classe filha.

A MRO é calculada usando o algoritmo C3, que segue três princípios:

    O primeiro princípio é o monotonicidade do C3: a ordem de herança não deve ser alterada na MRO de uma classe caso a ordem das classes base não seja alterada.

    O segundo princípio é o de consistência local: a MRO de uma classe não deve depender da MRO de suas subclasses.

    O terceiro princípio é o da precedência da classe base direta: as classes base diretas devem ter precedência na MRO em relação às classes base indiretas.
"""


class A:
    pass
    def metodo(self):
        print('A')


class B(A):
    pass
    def metodo(self):
        print('B')


class C(A):
    pass
    def metodo(self):
        print('C')


class D(B, C):
    pass
    def metodo(self):
        print('D')


d = D()
d.metodo()
        
print(D.mro())