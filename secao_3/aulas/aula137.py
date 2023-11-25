"""
Herança simples - Relações entre classes
Associação - usa, Agregação - tem
Composição - É dono de, Herança - É um

Herança vs Composição

Classe principal (Pessoa)
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""


# class Foo(object):
#   def __init__(self):
#     pass

# help(Foo)


class Pessoa:
    cpf = "312.591.944-21"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_da_classe(self):
        print(f"{self.__class__.__name__}: {self.nome} {self.sobrenome}")


class Cliente(Pessoa):
    cpf = 3212
    pass


class Aluno(Pessoa):
    pass


c1 = Cliente("Carlos", "Costa")
c1.falar_nome_da_classe()
a1 = Aluno("Maria", "Pinheiro")
a1.falar_nome_da_classe()
print(f"{c1.cpf}\n{a1.cpf}")
# help(Cliente)

"""
class Cliente(Pessoa)
 |  Cliente(nome, sobrenome)
 |  
 |  Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object
 |  
 |  Methods inherited from Pessoa:
 |  
 |  __init__(self, nome, sobrenome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  falar_nome_da_classe(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Pessoa:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
"""
