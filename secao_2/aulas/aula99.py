from sys import path

from aula99_package.modulo import func_do_modulo
from aula99_package import modulo
import aula99_package.modulo

print(func_do_modulo(3, 5))
print(modulo.func_do_modulo(3, 5))
print(aula99_package.modulo.func_do_modulo(3, 5))