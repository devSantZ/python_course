"""
Em Python, os métodos podem ser definidos como públicos, protegidos ou privados usando convenções de nomenclatura
específicas, pois Python não possui modificadores de acesso como em algumas outras linguagens de programação (por
exemplo, Java ou C++).
"""

# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

"""
É importante observar que, mesmo com as convenções de nomenclatura, ainda é possível acessar métodos protegidos e 
privados em Python, mas é considerado uma má prática fazê-lo, pois viola o encapsulamento e pode levar a comportamentos 
inesperados. A ideia é que os desenvolvedores respeitem essas convenções e tratem os métodos como sugerido por sua 
nomenclatura.
"""


class Foo:
    def __init__(self):
        self.public = 'public'
        self.protected = 'protected'
        self.private = 'private'


    def public_method(self):
        """
        Método Público:
        Um método é considerado público se for acessível a partir de qualquer lugar dentro da classe ou de fora dela.
        Em Python, os métodos são públicos por padrão, o que significa que todos os métodos definidos em uma classe são
        públicos, a menos que seu nome comece com um único sublinhado (_) ou dois sublinhados (__).
        """
        return f'Este é um método publico'

    def _protected_method(self):
        """
        Método Protegido:
        Um método é considerado protegido se seu nome começar com um único sublinhado (_). Embora não haja uma
        verdadeira restrição de acesso em Python, essa convenção indica que o método deve ser tratado como protegido e
        não deve ser acessado fora da classe ou das subclasses.
        """
        return f'Este é um método protegido'

    def __private_method(self):
        """
        Método Privado:
        Um método é considerado privado se seu nome começar com dois sublinhados (__). Da mesma forma, não há uma
        restrição real de acesso, mas essa convenção indica que o método deve ser tratado como privado e não deve ser
        acessado diretamente fora da classe.
        Quando se utiliza o duplo sublinhado, Python faz uma "mangling" (transformação do nome do método) para tornar o
        método mais difícil de ser acessado acidentalmente fora da classe. O nome do método é modificado na forma
        _NomeDaClasse__metodo_privado.
        """
        return f'Este é um método privado'


f = Foo()
print(f.public_method())
print(f._protected_method())
print(f._Foo__private_method())
