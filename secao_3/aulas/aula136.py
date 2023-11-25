"""
Composição é um conceito importante na Programação Orientada a Objetos que permite que uma classe contenha objetos de
outras classes como seus atributos. Essa relação é frequentemente chamada de "tem-um" (has-a), pois a classe principal
"tem" objetos de outras classes. A composição é usada para criar objetos complexos construindo-os a partir de objetos
mais simples e reutilizáveis.
"""


# Composição
class Client:
    def __init__(self, name):
        self.name = name
        self.adress = []

    def insert_adrees(self, road, number):
        self.adress.append(Adress(road, number))

    def insert_external_adrees(self, external_adree):
        self.adress.append(external_adree)

    def list_adress(self):
        for ad in self.adress:
            print(ad.road, ad.number)


class Adress:
    def __init__(self, road, number):
        self.road = road
        self.number = number


client1 = Client("Diego")
client1.insert_adrees("Av. Principal", 12)
client1.insert_adrees("Av. Santana", "S/N")
endereco_externo = Adress("Rua Sitio", 31)
client1.insert_external_adrees(endereco_externo)
client1.list_adress()
