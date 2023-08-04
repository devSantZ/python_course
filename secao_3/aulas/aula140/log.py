# Abstração


class Log: # Template method
    def _log(self, msg): # Assinatura do método
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'error: {msg}')

    def log_success(self, msg):
        return self._log(f'success: {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} | {self.__class__.__name__}')
        
        
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('logando')
    l.log_success('logando')
