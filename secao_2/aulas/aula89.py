"""
dir, hasattr e getattr em Python
    dir: Retorna uma lista de nomes de atributos
        e métodos disponíveis para um determinado objeto.
        sintaxe: dir(objeto)
        
    hasattr: Verifica se um objeto possui um 
        determinado atributo. Ela retorna True se o atributo 
        existir e False caso contrário
        sintaxe: hasattr(objto, atributo)
        
    getattr: Retorna o valor de um atributo de um objeto. 
        Se o atributo não existir, é possível fornecer um valor
        padrão opcional para ser retornado
        sintaxe: getattr(objeto, tributo. [padrão])
"""

# Exemplo dir()
mostra_atributo = lambda x: [i for i in dir(x)]

teste = mostra_atributo(1)
print("\n".join(teste))


# Exemplo hasattr()
valor = "String"
if hasattr(valor, "upper"):
    print(f"o método upper existe pra {valor}")
else:
    print("o método não existe")

# Exemplo getarrt()
metodo = "lower"
print(getattr(valor, metodo)())
