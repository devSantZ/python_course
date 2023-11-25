"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""


def param(value):
    def duble_value(d_number):
        return 2 * value

    def triple_value(t_number):
        return 3 * value

    def quadruple_value(q_numer):
        return 4 * value

    return duble_value, triple_value, quadruple_value


user = int(input("Numero: "))
number = param(user)
duble_value, triple_value, quadruple_value = number
print(duble_value(number))
print(triple_value(number))
print(quadruple_value(number))


# def param(value):
#     def mult_value(number):
#         return number * value
#     return mult_value
#
#
# dobro = param(2)
# triplo = param(3)
# quadruplo = param(4)
#
# print(dobro(3))
# print(triplo(3))
# print(quadruplo(3))
