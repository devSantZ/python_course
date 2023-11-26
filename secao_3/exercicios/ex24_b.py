from ex24_a import Pessoa
import json


with open("secao_3/exercicios/ex24.json", " r ") as file:
    data = json.load(file)
    p1 = Pessoa(**data[0])
    p2 = Pessoa(**data[1])
    p3 = Pessoa(**data[2])
    print(p1.nome, p2.nome, p3.nome)

