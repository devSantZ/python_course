"""
Problemas dos parametros mutaveis em funções python
Os parâmetros mutáveis em funções Python podem levar a problemas sutis e inesperados, especialmente quando se trata de
funções que são chamadas várias vezes ou em contextos concorrentes. Aqui estão alguns dos problemas comuns associados
aos parâmetros mutáveis em funções Python:

1. Compartilhamento de estado: Quando uma função modifica um parâmetro mutável, essa modificação é refletida em todos os
lugares em que o objeto é usado. Isso pode levar a efeitos colaterais indesejados, especialmente quando diferentes
partes do programa dependem do estado original do objeto.

2. Efeito colateral em chamadas subsequentes: Se uma função modificar um parâmetro mutável e a mesma função for chamada
novamente posteriormente, ela será afetada pelo estado modificado anteriormente. Isso pode levar a resultados incorretos
ou inesperados, pois a função não terá o estado inicial esperado.

3. Dificuldade na depuração: Quando uma função modifica um parâmetro mutável, pode ser difícil rastrear onde e quando
exatamente as modificações ocorreram. Isso pode tornar a depuração mais complexa e aumentar a probabilidade de erros.

4. Problemas de concorrência: Se várias threads ou processos estiverem compartilhando o mesmo objeto mutável e tentarem
modificá-lo simultaneamente, isso pode levar a condições de corrida e resultados imprevisíveis. É necessário adotar
mecanismos de sincronização adequados, como bloqueios (locks) ou semáforos, para evitar problemas de concorrência.

Para evitar esses problemas, é recomendável seguir algumas práticas recomendadas:

- Evite modificar objetos mutáveis passados como argumentos. Se possível, trabalhe com cópias dos objetos ou crie novos
objetos para evitar alterações indesejadas.

- Documente claramente as funções que têm efeitos colaterais e os objetos que são mutáveis. Isso ajudará os outros
desenvolvedores a entenderem como essas funções se comportam.

- Utilize objetos imutáveis sempre que possível, como strings ou tuplas, em vez de objetos mutáveis, como listas ou
dicionários.

- Considere o uso de bibliotecas ou estruturas de dados que garantam a imutabilidade ou forneçam mecanismos de controle
de acesso seguro a objetos mutáveis, como a classe `threading.Lock` para controle de concorrência.

Lembrando que o uso de parâmetros mutáveis em funções não é intrinsecamente ruim, mas é importante entender os possíveis
problemas e tomar precauções adequadas para evitar comportamentos indesejados.
"""
# Forma problemática
# def adiciona_clientes(cliente, lista=[]):
#     lista.append(cliente)
#     return lista


# Forma correta
def adiciona_clientes(cliente, lista=None):
    if lista is None:
        lista = []
    lista.append(cliente)
    return lista


clientes1 = adiciona_clientes("pedro")
adiciona_clientes("lucas", clientes1)
adiciona_clientes("maria", clientes1)
clientes1.append("eduardo")

clientes2 = adiciona_clientes("marta")
adiciona_clientes("caua", clientes2)
adiciona_clientes("julio", clientes2)
clientes2.append("murilo")

print(clientes1, clientes2, sep="\n")
