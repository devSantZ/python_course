class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f"{self.nome} está correndo")


civic = Carro("civic")
civic.acelerar()
