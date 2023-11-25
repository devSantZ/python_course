"""
================BONUS================
Dentro das compreensões de conjunto 
(set comprehension) e compreensões de dicionário
(dictionary comprehension) em Python, é possível 
usar a sintaxe de condicionais para aplicar lógica
condicional durante a construção do conjunto ou 
dicionário.
"""

# A sintaxe do if-else à esquerda:
# {expressão_true if condição else expressão_false for item in iterável}
#
# Exemplo:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

condicao_esquerda = lambda x: {x**2 if x % 2 == 0 else x**3 for x in x}
print(condicao_esquerda(lista))

# A sintaxe do if a direita
# {expressão for item in iterável if condição}
# usada para fazer um "filtro"

# Exemplo
condicao_direita = lambda x: {
    x**2 if x % 2 == 0 else x**3 for x in x if x**2 < 100 and x**3 < 100
}

print(condicao_direita(lista))
