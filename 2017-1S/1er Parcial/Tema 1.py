letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
puntaje=[1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]
cadena=input("Ingrese las palabras a clasificar: ")
palabras=cadena.split(",")
puntosPalabras=[]
for palabra in palabras:
    puntoDePalabra=0
    for i in range(len(palabra)):
        if palabra[i] in letras:
            posicion=letras.index(palabra[i])
            puntos=puntaje[posicion]
            if palabra[i+1]=="*":
                puntos=puntos*2
            puntoDePalabra+=puntos
    puntosPalabras.append(puntoDePalabra)
print("Las calificaciones de las palabras son:")
for i in range(len(palabras)):
    palabras[i]=palabras[i].replace("*","")
    print(palabras[i].lower(),":",puntosPalabras[i])
maximo=max(puntosPalabras)
posicion=puntosPalabras.index(maximo)
print("La palabra con mayor puntaje es",palabras[posicion].replace("*","").upper(),"(",maximo,"puntos )",)