"""
Abrindo e fechando arquivos: Utilize a função open() para abrir um arquivo. O contexto with é recomendado, pois
elegarante que o arquivo será fechado corretamente após o uso.

Modos de abertura de arquivo: Ao abrir um arquivo, você pode especificar um modo, como 'r' (leitura), 'w' (escrita), 'x'
(criação), 'a' (escrita ao final), 'b' (modo binário) e 't' (modo texto). O modo pode ser combinado com '+' para leitura
e escrita.

Métodos de escrita: Utilize o método write() para escrever uma string no arquivo. O método writelines() permite escrever
várias linhas de uma vez, recebendo uma lista de strings.

Movendo o cursor: O método seek() permite mover o cursor para diferentes posições no arquivo, especificando um
deslocamento em relação ao início do arquivo.

Métodos de leitura: Utilize o método read() para ler o conteúdo completo do arquivo como uma string. O método readline()
lê uma linha do arquivo, enquanto o readlines() lê todas as linhas e retorna uma lista.

Módulo os: O módulo os oferece funções adicionais para manipulação de arquivos. os.remove() ou os.unlink() apaga o
arquivo especificado. os.rename() permite renomear ou mover o arquivo.

Essas são algumas das funcionalidades básicas para manipulação de arquivos em Python. Elas permitem que você crie,
escreva, leia, mova e apague arquivos de texto de maneira eficiente. O exemplo fornecido mostra como utilizar essas
funcionalidades de forma prática.

Lembrando que também mencionamos o módulo json para geração e leitura de arquivos JSON, mas não o utilizamos no exemplo.
O módulo json permite trabalhar com a estrutura de dados JSON de forma conveniente em Python.
"""

"""
# Exemplo de manipulação de arquivos com Python

# Abrindo um arquivo em modo de escrita ('w')
with open('exemplo.txt', 'w') as arquivo:
    # Escrevendo no arquivo utilizando o método write()
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo de manipulação de arquivos em Python.\n')
    arquivo.write('Vamos explorar algumas funcionalidades.\n')

    # Utilizando o método writelines() para escrever várias linhas de uma vez
    linhas = ['Esta é a linha 4.\n', 'Esta é a linha 5.\n', 'Esta é a linha 6.\n']
    arquivo.writelines(linhas)

    # Movendo o cursor para o início do arquivo utilizando o método seek()
    arquivo.seek(0)

    # Lendo todo o conteúdo do arquivo utilizando o método read()
    conteudo = arquivo.read()
    print('Conteúdo do arquivo:\n', conteudo)

    # Movendo o cursor para o início do arquivo novamente
    arquivo.seek(0)

    # Lendo uma linha do arquivo utilizando o método readline()
    linha1 = arquivo.readline()
    print('Linha 1:', linha1)

    # Lendo todas as linhas do arquivo utilizando o método readlines()
    linhas = arquivo.readlines()
    print('Linhas restantes:\n', linhas)

# Exemplos de uso do módulo os para manipulação de arquivos
import os

# Apagando o arquivo utilizando o método remove() do módulo os
os.remove('exemplo.txt')

# Renomeando um arquivo utilizando o método rename() do módulo os
os.rename('exemplo.txt', 'novo_nome.txt')

"""
import os


caminho_arquivo = "aula12.txt"
with open(caminho_arquivo, "w+", encoding="utf-8z") as arquivo:
    arquivo.write("Linha 1\n")  # escreve uma linha
    arquivo.write("Linha 2\n")
    arquivo.writelines(("Linha 3\n", "Linha 4\n"))  # escreve várias linhas
    arquivo.seek(0, 0)
    print(arquivo.read())

    print("Lendo")
    arquivo.seek(0, 0)
    print(arquivo.readline(), end="")
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print("READLINES")
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print("#" * 10)

with open(caminho_arquivo, "r") as arquivo:
    print(arquivo.read())

# os.remove(caminho_arquivo) apaga o arquivo
# os.unlink(caminho_arquivo) apaga o arquivo
# os.rename(caminho_arquivo, 'aula113.txt') renomea o arquivo


from time import sleep

path_file = "aula112.txt"


def open_file():
    try:
        with open(path_file, "r") as way:
            print("ok, arquivo criado")
        return
    except:
        with open(path_file, "w") as way:
            print("Criando o arquivo")
            sleep(2)
        return open_file()


open_file()
