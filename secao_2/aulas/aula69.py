# """
# Closure e funções que retornam outras funções
# """
#
#
# def criar_saudacao(sald, nome):
#     def saudar():
#         return f'{sald} {nome}'
#     return saudar()
#
#
# print(criar_saudacao('olá', 'Diego'))
# Executando a função (sauda_nome) depois (usando closure)
def saudar(saudacao):
    def sauda_nome(nome):
        return f'{saudacao} {nome}!'
    return sauda_nome


puto_com_user = saudar('wtf')
deboa_com_user = saudar('salve meu mano')
print(puto_com_user('Pedro'))
print(deboa_com_user('Diego'))

# Executando a função antes (sem closure)
# def saudar(saudacao):
#     def sauda_nome(nome):
#         return f'{saudacao} {nome}!'
#     return sauda_nome('Diego')
#
#
# puto_com_user = saudar('wtf')
# deboa_com_user = saudar('salve meu mano')
# print(puto_com_user)
# print(deboa_com_user)
