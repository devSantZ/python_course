# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


falsy_or_truthy = lambda x: 'falsy'if not x else 'truthy'

print(f'{lista=}', falsy_or_truthy(lista))
print(f'{dicionario=}', falsy_or_truthy(dicionario))
print(f'{conjunto=}', falsy_or_truthy(conjunto))
print(f'{tupla=}', falsy_or_truthy(tupla))
print(f'{string=}', falsy_or_truthy(string))
print(f'{inteito=}', falsy_or_truthy(inteito))
print(f'{flutuante=}', falsy_or_truthy(flutuante))
print(f'{nada=}', falsy_or_truthy(nada))
print(f'{falso=}', falsy_or_truthy(falso))
print(f'{intervalo=}', falsy_or_truthy(intervalo))