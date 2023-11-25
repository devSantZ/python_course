# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print("ESTOU NO GETTER")
        return self._cor

    @cor.setter
    def cor(self, valor):
        print("ESTOU NO SETTER")
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("Azul")
caneta.cor = "Rosa"
caneta.cor_tampa = "Azul"
print(caneta.cor)
print(caneta.cor_tampa)

"""
Em Python, a combinação de decoradores @property, @<atributo>.setter e @<atributo>.deleter permite criar propriedades 
que se comportam como atributos, mas nos bastidores, possuem métodos personalizados para acesso, atribuição e exclusão.
Isso é uma forma de implementar o padrão de projeto "getter" e "setter" de forma mais elegante e Pythonica.
"""

# @property (Getter)
# O decorador @property é usado para criar um getter personalizado para um atributo de uma classe. O método decorado com
# @property é acessado como se fosse um atributo normal, mas, nos bastidores, ele chama a função definida no decorador.
# Assim, você pode realizar alguma lógica personalizada antes de retornar o valor.


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


circle1 = Circle("21")
print(circle1.radius)


# @<atributo>.setter (Setter)
# O decorador @<atributo>.setter permite criar um método para atribuir um valor personalizado a um atributo. Quando você
# faz uma atribuição ao atributo decorado com o setter, na verdade está chamando a função definida no decorador.


class Circle1:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius...")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setting radius...")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")


# Uso do @<atributo>.setter (Setter)
circle = Circle1(5)
circle.radius = 7  # Output: Setting radius...
print(circle.radius)  # Output: Getting radius... \n 7

circle.radius = (
    -3
)  # Output: Setting radius... \n ValueError: Radius cannot be negative.


"""
@<atributo>.deleter (Deleter)
O decorador @<atributo>.deleter permite criar um método para excluir um atributo. Quando você usa o operador del para 
excluir o atributo decorado, o método definido no decorador é chamado.
"""


class Circle2:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius...")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setting radius...")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius


# Uso do @<atributo>.deleter (Deleter)
circle = Circle2(5)
print(circle.radius)  # Output: Getting radius... \n 5

del circle.radius  # Output: Deleting radius...
# Agora, se tentarmos acessar o atributo, receberemos um AttributeError, pois o atributo foi deletado.
print(
    circle.radius
)  # Output: AttributeError: 'Circle' object has no attribute '_radius'

# O uso dos decoradores @property, @<atributo>.setter, e @<atributo>.deleter permite que você tenha mais controle sobre
# o acesso, atribuição e exclusão de atributos em suas classes, e ao mesmo tempo mantém uma interface limpa e fácil de
# usar para os usuários de suas classes.

"""
O uso do sublinhado (_) antes dos nomes dos atributos é uma convenção em Python para indicar que esses atributos são 
considerados "privados" e devem ser usados apenas dentro da classe. Embora não haja um mecanismo rígido de acesso 
privado em Python (como em algumas outras linguagens de programação), a convenção do sublinhado serve como um aviso para
os desenvolvedores de que esses atributos não devem ser acessados diretamente fora da classe.
"""
# Vamos corrigir os exemplos anteriores para seguir a convenção do sublinhado:


class Circle3:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius...")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setting radius...")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius


# Uso do @property, @<atributo>.setter e @<atributo>.deleter com o sublinhado
circle = Circle3(5)
print(circle.radius)  # Output: Getting radius... \n 5

circle.radius = 7  # Output: Setting radius...
print(circle.radius)  # Output: Getting radius... \n 7

del circle.radius  # Output: Deleting radius...
# Agora, se tentarmos acessar o atributo, receberemos um AttributeError, pois o atributo foi deletado.
print(
    circle.radius
)  # Output: AttributeError: 'Circle' object has no attribute '_radius'
