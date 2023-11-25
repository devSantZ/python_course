import os

print("Dica: É uma MARCA!!!")
palavra_secreta = "TOYOTA".upper()
letras_acertadas = ""
tentativas = 5

while True:
    letra_digitada = input("Digite uma letra: ").upper()

    if letra_digitada == "" or letra_digitada == " ":
        print("Por favor insira um caractere válido!")
        continue

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    else:
        tentativas -= 1
        print(f"voce tem {tentativas} tentativas restantes")

    if tentativas == 0:
        chute = input("Chute a palvra secreta: ")

        if chute == palavra_secreta:
            os.system("clear")
            print("Voce ganhou")
            print(f"A palavra secreta era: {palavra_secreta}")
            print(f"Voce precisou de {tentativas} tentativas para acertar")
            break

        else:
            print(f"Voce errou, a palavra secreta era: {palavra_secreta}")
            break

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += "*"
    print("palavra formada", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("Voce ganhou")
        print(f"A palavra secreta era: {palavra_secreta}")
        break
