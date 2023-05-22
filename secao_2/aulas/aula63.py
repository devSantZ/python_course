"""
Argumentos nomeados e não nomeados em Função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) 
"""

def soma(x = 0, y = 0):
    # Definição
    print(x+y)
    
    
# argumento não nomeado 
soma(3, 5)

# argumento nomeado
soma(y = 3, x = 4)