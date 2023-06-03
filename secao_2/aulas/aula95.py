"""
raise exception.
raise é usada para levantar (ou lançar) uma exceção.
Quando você encontra uma situação excepcional em seu
código, pode usar raise para interromper a execução 
normal e sinalizar que ocorreu um erro ou uma condição
especial.
sintaxe básica: raise Excecao("Mensagem de erro")
"""

def trata_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero')
    

def deve_ser_int_ou_float(n, d):
    tipo_n, tipo_d = type(n), type(d)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'voce enviou o tipo "{tipo_n.__name__}"', 
            f'use apenas o tipo "float" ou "int"'
        )
    if not isinstance(d, (int, float)):
        raise TypeError(
            f'voce enviou o tipo "{tipo_d.__name__}"', 
            f'use apenas o tipo "float" ou "int"'
        )
     

def divide(n, d):
    trata_zero(d)
    deve_ser_int_ou_float(n, d)
    return n / d

print(divide(3, '8'))