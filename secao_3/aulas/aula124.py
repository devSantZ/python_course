"""
Mantendo estados dentro da classe
Os atributos de instância são variáveis associadas a objetos específicos criados a partir de uma classe. Cada objeto
pode ter seus próprios valores para esses atributos, permitindo que você mantenha estados diferentes para cada instância
da classe.
"""

# Exemplo 1
class Estado:
    def __init__(self, total=1):
        self.total = total

    def incremantar(self, incremento):
        self.total += incremento

v1 = Estado()
v2 = Estado()

v1.incremantar(5)
v1.incremantar(10)
v1.incremantar(100)
print(v1.total)
print(v2.total)


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        self.filmando = True
        print(f'{self.nome} está filmando...')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} está não pode fotografar enquanto filma...')
            return
        print(f'{self.nome} está fotografando...')

    def parar_de_filmar(self):
        if self.filmando:
            print(f'{self.nome} parou de filmar')
            self.filmando = False
            return
        print(f'{self.nome} não está filmando')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.fotografar()