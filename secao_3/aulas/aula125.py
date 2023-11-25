"""
ATRIBUTOS DA CLASSE
Dentro de uma classe, podem ser definidos atributos, que são variáveis associadas a essa classe. Os atributos podem ser
de instância ou de classe.

Atributos de instância são específicos a cada objeto criado a partir da classe. Eles são definidos dentro do método
especial __init__, que é o construtor da classe, e podem ser acessados por meio da sintaxe self.nome_do_atributo. Cada
objeto pode ter seus próprios valores para esses atributos.

Atributos de classe, por outro lado, são compartilhados por todos os objetos da classe. Eles são definidos diretamente
dentro da classe, fora de qualquer método, e podem ser acessados por meio da sintaxe Classe.nome_do_atributo. Todos os
objetos da classe compartilham o mesmo valor para esses atributos.

Além disso, existem também os atributos de objeto, que são atribuídos dinamicamente a um objeto específico após sua
criação. Eles podem ser definidos simplesmente atribuindo um valor a um novo nome de atributo utilizando a sintaxe
objeto.nome_do_atributo = valor.
"""


class Exemplo:
    atributo_da_classe = "Este atributo é da classe "

    def __init__(self, atributo_da_instancia):
        self.atributo_da_instancia = atributo_da_instancia

    def concatenacao(self, palavra):
        return self.atributo_da_classe + palavra


# Exemplo.atributo_da_classe = 'Outra coisa '
var = Exemplo("refere-se ao atributo_da_instancia")
print(var.atributo_da_instancia)

print(
    Exemplo.concatenacao(var, '"com a palavra a juntar"')
)  # atributo_da_classe + "com a palavra a juntar"
print(var.concatenacao('Palavra pra juntar com o "var"'))


class Exemplo2:
    atributo_da_classe = "Este atributo é da classe "

    def __init__(self):
        pass

    @staticmethod
    def concatenacao(palavra):
        return Exemplo.atributo_da_classe + palavra


print(Exemplo2.atributo_da_classe)
print(Exemplo2.concatenacao("palavra aleatoria"))


# Atributos de classe
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa("João", 35)
p2 = Pessoa("Helena", 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
