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


@criar_func
def inverte(valor):
    return valor[::-1]


invertida = inverte(11)
print(invertida)


# Criando meu decorador
def is_positive_or_negative(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 0:
            return f'{result} É um numero positivo'
        return'{result} É um numero negativo'
    return inner


@is_positive_or_negative
def receive_number(n):
    return n


print(receive_number(12))
