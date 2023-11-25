"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo do Python de fazer coisas
@property é uma propriedade do objeto, ela
é um método que se comporta como um
atributo
Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Código cliente - é o código que usa seu código

Em Python, o decorador @property e o decorador @<nome_do_atributo>.getter são usados para criar propriedades de classe
que permitem controlar o acesso e a obtenção de valores de atributos de maneira mais pythonica. Eles são usados para
tornar o código mais legível, encapsulado e facilitar a manutenção, permitindo que você adicione lógica personalizada ao
acessar ou obter o valor de um atributo.
"""


class Caneta:
    def __init__(self, cor):
        self.cor = cor

    # Getter
    @property
    def get_cor(self):
        return self.cor


class Pontecension:
    def __init__(self, value):
        self.value = value

    @property
    def square(self, pot=2):
        return self.value**pot

    @property
    def cube(self, pot=3):
        return self.value**pot


caneta = Caneta("Preto")
print(caneta.get_cor)

n1 = Pontecension(5)
print(n1.cube, n1.square)


# Extras
"""
@property:
O decorador @property é usado para transformar um método de uma classe em uma propriedade. Quando você usa esse 
decorador, você pode acessar o método como se fosse um atributo de instância, sem a necessidade de chamar explicitamente
o método.
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius**2

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius


# Criando um círculo com raio 5
my_circle = Circle(5)

# Acessando o raio como uma propriedade, embora esteja implementado como um método
print(my_circle.radius)  # Saída: 5

# Acessando a área e a circunferência também como propriedades
print(my_circle.area)  # Saída: 78.5
print(my_circle.circumference)  # Saída: 31.4

# Neste exemplo, usamos o @property para criar propriedades radius, area e circumference na classe Circle. Embora elas
# sejam métodos, podemos acessá-las diretamente como propriedades, o que torna o código mais legível.

"""
Vamos explicar em mais detalhes o uso do @property para criar getters personalizados:

Em Python, o @property é um decorador que permite transformar um método em uma propriedade, permitindo que você acesse o
 método como se fosse um atributo de instância, em vez de precisar chamá-lo explicitamente como um método.

O benefício do @property é que ele permite adicionar lógica personalizada durante o acesso ao atributo, sem que o 
usuário do objeto precise saber que por trás há um método executando.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value


# Criando um retângulo
rectangle = Rectangle(5, 3)

# Acessando os atributos como propriedades
print(rectangle.width)  # Saída: 5
print(rectangle.height)  # Saída: 3

# Acessando a área como uma propriedade (não precisa chamar como método)
print(rectangle.area)  # Saída: 15

# Alterando o valor da largura através do setter
rectangle.width = 10
print(rectangle.width)  # Saída: 10

# Tentando atribuir um valor negativo (o setter lançará um ValueError)
rectangle.height = -2  # Isso lançará um ValueError

# Neste exemplo, criamos a classe Rectangle com os atributos _width e _height, e definimos os getters usando o decorador
# @property. Isso permite que width e height sejam acessados como propriedades diretamente. Também implementamos os
# setters personalizados usando o decorador @<nome_do_atributo>.setter para adicionar validações de valores negativos.

# Usar o @property para criar getters personalizados é uma prática comum em Python quando queremos adicionar lógica de
# validação, cálculos ou manipulação de dados em atributos de classe. Isso torna o código mais legível, encapsulado e
# menos suscetível a erros de uso.
