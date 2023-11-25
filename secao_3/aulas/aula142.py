"""
abstractmethod para qualquer método já decorado (@property e setter)
É possível criar @property @property.setter @classmethod
@staticmethod e métodos normais como abstratos, para isso
use @abstractmethod como decorator mais interno.
Foo - Bar são palavras usadas como placeholder
para palavras que podem mudar na programação.

"""


from abc import ABC, abstractmethod


class AbstactFoo(ABC):
    def __init__(self, nome):
        self._nome = nome

    @property
    # @abstractmethod
    def nome(self):
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        ...


class Foo(AbstactFoo):
    def __init__(self, nome):
        super().__init__(nome)

    # @property
    # def nome(self):
    #     return self._nome

    # @nome.setter
    # def nome(self, nome):
    #     self.nome = nome

    @AbstactFoo.nome.setter
    def nome(self, nome):
        self._nome = nome


foo = Foo("Bar")
print(foo.nome)
