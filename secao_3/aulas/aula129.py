"""
Em Python, o @staticmethod é um decorador usado para definir um método estático em uma classe. Um método estático
pertence à classe em si, em vez de pertencer a uma instância específica dessa classe. Isso significa que você pode
chamar um método estático diretamente da classe, sem precisar criar uma instância dela.
Um método estático em Python é uma função definida dentro de uma classe, mas ele não tem acesso aos atributos
específicos da instância ou à própria classe. Por essa razão, ele é muitas vezes usado para funções que são relevantes
para a classe como um tod0, mas não dependem de nenhum estado específico da instância.

Podemos dizer que o método estático está "protegido" dentro da classe, no sentido de que ele é definido e vinculado à
classe, mas não tem acesso direto a nenhum dos atributos de instância (dados do objeto) ou atributos de classe (dados
compartilhados por todas as instâncias). Ele é uma funcionalidade da classe que pode ser acessada por meio da classe
em si ou por meio de suas instâncias, mas não depende delas para funcionar.

Isso é útil em cenários em que você deseja agrupar certas funções juntas dentro da classe, mas elas não precisam
interagir com o estado interno das instâncias. Um exemplo comum é criar funções utilitárias relacionadas à classe, que
podem ser acessadas de forma mais conveniente através da classe em vez de serem funções soltas fora da classe.

No entanto, é importante lembrar que, embora o método estático não tenha acesso aos atributos da instância, ele ainda
pode ser chamado a partir de uma instância, pois o Python permite esse tipo de acesso, embora não seja a forma
recomendada de usar métodos estáticos. O acesso adequado a um método estático é chamá-lo diretamente através da classe,
como no exemplo anterior.
"""


class MinhaClasse:
    contador = 0  # Variável de classe para contar instâncias

    def __init__(self, nome):
        self.nome = nome
        MinhaClasse.contador += 1

    def metodo_normal(self):
        # Método normal que pode acessar atributos de instância
        return f"Olá, sou {self.nome}"

    @staticmethod
    def metodo_estatico():
        # Método estático que não acessa atributos de instância ou de classe
        return "Método estático sendo chamado"


# Criando instâncias da classe
objeto1 = MinhaClasse("Objeto 1")
objeto2 = MinhaClasse("Objeto 2")

# Chamando um método normal
print(objeto1.metodo_normal())  # Saída: Olá, sou Objeto 1

# Chamando um método estático diretamente da classe
print(MinhaClasse.metodo_estatico())  # Saída: Método estático sendo chamado

# Você também pode chamar o método estático a partir de uma instância, mas não é necessário:
print(objeto1.metodo_estatico())  # Saída: Método estático sendo chamado

# Observe que o método estático não requer a passagem de self como primeiro argumento, pois ele não está associado a uma
# instância específica. Em vez disso, ele pode ser usado para realizar tarefas que não dependem de nenhum atributo
# específico de instância ou de classe.

# Uma característica importante do @staticmethod é que ele não pode acessar ou modificar os atributos de instância ou de
# classe diretamente. Caso você precise acessar atributos de classe, considere usar o @classmethod, que permite acesso
# aos atributos de classe através do primeiro argumento cls.