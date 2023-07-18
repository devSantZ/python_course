# Os métodos de classe (classmethod) são métodos da classe e não da instância, quer dizer que eles não tem acesso aos
# dados da instância.
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod
    def fala_nome(self):
        print(self.nome)  # --> Erro


p1 = Pessoa('Luiz', 'Otávio')
p1.fala_nome()  # AttributeError: type object 'Pessoa' has no attribute 'nome'

# Um caso onde julgo útil ter um método de classe é para gerar um novo objeto da classe, por exemplo:


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod
    def cria_pessoa(cls, nome, sobrenome):
        return cls(nome, sobrenome)


p1 = Pessoa.cria_pessoa('Marcos', 'Otávio')
p2 = Pessoa.cria_pessoa('Lucas', 'Ferreira')

print(p1.nome, p1.sobrenome)  # Marcos Otávio
print(p2.nome, p2.sobrenome)  # Lucas Ferreira

# Os métodos de classe só tem acesso à classe em si (nada das instâncias) então, ao invés de "self" (que se refere à
# instancia), usamos "cls" (que se refere à classe em si).
#
# Geralmente, em 99.9% dos casos você vai trabalhar com métodos de instância. Você vai usar métodos de classe em
# cenários muito específicos, como o que eu te demonstrei anteriormente, gerar um novo objeto da classe por alguma
# razão específica.
#
# Imagine isso como sendo um molde (classe) e um objeto gerado a partir do molde

# Tudo o que é ligado à classe pode ser adicionado em um classmethod, tudo o que é ligado ao objeto (instância) deve ser
# adicionado a um método de instância.
#
# Imagine que cada um desses cookies tem um nome (claramente isso é de instância).


class Cookie:
    def __init__(self, nome):
        self.nome = nome  # instância

    def fala_nome(self):
        # Aqui eu vou precisar do nome da instância
        # portanto método de instância
        print(f'O nome do cookie é: {self.nome}')

    @classmethod
    def cria_cookie(cls):
        # Isso retorna a própria classe já criando
        # uma instância
        return cls(nome='Sem nome')


c1 = Cookie('Gato 1')
c1.fala_nome()  # O nome do cookie é: Gato 1

# Se, por algum motivo, eu precisar criar um objeto
# sem nome, eu posso utilizar meu método de classe
# isso é apenas um exemplo bobo
c2 = Cookie.cria_cookie()
c2.fala_nome()  # O nome do cookie é: Sem nome

# Resumo
# Tem mais uma coisa faltando... falamos dos métodos de classe e de instância... mas também tem os métodos estáticos,
# esses não tem acesso nem à classe e nem à instancia. São basicamente funções que por algum motivo vivem dentro da
# classe (talvez por organização).

# Então segue a regrinha:

# 1 - Se precisar usar a palavra self dentro do método: tem de ser método de instância
# 2 - Se precisar usar a classe em si dentro do método (cls) tem de ser método de classe
# 3 - Se não precisar nem de self e nem de cls dentro do método, pode ser um método estático.