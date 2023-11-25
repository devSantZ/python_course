"""
Métodos de classe + factories (fábricas)
São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a
própria classe.
@classmethod é um decorador especial usado para definir métodos que operam na classe em vez de operar em instâncias da classe. Esse
tipo de método recebe a própria classe como primeiro argumento, por convenção chamado de cls, em vez de receber a
instância (por meio do argumento self, que é comum em métodos de instância). Isso permite que você acesse e modifique
atributos de classe ou realize operações que envolvam a classe como um todoo.
"""


class Exemplo1:
    instance_count = 0

    def __init__(self):
        Exemplo1.instance_count += 1

    # Conta quantas vezes a classe foi instanciada
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count


class Exemplo2:
    atributo_da_classe = "Este atributo é da classe "

    def __init__(self):
        pass

    @classmethod
    def concatenacao(cls, palavra):
        return cls.atributo_da_classe + palavra


class Exemplo3:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoa_sem_nome(cls, idade):
        return cls("Anônima", idade)


# Exemplo classe 1
a = Exemplo1()
b = Exemplo1()
c = Exemplo1()
d = Exemplo1()
e = Exemplo1()
f = Exemplo1()
print(Exemplo1.get_instance_count())

# Exemplo classe 2
print(Exemplo2.atributo_da_classe)
print(Exemplo2.concatenacao("palavra aleatoria"))

# Exemplo classe 3
p1 = Exemplo3.pessoa_sem_nome(30)
p2 = Exemplo3("carlos", 21)
print(p2.nome)
