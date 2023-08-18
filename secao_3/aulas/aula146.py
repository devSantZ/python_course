"""
Teoria: python Special Methods, Magic Methods ou Dunder Methods
Dunder = Double Underscore = __dunder__
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames
"""


"""
Os métodos especiais em Python são métodos predefinidos com nomes específicos que têm um significado especial para as classes. Eles permitem que você defina o comportamento personalizado de objetos quando eles estão envolvidos em operações específicas, como adição, comparação, conversão para string, entre outros. Esses métodos são invocados automaticamente quando você utiliza certos operadores ou funções built-in do Python.

Aqui estão alguns exemplos de métodos especiais comuns:

    __init__(self, ...): Este é o método de inicialização da classe, chamado quando um novo objeto é criado. Ele é usado para configurar as propriedades iniciais do objeto.

    __str__(self): Este método controla a representação em formato de string do objeto quando a função str() é chamada sobre ele. É útil para fornecer uma representação legível do objeto.

    __repr__(self): Semelhante ao __str__, mas retorna uma representação não ambígua do objeto, preferencialmente uma que pode ser usada para recriar o objeto.

    __len__(self): Define o comportamento do objeto quando a função len() é aplicada a ele, como em listas ou strings.

    __add__(self, other): Define o comportamento da adição entre dois objetos. Por exemplo, você pode definir a adição entre duas instâncias de uma classe personalizada.

    __eq__(self, other): Controla a comparação de igualdade entre objetos usando o operador ==.

    __lt__(self, other): Controla a comparação de menor que entre objetos usando o operador <.

    __getitem__(self, key): Permite que você acesse elementos de um objeto como se fosse uma sequência ou mapeamento.

    __setitem__(self, key, value): Usado para definir o valor de um elemento do objeto, caso ele suporte operações de atribuição.

    __delitem__(self, key): Define o comportamento de exclusão de um elemento, caso o objeto seja "indexável" e suporte exclusões.

Estes são apenas alguns exemplos de métodos especiais em Python. Eles permitem que você personalize a funcionalidade das suas classes para se comportarem de maneira intuitiva e coerente com as operações nativas da linguagem. Isso torna o código mais legível e expressivo, e ajuda a criar classes mais poderosas e flexíveis.
"""
