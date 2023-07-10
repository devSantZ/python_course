import os
from time import sleep
 
#lista
lista_de_compra = []
 
 
while True:
    #entrada do usuário
    entrada = input('[i]nseir [a]pagar [l]]istar: ').lower()
 
    # inserir item
    if entrada == 'i':
        if entrada == '' or entrada == ' ':
            print('Por favor, insira um item válido.')
            sleep(2)
            os.system('clear')
        else:
            item = input('adicione um item: ')
            print(f'Você adicionou "{item}" na sua lista.')
            lista_de_compra.append(item)
            sleep(2)
            os.system('clear')
 
    # listar itens
    elif entrada == 'l':
        os.system('clear')
        if len(lista_de_compra) == 0:
            print('Nada para listar...')
            sleep(2)
            os.system('clear')
        else:
            for i, v in enumerate(lista_de_compra):
                print(i, v)
 
    # apagar item
    elif entrada == 'a':
        os.system('clear')
        if len(lista_de_compra) == 0:
            print('Nada para apagar...')
            sleep(2)
            os.system('clear')
        else:
            try:
                for i, v in enumerate(lista_de_compra):
                    print(i, v)
                indice = int(input('Escolha o índice para apagar: '))
                lista_de_compra.pop(indice)
                print('Removido com sucesso.')
            except IndexError:
                print('Não existe esse índice.')
                sleep(2)
                os.system('clear')
            except ValueError:
                print('Insira apenas índices válidos.')
                sleep(2)
                os.system('clear')
 
    else:
        print('Escolha uma ação válida.')
        sleep(2)
        os.system('clear')