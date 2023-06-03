import sys


try:
    sys.path.append('/home/devsantz/Downloads') # aplique o caminho do seu computador
    import aula97_modulo
    
except ModuleNotFoundError as e:
    print(f'Módulo não encontrado, erro {e}')
    


print(*sys.path, sep='\n')
