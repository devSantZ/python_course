"""
================BONUS================
Em Python, existem valores truthy e falsy, tipos 
mutáveis e imutáveis. Vamos abordar cada conceito
separadamente:

Valores Truthy e Falsy:
Em Python, alguns valores são considerados "truthy"
e outros são considerados "falsy" em um contexto booleano.
Valores truthy são aqueles que são considerados 
verdadeiros, enquanto os valores falsy são considerados 
falsos. Aqui estão alguns exemplos:

Valores truthy:

    Qualquer número diferente de zero (por exemplo, 1, 2.5, -3)
    Qualquer string não vazia (por exemplo, "hello", "123")
    A lista, tupla, dicionário ou conjunto não vazios
    O valor especial True

Valores falsy:

    O número zero (0) de qualquer tipo (int, float)
    O valor especial None
    Uma string vazia ('' ou "")
    A lista, tupla, dicionário ou conjunto vazios
    O valor especial False

Ao avaliar uma expressão em um contexto booleano, esses
valores truthy e falsy são usados para determinar o resultado. Por exemplo, em um condicional "if", o bloco de código é executado se a expressão for truthy e ignorado se for falsy.

Tipos Mutáveis e Imutáveis:
Em Python, existem tipos mutáveis e imutáveis. A mutabilidade
se refere à capacidade de alterar um objeto após sua criação.

Tipos mutáveis:

    Listas (list)
    Dicionários (dict)
    Conjuntos (set)

Tipos imutáveis:

    Números (int, float)
    Strings (str)
    Tuplas (tuple)
    Valores booleanos (bool)

Em tipos mutáveis, você pode modificar o objeto existente, 
adicionar ou remover elementos, enquanto em tipos imutáveis,
você cria um novo objeto sempre que faz uma modificação.
Por exemplo, ao modificar uma lista, você pode alterar um 
elemento específico sem criar uma nova lista. No entanto,
em uma string, se você deseja fazer uma alteração, 
é necessário criar uma nova string com as modificações 
desejadas.

A distinção entre tipos mutáveis e imutáveis é importante 
para entender o comportamento de alguns recursos da linguagem 
Python, como a atribuição por referência e a passagem de 
argumentos para funções.
"""
# Exemplos
value = 10

if value:  # value é truthy
    print("Value é verdadeiro!")
else:
    print("Value é falso!")

empty_list = []

if empty_list:  # empty_list é falsy
    print("Lista não vazia!")
else:
    print("Lista vazia!")

name = "John"

if name:  # name é truthy
    print("Nome não vazio!")
else:
    print("Nome vazio!")


# Exemplo com tipo mutável (lista)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Exemplo com tipo imutável (string)
my_string = "Hello"
new_string = my_string + " World"
print(new_string)  # Output: "Hello World"
