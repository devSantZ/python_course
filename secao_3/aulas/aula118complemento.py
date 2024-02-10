# Método 1 hardcode
class Computador:
    def __init__(self):
        self.marca = "apple"
        self.memoria = "8gb"
        self.placadevideo = "redeon"


computador1 = Computador()
print(computador1.marca)


# Metodo 2
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("Carlos", 29)
print(pessoa1.nome, pessoa1.idade)


# Metodo 3
class Carro:
    pass


car1 = Carro()
car1.marca = "Ford"
car1.modelo = "Ranger"

print(car1.marca, car1.modelo)

