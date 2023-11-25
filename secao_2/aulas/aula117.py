"""Positional-Only Parameters (/) e Keyword-Only Arguments (*)
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)

🟢 Positional-only Parameters (/) - Tudo antes da barra deve
ser ❗️APENAS❗️ posicional.

PEP 570 – Python Positional-Only Parameters
https://peps.python.org/pep-0570/

🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.

PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""


# Todos os parâmetros antes da barra devem ser posicionais
def positional_only_parameters(a, b, /, x, y):
    print(a + b + x + y)


def keyword_only_parameters(a, b, *, c):
    print(a + b + c)


positional_only_parameters(1, 2, 3, 4)
keyword_only_parameters(1, 2, c=3)
