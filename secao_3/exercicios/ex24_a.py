import os
import json


BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, "ex24.json")


class Pessoa:
    def __init__(self, nome: str, idade: int, cidade: str):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def salvar(*args):
        with open(SAVE_TO, "w", encoding="utf8") as file:
            for i in args:
                json.dump(i, file, indent=2, ensure_ascii=False)


p1 = Pessoa("Carlos", 21, "São Paulo")
p2 = Pessoa("Marcos", 35, "Brasilia")
p3 = Pessoa("Junior", 2, "Itapecuru-Mirim")
data = [vars(p1), vars(p2), vars(p3)]


if __name__ == "__main__":
    Pessoa.salvar(data)
