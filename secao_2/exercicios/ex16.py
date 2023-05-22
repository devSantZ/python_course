"""
Sistema de perguntas e respostas com dicionários
"""

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

indice_pergunta = 0
indice_resposta = 0
acertos = 0
erros = 0

for i in perguntas:
    pergunta = (perguntas[indice_pergunta].get('Pergunta'))
    opcoes = (perguntas[indice_pergunta].get('Opções'))
    resposta = (perguntas[indice_pergunta].get('Resposta'))
    print(pergunta)
    for j, k in enumerate(opcoes):
        print(f'{j}) {k}')

    indice_pergunta += 1
    indice_opcoes = 0
    user = int(input('Escolha uma opção: '))
    if opcoes[user] == resposta:
        print('acertou')
        acertos += 1
    else:
        print('Errou')
        erros += 1

print(f'voce acertou {acertos} perguntas de um total de {len(perguntas)} e errou {erros}x')


# com funcoes

# def exibir_pergunta(pergunta):
#     print(pergunta['Pergunta'])
#     for indice, opcao in enumerate(pergunta['Opções']):
#         print(f'{indice}) {opcao}')
#
#
# def verificar_resposta(resposta_usuario, pergunta):
#     resposta_correta = pergunta['Resposta']
#     if pergunta['Opções'][resposta_usuario] == resposta_correta:
#         return True
#     else:
#         return False
#
#
# def jogar_quiz(perguntas):
#     acertos = 0
#     erros = 0
#
#     for pergunta in perguntas:
#         exibir_pergunta(pergunta)
#         resposta_usuario = int(input('Escolha uma opção (Digite o número correspondente): '))
#         if verificar_resposta(resposta_usuario, pergunta):
#             print('Acertou!')
#             acertos += 1
#         else:
#             print('Errou!')
#             erros += 1
#
#         print()  # Adiciona uma linha em branco para separar as perguntas
#
#     print(f'Você acertou {acertos} perguntas de um total de {len(perguntas)} e errou {erros} vezes.')
#
#
# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]
#
# jogar_quiz(perguntas)
#
