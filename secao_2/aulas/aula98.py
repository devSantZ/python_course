"""
Singleton é um padrão de projeto que permite criar uma
classe na qual somente uma única instância pode existir.
Isso significa que, independentemente de quantas vezes
você tente criar uma nova instância da classe, você
sempre obterá a mesma instância original.

O padrão Singleton é útil em situações em que você deseja
ter um ponto de acesso global a uma única instância de uma
classe. Isso pode ser útil, por exemplo, quando você 
precisa compartilhar recursos ou manter um estado global
consistente em um sistema
"""
import importlib

import aula98_m


print(aula98_m.var)

for i in range(5):
    importlib.reload(aula98_m)
    print(i)