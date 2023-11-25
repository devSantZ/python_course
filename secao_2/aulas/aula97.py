"""
Modularização - Entendendo os seus próprios módulos Python
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por
padrão
O python conhece todos os módulos e pacotes presentes
nos caminhos de sys.path
"""
# import sys


# try:
#     sys.path.append('secao_2/aulas/aula97_modulo.py') # aplique o caminho do seu computador
#     from aula97_modulo import varialvel
#     print(varialvel)

# except ModuleNotFoundError as e:
#     print(f'Módulo não encontrado, erro {e}')


# print(*sys.path, sep='\n')
import aula97_modulo

print("Este módulo se chama", __name__)
