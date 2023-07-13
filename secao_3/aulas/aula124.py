"""
Mantendo estados dentro da classe
"""

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