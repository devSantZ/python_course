while True:
    #coletando os valores 
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador [+-/*]: ')
    
    numeros_validos = None
    #verificando se os números são válidos para o programa
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        print('Um ou ambos os números digitados não são válidos')
        numeros_validos = None
    #verificando se os operadores são válidos
    operadores_validos = '+-/*'
    
    if operador not in operadores_validos:
        print('Por favor, insira um operador válido')
        continue
    
    if len(operador) > 1:
        print('Insira apenas um operador')
        continue
    
    if numeros_validos:
        #implementação do código para execução do cálculo
        soma = '+'
        sub = '-'
        div = '/'
        mult = '*'
        
        if operador == soma:
            calc = numero_1 + numero_2
            print(f'{numero_1} + {numero_2} = {calc:.2f}')

        if operador == sub:
            calc = numero_1 - numero_2
            print(f'{numero_1} - {numero_2} = {calc:.2f}')

        if operador == div:
            calc = numero_1 / numero_2
            print(f'{numero_1} / {numero_2} = {calc:.2f}')

        if operador == mult:
            calc = numero_1 * numero_2
            print(f'{numero_1} * {numero_2} = {calc:.2f}')
        
    
    sair = input('Deseja continuar? [enter] para sim ou digite [s] para sair: ').lower().startswith('s')
    if sair:
        break