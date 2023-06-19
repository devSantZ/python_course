"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover/ Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções.
"""


# funcção decoradora
def criar_func(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
            resultado = func(*args, **kwargs)
        return resultado
    return interna


def e_string(valor):
    if not isinstance(valor, str):
        raise TypeError('valor tem que ser uma string!')


def inverte(valor):
    return valor[::-1]

invertida_string_checando_valor = criar_func(inverte)
invertida = invertida_string_checando_valor('1234')
print(invertida)