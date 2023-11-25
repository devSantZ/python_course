separador = lambda y, x="=": print(f"{y}\n", 30 * f"{x}")

# Criando dados para armazenar num dicionário
marca = "apple"
cor = "cinza espacial"
tam = "14 pol"
modelo = "Macbook air"
chip = "m1"

# Empacotando dos dados
mac = {"marca": marca, "cor": cor, "tam": tam, "modelo": modelo, "chip": chip}

# Dados
carro = {"fabricante": "Honda", "model": "Civic ej6", "ano": "1995", "valor": 65000}

separador("desempacotamento de dicionários")
# Desempacotando dados
frabricante, model, ano, valor = (
    carro["fabricante"],
    carro["model"],
    carro["ano"],
    carro["valor"],
)
print(frabricante, model, ano, valor)


# Calculando área do triângulo
def calcula_area_triangulo():
    """
    fução recebe 2 valores separados por virgula, onde
    o primeiro valor equivale a b(base) e o segundo
    à h(altura) e retorna o calculo da área do
    triângulo>
    """
    dados = input("insira a área, base e altura do triângulo: ").split()
    b, h = [int(i) for i in dados]
    area = b * h / 2
    return f"{area} cm2"


resultado = calcula_area_triangulo()
print(resultado)

"""
Em Python, **kwargs é uma sintaxe especial que permite 
passar um número variável de argumentos nomeados para 
uma função. A palavra-chave kwargs é uma abreviação para
"keyword arguments" (argumentos de palavra-chave).
"""
separador('uso de "**kwargs" na função')

dados_pessoa = {
    "nome": "João",
    "sobrenome": "Almeida",
    "idade": 32,
    "altura": 1.67,
    "peso": 63,
}


def desempacota(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


pessoa = desempacota(nome="Diego", sobrenome="Santos", idade=21)
print(pessoa)
print(desempacota(**dados_pessoa))
