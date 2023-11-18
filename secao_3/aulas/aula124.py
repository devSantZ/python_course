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

    def incrementar(self, incremento):
        self.total += incremento

v1 = Estado()
v2 = Estado()

v1.incrementar(5)
v1.incrementar(10)
v1.incrementar(100)
print(v1.total)
print(v2.total)


class Camera:
    def __init__(self, nome, estado=False):
        self.nome = nome
        self.estado = estado
        
        
    def filmar(self):
        if self.estado:
            print(f'{self.nome} já está filmando')
            return
        self.estado = True
        print(f'{self.nome} está filmando')
    
    
    def parar_de_filmar(self):
        if self.estado:
            print(f'{self.nome} está parando de filmar')
            self.estado = False
            return
        print(f'{self.nome} não está filmando')
        
        
    def fotografar(self):
        if not self.estado:
            print(f'{self.nome} está fotografando')
            return
        print(f'{self.nome} nao pode fotografar enquanto filma')
        

cam1 = Camera('Nokia')
cam1.filmar()
cam1.filmar()
cam1.fotografar()
cam1.parar_de_filmar()
cam1.fotografar()