"""
Em Python, uma classe é uma estrutura que permite definir objetos com atributos (variáveis) e métodos (funções)
relacionados. Uma classe serve como um modelo ou projeto para criar objetos específicos, conhecidos como instâncias da
classe.
As classes são criadas usando a palavra-chave "class" seguida pelo nome da classe
"""
# classe

class Exemplos:
    """
    Classe com exemplos de Classes, Objetos, Atributos, Métodos,
    Encapsulamento, Herança e Polimorfismo.
    """

    # Exemplo de Classe
    class Pessoa:
        pass

    # Exemplo de criação de objetos
    pessoa1 = Pessoa()
    pessoa2 = Pessoa()

    # Exemplo de atributos em uma classe
    class Retangulo:
        def __init__(self, largura, altura):
            self.largura = largura
            self.altura = altura

        def calcular_area(self):
            return self.largura * self.altura

    # Exemplo de encapsulamento
    class ContaBancaria:
        def __init__(self, saldo):
            self._saldo = saldo

        def depositar(self, valor):
            self._saldo += valor

        def _verificar_saldo(self):
            return self._saldo

    # Exemplo de herança
    class Animal:
        def fazer_som(self):
            pass

    class Cachorro(Animal):
        def fazer_som(self):
            return "Au au!"

    # Exemplo de polimorfismo
    class Gato(Animal):
        def fazer_som(self):
            return "Miau!"

    def fazer_barulho(animal):
        print(animal.fazer_som())

    cachorro = Cachorro()
    gato = Gato()

    fazer_barulho(cachorro)  # Saída: Au au!
    fazer_barulho(gato)  # Saída: Miau!
