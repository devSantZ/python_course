from itertools import zip_longest


z = []

def lists_to_zip(x, y):
    def inner_function(func):
        def wapper(*args, **kwargs):
            z.append([i for i in zip(x, y)]) # ou z.append([i for i in zip_longest(x, y)]) -> usa a maior lista primeiro
            return z
        return wapper
    return inner_function


@lists_to_zip(['Salvador', 'Ubatuba', 'Belo Horizonte'],['BA', 'SP', 'MG', 'RJ'])
def zipper():
    pass


print(zipper())

# Solução do professor
# def zipper(x, y):
#     intervalo = min(len(x), len(y))
#     return [
#         (x[1], y[1]) for i in range(intervalo)
#     ]
    
# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# capital = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(cidades, capital))
