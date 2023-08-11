"""
Polimorfismo em Python Orientado a Objetos
Polimorfismo é o princípio que permite que classes deridavas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retorno iguais
SO"L"ID
Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclasse sem quebrar a aplicação.
"""
"""
1. Polimorfismo:

Polimorfismo é um conceito da programação orientada a objetos que permite que objetos de diferentes classes sejam tratados de maneira uniforme, como se fossem do mesmo tipo, desde que implementem certos métodos ou comportamentos em comum. Isso promove a reutilização de código, flexibilidade e extensibilidade.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
    

class Cachorro(Animal):
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        return f'woolf'
    

class Gato(Animal):
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        return f'Miau'


def fazer_animal_falar(animal):
    print(f'o {animal.nome} faz {animal.falar()}')


cachorro = Cachorro('cachorro')
gato = Gato('gato')
    
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)


# alternativa mais simples
# class Animal:
#     def falar(self):
#         pass

# class Cachorro(Animal):
#     def falar(self):
#         return "Woof!"

# class Gato(Animal):
#     def falar(self):
#         return "Meow!"

# def fazer_animal_falar(animal):
#     print(animal.falar())

# cachorro = Cachorro()
# gato = Gato()

# fazer_animal_falar(cachorro)  # Saída: "Woof!"
# fazer_animal_falar(gato)  # Saída: "Meow!"


"""
Nesse exemplo, a classe Animal define um método falar, mas não implementa sua funcionalidade. As classes Cachorro e Gato herdam de Animal e implementam o método falar de maneira diferente. A função fazer_animal_falar aceita qualquer objeto do tipo Animal e chama o método falar. Isso ilustra o polimorfismo, pois os objetos são tratados de maneira uniforme, mas o comportamento específico depende da implementação de cada classe.

Ele ilustra polimorfismo de inclusão (ou subtipo), onde as subclasses Cachorro e Gato são tratadas como objetos do tipo Animal na função fazer_animal_falar, permitindo que o mesmo método seja chamado em objetos de diferentes classes que herdam da classe base Animal.

O polimorfismo ocorre porque a função fazer_animal_falar é capaz de aceitar qualquer objeto do tipo Animal (ou uma subclasse de Animal) como argumento, e o método falar do objeto passado é chamado dinamicamente, independentemente de ser um objeto da classe Cachorro ou Gato.

Isso torna o código flexível e reutilizável, permitindo que você adicione mais subclasses de Animal no futuro e continue usando a mesma função fazer_animal_falar sem precisar modificá-la.

Em resumo, seu código é um exemplo válido de polimorfismo, mostrando como as subclasses podem ser tratadas de maneira uniforme como objetos da classe base ou de uma interface comum.
"""

print(20*'*')

"""
2. Assinatura de Métodos:

A assinatura de um método refere-se à combinação de seu nome e parâmetros. Uma linguagem de programação verifica a assinatura de um método para determinar qual implementação específica do método deve ser chamada.
"""


class Calculadora:
    def somar(self, x, y):
        return x + y
    
    def multiplicar(self, x, y):
        return x * y
    
    def dividir(self, x, y):
        return x / y
    
    
calculadora = Calculadora()
res_soma = calculadora.somar(3, 10)
res_mult = calculadora.multiplicar(4, 2)
res_div = calculadora.dividir(15, 3)
print(f'{res_soma}\n{res_mult}\n{res_div}')


"""
Nesse exemplo, a assinatura dos métodos somar, multiplicar e dividir inclui os parâmetros que eles aceitam. O Python verifica a assinatura do método chamado para decidir qual implementação usar.
"""

print(20*'*')

"""
3. Princípio da Substituição de Liskov:

O Princípio da Substituição de Liskov (Liskov Substitution Principle, LSP) é um dos cinco princípios SOLID da programação orientada a objetos. Ele estabelece que os objetos de uma classe derivada devem poder ser substituídos pelos objetos da classe base sem afetar a corretude do programa.
"""


class Forma:
    def calcular_area(self):
        pass
    

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura
        
        
    def calcular_area(self):
        return self.altura * self.largura
    
    
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    
    def calcular_area(self):
        return self.lado * self.lado
    
    
def imprimir_area(res):
    print(f'{res.calcular_area()}')
    

retangulo = Retangulo(3, 8)
quadrado = Quadrado(5)
imprimir_area(retangulo)
imprimir_area(quadrado)

"""
Neste exemplo, a classe Quadrado herda da classe base Forma, assim como a classe Retangulo. As duas subclasses implementam o método calcular_area. A função imprimir_area recebe um objeto Forma (pode ser um Retangulo ou um Quadrado) e chama o método calcular_area para imprimir a área. Isso demonstra o LSP, pois as subclasses podem ser substituídas pela classe base sem causar problemas no comportamento esperado.
"""
class DataBase(ABC):
    @abstractmethod
    def conect_data_base(self):
        pass
    
    @abstractmethod
    def exec_query(self, query):
        pass
    

class MySqlBase(DataBase):
    def conect_data_base(self):
        print('conectando ao banco Mysql')
    
    def exec_query(self, query):
        print(f'Executando: {query}')


class SqLiteBase(DataBase):
    def conect_data_base(self):
        print('conectando ao banco SqLite')
        
    
    def exec_query(self, query):
        print(f'Executando: {query}')
        

def use_data_base(db):
    db.conect_data_base()
    db.exec_query('SELECT * FROM tabela')
    

mysql = MySqlBase()
sqlite = SqLiteBase()
use_data_base(mysql)
use_data_base(sqlite)



# Outro exemplo


class Notification(ABC):
    @abstractmethod
    def notify(self, msg, user):
        pass
    
    
class NotifyEmail(Notification):
    def notify(self, msg, user):
        print(f'send {msg} to {user}')
    
    
class NotfySMS(Notification):
    def notify(self, msg, user):
        print(f'send {msg} to {user}')


if __name__ == '__main__':
    notification = NotfySMS()
    notification.notify('André', 'good luck')