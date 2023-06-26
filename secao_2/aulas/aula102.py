"""
funções decoradoras com parâmetro
"""
# funcção decoradora


def fabrica_de_decoradores(a=None, b=None, c=None):
    def decoradora(func):
        def aninhada(*args, **kwargs):
            resul = func(*args, **kwargs)
            return resul
        return aninhada
    return decoradora


@fabrica_de_decoradores("""a=None, b=None, c=None""")
def soma(n=None):
    return n


# Exemplo
def imposto_em_porcentagem(x):
    def imposto(func):
        def inner_function(*args, **kwargs):
            result = func(*args, **kwargs)
            result += (result * x)
            return result
        return inner_function
    return imposto


@imposto_em_porcentagem(0.1)
def soma(x, y):
    return x + y


print(soma(5, 5))

