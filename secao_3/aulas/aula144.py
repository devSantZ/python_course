"""
Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclasse sem quebrar a aplicação.
Sobrecarga de métodos (overload)  🐍 = ❌
Sobreposição de métodos (override) 🐍 = ✅
"""
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        pass
    

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'[SMS]: enviando: {self.mensagem}')
        

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'[E-mail]: enviando: {self.mensagem}')
        
        
def enviar_notificacao(mensagem: Notificacao):
    return mensagem.enviar()


enviar_notificacao(NotificacaoSMS('olá, testando SMS!'))
enviar_notificacao(NotificacaoEmail('olá, testando E-mail!'))