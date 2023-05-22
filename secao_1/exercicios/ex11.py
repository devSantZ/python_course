lista = ['Diego', 'Luís', 'Marcos', 'Pedro']

ad = -1
for i in lista:
    ad += 1
    print(ad, i)
    
# solução do professor
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])