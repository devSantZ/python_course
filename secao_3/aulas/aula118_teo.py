"""
A programação orientada a objetos (POO) é um paradigma de programação que organiza o código em torno de objetos que
representam entidades do mundo real. No Python, assim como em várias outras linguagens de programação, é possível
utilizar a POO para desenvolver programas de forma estruturada e modular.

Existem alguns conceitos fundamentais na programação orientada a objetos em Python:

1. Classes: Uma classe é uma estrutura que define o comportamento e as propriedades de um objeto. Ela é a estrutura
fundamental da POO em Python. Por exemplo, você pode ter uma classe chamada "Carro" que define como um objeto carro se
comporta e quais atributos ele possui.

2. Objetos: Um objeto é uma instância de uma classe. Quando você cria um objeto, você está criando uma cópia da classe
com valores específicos para os atributos desse objeto. Por exemplo, você pode criar um objeto chamado "meu_carro" a
partir da classe "Carro", que possui valores únicos para atributos como cor, marca, modelo, etc.

3. Atributos: Atributos são as características de um objeto. Eles podem ser variáveis que armazenam valores específicos
para cada objeto ou métodos (funções) que definem o comportamento do objeto. Por exemplo, um atributo de um objeto carro
pode ser a sua cor.

4. Métodos: Métodos são funções definidas dentro de uma classe que descrevem as ações que um objeto pode realizar. Eles
podem alterar o estado do objeto ou retornar informações sobre ele. Por exemplo, um método de um objeto carro pode ser
"acelerar" ou "frear".

5. Encapsulamento: É o princípio de esconder os detalhes internos de um objeto e fornecer uma interface pública para
interagir com ele. Em Python, o encapsulamento pode ser alcançado usando convenções de nomenclatura, onde métodos e
atributos com um sublinhado no início são considerados como "privados", ou seja, devem ser acessados apenas internamente
dentro da classe.

6. Herança: A herança permite criar novas classes que herdam os atributos e métodos de uma classe existente. Essa
característica permite reutilizar o código e criar hierarquias de classes. Por exemplo, você pode ter uma classe
"CarroEsportivo" que herda da classe "Carro" e adiciona atributos e métodos específicos para carros esportivos.

7. Polimorfismo: Polimorfismo é a capacidade de um objeto pode ser referenciado de várias maneiras, dependendo do
contexto. Isso permite que objetos de diferentes classes sejam tratados de forma semelhante quando compartilham métodos
com o mesmo nome. Por exemplo, tanto um objeto "Carro" quanto um objeto "Moto" podem ter um método "acelerar", mesmo que
a implementação seja diferente para cada um.

Esses são apenas alguns conceitos básicos da programação orientada a objetos em Python. A POO é uma abordagem poderosa
para organizar e estruturar o código, promovendo a reutilização, modularidade e legibilidade do mesmo.


A linguagem Python é considerada uma linguagem multiparadigma, ou seja, possibilita que o desenvolvedor programe utilizando diferentes tipos de programação como procedural, funcional, imperativa e orientação a objetos.

A programação orientada a objetos é um dos paradigmas mais utilizados atualmente, porque através dela é possível organizar a arquitetura do programa trazendo uma perspectiva mais perto do mundo real, considerando as coisas (abstratas ou concretas) do mundo real como objetos no sistema, que interagem entre si e dão vida ao fluxo do programa.

E para garantir uma programação orientada a objetos eficiente, existem alguns pilares desse paradigma que podemos utilizar em programas escritos com Python.
1º Pilar: Abstração

Na programação orientada a objetos, a construção dos objetos é baseada em uma Classe que representa as características daquele objeto.

Abstração é o princípio de criar uma classe que contenha atributos e métodos que são comuns a outras classes e que podem servir como base para serem herdados.

Você abstrai características comuns a N classes e fornece uma classe abstrata que pode ser herdada e servir de base para as demais.

Nesse conceito, podemos mencionar também a questão de fornecer uma classe abstrata como um contrato para que quando herdada garanta que as classes filhas irão implementar os métodos necessários, dessa forma, proteger o nosso código dando a certeza da existência e implementação do método.

Para ilustrar a abstração, imagine um sistema bancário, onde uma Conta bancária possa ser de diversos tipos, como, Conta poupança, Conta Corrente, Conta PJ, etc.

Cada tipo de conta, ainda é uma Conta, e as características comuns a todos os tipos de contas podem ser Abstraídas em  """
from abc import ABCMeta, abstractmethod


# Uma classe abstrata. Por exemplo:
class Conta(metaclass=ABCMeta):
    _numero = "00000"
    _titular = "root"
    saldo = 0

    @abstractmethod
    def __init__(self, numero: str, titular: str, saldo: float):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, value: float):
        pass

    @abstractmethod
    def depositar(self, value: float):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass

"""
Dessa forma eu crio uma abstração do conceito de Conta e disponibilizo uma classe para ser herdada por outras classes que são do tipo Conta.

Obs: Uma classe abstrata não deve ser utilizada diretamente, deve ser vista e utilizada como uma base para outras classes como ContaCorrente, ContaPoupanca, etc.
2º Pilar: Encapsulamento

O princípio de encapsulamento consiste em "esconder" a parte funcional dos objetos de forma que quem estiver utilizando não tenha que conhecer mais do que o necessário para utiliza-lo.

Por exemplo, ao dirigir um carro, se quisermos que o carro pare de andar, não é preciso, conhecer toda a mecânica do funcionamento por dentro do veículo para que possamos frear. Basta pisar no freio, o freio é o encapsulamento do comportamento de frear de um carro.

Na orientação a objetos, estruturamos as classes de forma a encapsular toda regra de negócio e parte funcional relacionada a classe dentro de métodos e atributos, de forma que quem utilize, apenas diga oque quer fazer.
"""


# Por exemplo:
class Biblioteca:

    def __init__(self, livros_disponiveis) -> None:
        self.livros_disponiveis = livros_disponiveis

    def exibir_livros(self):
        for livro in self.livros_disponiveis:
            print(livro)

    def emprestar_livro(self, livro):
        print(f'Você escolheu o livro: {livro}')
        if livro in self.livros_disponiveis:
            self.livros_disponiveis.remove(livro)
        else:
            print('Desculpe o livro não está disponível!')

    def devolver_livro(self, livro):
        self.livros_disponiveis.append(livro)
        print(f'Obrigado pro devolver o livro: {livro}')

"""
Na classe biblioteca, temos os métodos que fornecem as regras de negócio para que o programa que for utilizar não precise conhecer oque está acontecendo ali dentro e sim possa simplesmente dizer:

// biblioteca me mostre os livros:
biblioteca.exibir_livros()

3º Pilar: Herança

A herança consiste em determinar que uma classe existe por si mesma, porém, ela é uma outra classe em sua essência... Por exemplo, uma ContaCorrente existe mas ela é uma Conta.

Quando a herança é utilizada, a classe que herda, automaticamente, possui os atributos e métodos definidos na classe da qual herdou.

Por exemplo, imagine que o sistema bancário tenha uma uma regra geral para deposito e exibição de saldo para todos os tipos de conta somente o saque muda de conta para conta. Nesse caso, podemos criar uma classe Conta com as características comuns das outras Contas, e as outras contas, irão herdar essas características:
"""
class Conta(metaclass=ABCMeta):
    _numero = "00000"
    _titular = "root"
    _saldo = 0

    @abstractmethod
    def __init__(self, numero: str, titular: str, saldo: float):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    @abstractmethod
    def sacar(self, value: float):
        pass

    @abstractmethod
    def depositar(self, value: float):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass


class ContaPoupanca(Conta):

    def __init__(self, numero: str, titular: str, saldo: float):
        super().__init__(numero, titular, saldo)

    def sacar(self, value: float):
        if value <= self._saldo:
            self._saldo -= value
            return True

        return False

    def depositar(self, value: float):
        if value > 0:
            self._saldo += value
            return True

        return False

    def exibir_saldo(self):
        return self._saldo

    def titular(self):
        return self._titular

    def numero(self):
        return self._numero


class BankingSystem:
    __contas = []

    def __gerar_numero_conta(self):
        numero = len(self.__contas) + 1
        return f"{numero:05}"

    def __checar_valor_positivo(self, value):
        if value <= 0:
            return False

        return True

    def criar_conta_poupanca(self, deposito_inicial: float, nome_titular: str):
        if self.__checar_valor_positivo(deposito_inicial) == False:
            print("Deposito Inicial deve ser maior que Zero!")
            return

        conta = ContaPoupanca(self.__gerar_numero_conta(), nome_titular, deposito_inicial)
        self.__contas.append(conta)
        print("Conta criada com sucesso!")
        print("Titular: ", conta.titular())
        print("Número da conta: ", conta.numero())
        print("Saldo: ", conta.exibir_saldo())

    def total_of_contas(self):
        print("contas: ", str(len(self.__contas)))

    def acessar_conta(self, nome_titular: str, conta_numero: str):
        contas = [acc for acc in self.__contas 
                    if acc.titular() == nome_titular and acc.numero() == conta_numero]
        if len(contas) == 0:
            print("Conta não existe!")
            return

        conta = contas[0]
        print("Digite 1 para sacar")
        print("Digite 2 para depositar")
        print("Digite 3 para exibir saldo")
        escolha_usuario = (int(input()))
        if escolha_usuario == 1:
            print("sacar")
            print("Digite o valor a sacar")
            value = float(input())
            if conta.sacar(value):
                print("Saque realizado com sucesso!")
            else:
                print("Problema ao sacar, verifique o saldo!")
        elif escolha_usuario == 2:
            print("DEPOSITAR")
            print("Digite o valor do depósito")
            value = float(input())
            if conta.depositar(value):
                print("Deposito realizado com sucesso!")
            else:
                print("Problema ao depositar, valor não permitido!")
        elif escolha_usuario == 3:
            print(conta.exibir_saldo())
        else:
            print("Escolha inválida!")

banking_system = BankingSystem()
while True:
    print("Digite 1 para criar uma conta poupança")
    print("Digite 2 para acessar a conta")
    print("Digite 3 para exibir o total de contas")
    print("Digite 0 para sair")
    escolha_usuario = (int(input()))
    if escolha_usuario == 1:
        print("CREATE")
        print("Digite o nome do titular da conta")
        nome_titular = input()
        print("Digite o deposito inicial")
        initial_deposit = float(input())
        banking_system.criar_conta_poupanca(initial_deposit, nome_titular)
    elif escolha_usuario == 2:
        print("ACCESS")
        print("Digite o nome do titular da conta")
        nome_titular = input()
        print("Digite o número da conta")
        conta_numero = input()
        banking_system.acessar_conta(nome_titular, conta_numero)
    elif escolha_usuario == 3:
        banking_system.total_of_contas()
    elif escolha_usuario == 0:
        quit()
    else:
        print("Escolha inválida!")
