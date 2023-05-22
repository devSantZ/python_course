"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todos os códigos são alcançavel,
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    x = 2
    
    def outra_funcao():
        global x
        x = 3
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
