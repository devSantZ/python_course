""" validator login """
print(20 * "-")
print("olá, seja bem vindo ao nosso sistema, favor, faça login para continuar")
print(20 * "-")

USER = "Diego Santos"
PASSWORD = "123"
TENTATIVAS = 4

while True:
    ent_user = input("Insira seu Usuário: ")
    ent_password = input("Insira sua Senha: ")
    if ent_user == "" or ent_password == "":
        print("Favor, preencha todos os campos")

    if ent_user != USER or PASSWORD != ent_password:
        print("Usuário ou senha incorreto!")
        TENTATIVAS -= 1
        print(f"{TENTATIVAS} tentativas restantes")

    if ent_user == USER and ent_password == PASSWORD:
        print("Usuário logado com sucesso!")
        print(f"Olá {USER}, bem vindo ao nosso sistema!")
        break

    if TENTATIVAS == 0:
        print("Voce excedeu o máximo de tentativas.")
        break

print("Obrigado por escolher a Santz Technologies")
