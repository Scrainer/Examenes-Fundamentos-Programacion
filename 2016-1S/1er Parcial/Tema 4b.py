lista = [5,3,2,6,7,34,1,23,5,6]
lista2 = []

for i in range(1,len(lista)):
    if (lista[i-1] <= lista[i]) and (lista[i] >= lista[i+1]):
        lista2.append(lista[i])


print(lista2)