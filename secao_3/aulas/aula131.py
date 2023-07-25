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
        return self.value ** pot

    @property
    def cube(self, pot=3):
        return self.value ** pot


caneta = Caneta('Preto')
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
        return 3.14 * self._radius ** 2

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
@<nome_do_atributo>.getter:
O decorador @<nome_do_atributo>.getter é usado para criar um método que será usado como o getter (obtenção) para um 
atributo específico. Isso permite adicionar lógica personalizada ao obter o valor do atributo.
"""


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.getter
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Criando uma temperatura com 25 graus Celsius
temp = Temperature(25)

# Acessando a temperatura em Celsius usando o getter personalizado
print(temp.celsius)  # Saída: 25

# Acessando a temperatura em Fahrenheit diretamente como uma propriedade
print(temp.fahrenheit)  # Saída: 77.0

# Neste exemplo, usamos o @celsius.getter para definir um getter personalizado para a propriedade celsius. Isso nos
# permite adicionar lógica de conversão quando o valor em Celsius é obtido.
