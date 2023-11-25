# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._marca = None
        self._transmissao = None
        self._direcao = None
        self.motor = []

    def exibir_caracteristicas(self, motor):
        print(
            f"nome: {self.nome}\n"
            f"marca: {self.marca}\n"
            f"trasmissão: {self.transmissao}\n"
            f"direção: {self.direcao}\n"
            f"motor: {Motor.caracter_motor(motor)}"
        )

    def insert_motor(self, potencia, cilindros):
        self.motor.append(Motor(potencia, cilindros))

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def transmissao(self):
        return self._transmissao

    @transmissao.setter
    def transmissao(self, transmissao):
        self._transmissao = transmissao

    @property
    def direcao(self):
        return self._direcao

    @direcao.setter
    def direcao(self, direcao):
        self._direcao = direcao


class Motor:
    def __init__(self, pontencia, cilindros):
        self.pontencia = pontencia
        self.cilindros = cilindros

    def caracter_motor(self):
        return f"{self.cilindros, self.pontencia}"


class Fabrincante:
    def __init__(self, fabricante):
        self.fabricante = fabricante


fabricante1 = Fabrincante("Mercedes")
motor1 = Motor("150 cv", "4 em linha")
carro1 = Carro("Mercedes Benz Classe C")
carro1.marca = fabricante1.fabricante
carro1.transmissao = "Automático de 9 marchas"
carro1.direcao = "Elétrica"
carro1.exibir_caracteristicas(motor1)
print()
fabricante2 = Fabrincante("BMW")
motor2 = Motor("600 cv", "4")
carro2 = Carro("M5 Series")
carro2.marca = fabricante2.fabricante
carro2.transmissao = "5 manuais"
carro2.direcao = "Manual"
carro2.exibir_caracteristicas(motor2)
print()
fabricante3 = Fabrincante("Fiat")
motor3 = Motor("100 cv", "4 em Linha")
carro3 = Carro("Uno Mille Fire  ")
carro3.marca = fabricante3.fabricante
carro3.transmissao = "5 manuais"
carro3.direcao = "Manual"
carro3.exibir_caracteristicas(motor3)
