from log import LogFileMixin

     
log = LogFileMixin()
    
    
class Eletronic:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
        
    def ligar(self):
        if not self._ligado:
            self._ligado = True
            log.log_success(f'{self._nome}, status: {self._ligado = }')
        
    def desligar(self):
        if self._ligado:
            self._ligado = False
            log.log_success(f'{self._nome}, status: {self._ligado = }')
            
            
    
class Smartphone(Eletronic):
    pass



# Herança multipla prof res
# class Eletronic:
#     def __init__(self, nome):
#         self._nome = nome
#         self._ligado = False
        
#     def ligar(self):
#         if not self._ligado:
#             self._ligado = True
            
#     def desligar(self):
#         if self._ligado:
#             self._ligado = False
            
            

# class Smartphone(Eletronic, LogFileMixin):
#     def ligar(self):
#         super().ligar()
#         if self._ligado:
#             self.log_success(f'{self._nome}, status: {self._ligado = }')
            
#     def desligar(self):
#         super().desligar()
#         if not self._ligado:
#             self.log_error(f'{self._nome}, status: {self._ligado = }')
