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
        raise TypeError("valor tem que ser uma string!")


@criar_func
def inverte(valor):
    return valor[::-1]


invertida = inverte("olá")
print(invertida)


# Criando meu decorador
def is_positive_or_negative(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in result:
            if i > 0:
                print(f"{i} É um numero positivo")
            else:
                print(f"{i} É um numero negativo")
        return f""

    return inner


@is_positive_or_negative
def receive_number(*args):
    return list(args)


print(receive_number(12, 1, 4, -4, -34, 2))
