numero=[]
articulos=["el","las","los","la"]
a=input("ingrese una frase:")
b=a.split(" ")
for i in b:
    if i in articulos:
        numero.append(articulos)
print(len(numero))