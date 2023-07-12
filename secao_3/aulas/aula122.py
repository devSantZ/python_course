"""
O parâmetro self é uma convenção em Python que representa o próprio objeto que está sendo manipulado. Ele é usado como o
primeiro parâmetro em todos os métodos de uma classe, incluindo o método __init__.
Ao criar uma classe e seus métodos, o parâmetro self é utilizado para acessar e manipular os atributos e métodos do
objeto atual. Ele é uma referência ao próprio objeto e permite que você se refira a si mesmo dentro da definição da
classe.
 """
class Cookie:
    def __init__(self, tipo, nome):
        self.tipo = tipo
        self.nome = nome

    def assar_cookie(self):
        if self.tipo == 'salgado'.lower():
            print('Não vou assar um bolo salgado!')
        else:
            print(f'{self.nome} está assando')

bolinho = Cookie('doce', 'red velvet')
Cookie.assar_cookie(bolinho)

