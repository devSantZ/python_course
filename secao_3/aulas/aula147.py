"""
__repr__(self):
O método __repr__ é responsável por fornecer uma representação não ambígua do objeto, preferencialmente uma que possa ser usada para recriar o objeto. Essa representação é voltada para desenvolvedores e é retornada quando a função repr() é chamada sobre o objeto. A ideia é que a representação retorne um formato que, se passado de volta para eval(), crie um objeto equivalente.
"""


from typing import Any


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # __repr__ deve retornar uma string
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f"{class_name}('{self.nome}', {self.idade})"

pessoa = Pessoa("Alice", 30)
print(repr(pessoa))  # Saída: Pessoa('Alice', 30)


"""
__str__(self):
O método __str__ é responsável por fornecer uma representação legível do objeto como uma string. Essa representação é voltada para os usuários finais e é retornada quando a função str() é chamada sobre o objeto. É uma representação mais amigável e geralmente menos detalhada do que a retornada por __repr__.
"""



class Pessoa2:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def __str__(self) -> str:
        return f'{self.nome} tem {self.idade} anos'
    
    
pessoa2 = Pessoa2('Carlos', 23)
print(str(pessoa2))



# Extras
class Ponto:
    def __init__(self, x:int, y:int, z:str) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self) -> str:
        return f'({self.x, self.y}, {self.z})'
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.x!r}, {self.y!r}, {self.z!r})"
        


p1 = Ponto(2, 42, 94)
print(f'{p1!r}')
# print(f'{p1!s}')