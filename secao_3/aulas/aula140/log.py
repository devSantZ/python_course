# Abstração
"""
A abstração envolve a criação de uma classe genérica, também conhecida como classe abstrata, que contém métodos     abstratos. Esses métodos são declarados na classe abstrata, mas não possuem uma implementação específica.

Em seguida, você cria classes especializadas, conhecidas como subclasses, que herdam da classe abstrata. Essas subclasses são responsáveis por fornecer a implementação dos métodos abstratos de acordo com suas necessidades específicas.

Na aula mencionada, a classe abstrata é a Log, enquanto as subclasses são LogPrintMixin e LogFileMixin. A classe Log define a estrutura básica e os métodos abstratos, enquanto as subclasses implementam esses métodos de acordo com suas funcionalidades específicas.

Portanto, a abstração em si envolve a criação dessa hierarquia de classes, onde uma classe abstrata fornece a base genérica e as subclasses especializadas aprimoram e implementam os detalhes específicos. Isso permite uma estrutura flexível e modular, onde comportamentos e funcionalidades podem ser compartilhados e adaptados de forma consistente.
"""
from abc import ABC, abstractmethod
from pathlib import Path
import datetime


#          caminho do módulo
#                  ^
LOG_FILE = Path(__file__).parent / "log.txt"
data_hour = datetime.datetime.now()
dt, hr = (data_hour.strftime("%Y-%m-%d"), data_hour.strftime("%H:%M:%S"))


class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f"error: {msg}")

    def log_success(self, msg):
        return self._log(f"success: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg}"  # {self.__class__.__name__}'
        with open(LOG_FILE, "a") as file:
            file.write(f"{dt}, {hr}\n{msg_formatada}\n")
            file.write("\n")

    # @property
    # def log(self):
    #     return self._log

    # @log.setter
    # def log(self, log):
    #     self.log = log


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} | {self.__class__.__name__}")


if __name__ == "__main__":
    # lp = LogPrintMixin()
    # lp.log_error('Não foi possivel logar (lp)')
    # lp.log_success('Sucesso ao logar (lp)')

    # lf = LogFileMixin()
    # lf.log_error('Não foi possivel acessar (lf)')
    # lf.log_success('Sucesso ao logar (lf)')
    ...
