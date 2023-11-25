"""
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.
Criando um set
set(iterável) ou {1, 2, 3}
s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
Sets são eficientes para remover valores duplicados
de iteráveis.
- Seus valores serão sempre únicos;
- Não aceitam valores mutáveis;
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)
"""
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
s1 = {1, 2, 3}
print(3 not in s1)
for numero in s1:
    print(numero)
"""
Métodos úteis:
add, update, clear, discard
"""

s1 = set()
s1.add("Luiz")
s1.add(1)
s1.update(("Olá mundo", 1, 2, 3, 4))
# s1.clear()
s1.discard("Olá mundo")
s1.discard("Luiz")
print(s1)
print(s1)
"""
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
"""
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)


# ============  EXEMPLOS ============
frutas = {"maçã", "banana", "laranja"}
# Adicionando elementos a um conjunto
frutas.add("abacaxi")

# Verificando a existência de um elemento em um conjunto
existe_banana = "banana" in frutas

#     Removendo um elemento de um conjunto
frutas.remove("maçã")

# Iterando sobre um conjunto:
for fruta in frutas:
    print(fruta)

# Realizando operações entre conjuntos
frutas1 = {"maçã", "banana", "laranja"}
frutas2 = {"banana", "abacaxi", "uva"}

uniao = frutas1.union(frutas2)  # união de conjuntos (sem duplicação)
intersecao = frutas1.intersection(
    frutas2
)  # interseção de conjuntos, (o que tem em ambas)
diferenca = frutas1.difference(frutas2)  # diferença entre conjuntos
print(f"{frutas1}\n{frutas2}")
print(f"{uniao = }\n{intersecao = }\n{diferenca = }")
