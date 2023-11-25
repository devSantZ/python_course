var = "ru3+274n8t8382t2094t47462"
tamanhao_var = 0
quantidade_letras = 0
quantidade_numero = 0

while var:
    try:
        for i in var:
            tamanhao_var += 1
            if i.isalpha():
                print(f"{i} é uma letra")
                quantidade_letras += 1
            elif i.isnumeric():
                print(f"{i} é um número")
                quantidade_numero += 1
            else:
                (f"{i} não é um numero e não é uma letra")
        if tamanhao_var == len(var):
            print(
                f"a variavel tem {quantidade_letras} letras e {quantidade_numero} numeros"
            )
            break
    except:
        print("Algo deu errado!!")
