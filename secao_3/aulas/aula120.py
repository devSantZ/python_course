"""
O método __init__ é um método especial em Python que é executado automaticamente quando um objeto é criado a partir de
uma classe. Ele é conhecido como o construtor da classe, pois é responsável por inicializar os atributos do objeto.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("Diego", 22)
print(pessoa1.nome)

class Multiplo:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def mult(self):
        return self.valor1 * self.valor2

teste = Multiplo(10, 5)
print(teste.mult())