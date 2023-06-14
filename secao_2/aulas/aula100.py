"""
A palavra-chave nonlocal é usada para declarar uma variável em um 
escopo externo a uma função aninhada. Ela permite que você atribua
um valor a uma variável definida em uma função externa à função atual.
Em resumo, nonlocal é usada para indicar que uma variável pertence a
um escopo externo ao da função atual e permite que você faça referência
e modificações nessa variável dentro da função aninhada. É uma forma de
acessar variáveis em um escopo superior dentro de funções internas ou 
aninhadas em Python.
"""

# Exemplo 1
def func_de_fora():
    variavel_de_fora = "Hello "
    def func_de_dentro():
        nonlocal variavel_de_fora
        variavel_de_fora += "World"
        return variavel_de_fora
    return func_de_dentro()

test1 = func_de_fora()
print(test1)


def valor_inicial(x):
    valor = x
    print(locals(), 'locals de valor_inicial')
    
    def valores_secundarios(y):
        nonlocal valor
        valor += y
        print(locals(), 'locals de valores_secundarios')
        return valor
    return valores_secundarios


teste = valor_inicial(10)
print(teste(4))
print(teste(1))
print(teste(32))