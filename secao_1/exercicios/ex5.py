print("-" * 30)
print("exercício 1")
print("-" * 30)
try:
    numero = int(input("Digite um número inteiro: "))
    numero = int(numero)
    if numero % 2 == 0:
        print(f"o número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

except:
    print(f"Voce não digitou um número inteiro")

print("-" * 30)
print("exercício 2")
print("-" * 30)

try:
    hora_digitada = int(input("Digite o horário: "))
    while hora_digitada >= 0 and hora_digitada <= 24:
        if hora_digitada in range(0, 12):
            print("Bom dia")
            break
        elif hora_digitada in range(12, 18):
            print("Boa tarde")
            break
        elif hora_digitada in range(18, 24):
            print("Boa noite")
            break

    print("voce inseriu um horário inesistente")

except:
    print("use apenas números inteiros para este programa!")

print("-" * 30)
print("exercício 3")
print("-" * 30)

nome_do_usuario = input("Qual é o seu nome? ")

tamanho_do_nome = len(nome_do_usuario)
if tamanho_do_nome <= 4:
    print("nome curto")
elif tamanho_do_nome == 5 or tamanho_do_nome == 6:
    print("nome normal")
elif tamanho_do_nome > 6:
    print("seu nome é muito longo")
