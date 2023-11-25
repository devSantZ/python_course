"""
Classes abstratas - Abstract Base Class (abc)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes
a criarem métodos concretos. Também podem ter
métodos concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos
abstratos é que elas NÃO PODEM ser instânciadas
diretamente.
Métodos abstratos DEVEM ser implementados
nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse
sendo ABCMeta.
É possível criar @property @setter @classmethod
@staticmethod e @method como abstratos, para isso
use @abstractmethod como decorator mais interno.
"""
from abc import ABC, abstractmethod


# class Log(metaclass=ABCMeta)
class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f"error: {msg}")

    def log_success(self, msg):
        return self._log(f"success: {msg}")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} | {self.__class__.__name__}")


l = LogPrintMixin()
l.log_success("hello")

"""
1. Classe Abstrata e Métodos Abstratos:

Uma classe abstrata define um contrato básico que suas subclasses devem cumprir. Ela pode conter métodos abstratos, que são métodos declarados, mas não implementados na classe abstrata. As subclasses são obrigadas a implementar esses métodos.
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius**2, 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)


circulo = Circle(8)
print(circulo.area())

quadrado = Square(14)
print(quadrado.area())


class Calc(ABC):
    @abstractmethod
    def operation(self):
        pass


class Division(Calc):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def operation(self):
        return round(self.n1 / self.n2, 2)


class Multiplication(Calc):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def operation(self):
        return round(self.n1 * self.n2, 2)


class Subtraction(Calc):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def operation(self):
        return round(self.n1 - self.n2, 2)


class Addition(Calc):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def operation(self):
        return round(self.n1 + self.n2, 2)


div = Division(10, 2)
mul = Multiplication(4, 5)
sub = Subtraction(15, 5)
add = Addition(8, 2)
print(f"{div.operation()}\n{mul.operation()}\n{sub.operation()}\n{add.operation()}\n")
