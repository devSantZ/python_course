# calculadora imc

nome = str((input("Qual seu nome? ")))
altura = float(input("Qual sua altura? "))
peso = float(input("Quanto voce pesa? "))
imc = peso / (altura**2)
print(imc)
