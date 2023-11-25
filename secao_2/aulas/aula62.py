"""
introdução a funções (def) em Python
Fuções são trechos de códigos usados para
replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico
Por padrão, funções retornam None
"""


#           parâmetro
def imprimir(a, b, c):
    print(a, b, c)


#     argumento/valor
imprimir(1, 2, 34)


def saudacao(nome="Sem Nome"):
    print(f"olá {nome}")
