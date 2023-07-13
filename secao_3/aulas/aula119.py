"""
Em Python, uma classe é uma estrutura que permite definir objetos com atributos (variáveis) e métodos (funções)
relacionados. Uma classe serve como um modelo ou projeto para criar objetos específicos, conhecidos como instâncias da
classe.
As classes são criadas usando a palavra-chave "class" seguida pelo nome da classe
"""
class Pessoa:
    pass

pessoa1 = Pessoa()
pessoa1.nome = 'Diego'
pessoa1.sobrenome = 'Santos'

pessoa2 = Pessoa()
pessoa2.nome = 'Lucas'
pessoa2.sobrenome = 'Moraes'

print(pessoa1.nome, pessoa1.sobrenome)
print(pessoa2.nome, pessoa2.sobrenome)
