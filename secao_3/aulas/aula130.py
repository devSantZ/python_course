"""
method vs @classmethod vs @staticmethod
method - self, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático (❌self, ❌cls)
"""


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    # setters
    def set_user(self, user):
        self.user = user

    # setters
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_auth_user(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def load_connection(user, password):
        try:
            if user and password:
                return f"login success"
            return f"login failure"
        except ValueError:
            print("Error")


user3 = Connection.create_auth_user("Luana", "lu123")
print(user3.password)
try_connection_user3 = Connection.load_connection(user3.user, user3.password)
print(try_connection_user3)


user2 = Connection()
user2.set_user("santz")
user2.set_password(1234)

try_connection_user2 = Connection.load_connection(user2.user, user2.password)
print(try_connection_user2)
