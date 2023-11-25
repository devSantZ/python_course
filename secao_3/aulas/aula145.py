"""
Criando Exceptions em Python Orientado a Objetos
Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.
https://docs.python.org/3/library/exceptions.html
Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
"""


class MeuError(Exception):
    pass


class OutroError(Exception):
    pass


def levantar_excecao():
    _exeception = MeuError("erro da minha classe")
    raise _exeception


try:
    levantar_excecao()

except (MeuError, ZeroDivisionError) as error:
    print(f"{error.__class__.__name__}: {error}")
    print(28 * "= ")
    _exeception = OutroError("erro da minha outra classe")
    raise _exeception from error
