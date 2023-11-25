"""
try, except, else e finally
O try-except é uma construção da linguagem Python 
que permite capturar e tratar exceções, ou erros,
que podem ocorrer durante a execução de um programa.
Essa construção é muito útil quando se deseja evitar
que o programa seja interrompido abruptamente devido
a um erro e, ao invés disso, executar algum código
para lidar com essa situação.
Extrutura básica
try:
    # Código que pode gerar uma exceção
    # ...
except Excecao1:
    # Código para tratar a exceção Excecao1
    # ...
except Excecao2:
    # Código para tratar a exceção Excecao2
    # ...
else:
    # Código a ser executado se nenhuma exceção ocorrer no bloco try
    # ...
finally:
    # Código a ser executado sempre, independentemente de ter ocorrido uma exceção ou não
    # ...
"""

try:
    # lista = [1, 2]
    # print(lista[4])
    # i = c[3]
    a = 10
    b = 0
    c = a / b
    print(c)

except ZeroDivisionError as error:
    print(error.__class__.__name__, error)
except NameError:
    print('Nome "c" não está definido!')
except IndexError:
    print("O index está fora do range da lista!")
