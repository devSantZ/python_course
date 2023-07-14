"""
__dict__ e vars para atributos da instancia
"""


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade



dados = {'nome': 'Caio', 'sobrenome': 'Almeida', 'idade': 26}
p1 = Pessoa(**dados)
print(vars(p1))



# print(p1.__dict__)
# print(vars(p1))
# p1.__dict__['partimonio'] = 21000000
