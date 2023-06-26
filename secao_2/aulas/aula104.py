"""
O método count() em Python é usado para contar o número de ocorrências
de um determinado elemento em uma sequência, como uma lista, uma string
ou uma tupla. Ele retorna um valor inteiro representando a contagem.
sintaxe basica: sequencia.count(elemento)

"""
from itertools import count 
# teste = count()

# for i in teste:
#     if i >=10:
#         break
#     print(i)


frutas = ['banana', 'maçã', 'pera', 'uva', 'morango', 'abacaxi']

# Conta quantas vezes a letra 'a' aparece em cada palavra da lista
contagem = [(fruta, fruta.count('a')) for fruta in frutas]
print(*contagem, sep='\n')

frase = "Olá, como você está?"
contagem = frase.count('a')
print(contagem) 


