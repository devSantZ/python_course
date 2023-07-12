"""
Escopo e métodos da classe
"""
#
# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
#         var = 'Qualquer coisa'
#         print(var)  # O print é executado assim que a classe é instanciada
#
# animal1 = Animal('Cachorro')
# print(animal1.nome)

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self, comida):
        return f'{self.nome} está comendo {comida}'

    # def executar(self, *args, **kwargs):
    #     return self.comer(*args, **kwargs)

animal1 = Animal('Urso')
print(Animal.comer(animal1,'Foca'))
# print(Animal.executar(animal1,'Foca'))