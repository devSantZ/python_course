"""
O método isinstance() é uma função embutida em 
Python que verifica se um objeto é uma instância                       
de uma determinada classe ou de uma das suas subclasses.
Ele retorna um valor booleano: True se o objeto for 
uma instância da classe especificada, e False caso
contrário.
"""
tipos = dict(
    string="tomate",
    inteiro=34,
    flutuante=2.5,
    booleano=True,
    tupla=(1, 2, "Lucas"),
    lista=[1, 2, 3],
    dicionario={"chave": "valor"},
    conjundo={1, 2, 3},
)

for c, v in tipos.items():
    instacia = isinstance(v, (bool, str, int))
    print(f"{c}: {v}, {instacia}")
